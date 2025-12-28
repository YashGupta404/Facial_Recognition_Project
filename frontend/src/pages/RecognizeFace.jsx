import { useState, useRef, useCallback, useEffect } from 'react';
import Webcam from 'react-webcam';
import { Scan, CheckCircle, AlertCircle, UserCheck, Clock } from 'lucide-react';
import * as faceapi from 'face-api.js';
import api from '../services/api';

export default function RecognizeFace() {
    const webcamRef = useRef(null);
    const [modelsLoaded, setModelsLoaded] = useState(false);
    const [registeredFaces, setRegisteredFaces] = useState([]);
    const [isRecognizing, setIsRecognizing] = useState(false);
    const [recognizedUser, setRecognizedUser] = useState(null);
    const [recentAttendance, setRecentAttendance] = useState([]);
    const [status, setStatus] = useState({ type: '', message: '' });
    const [loading, setLoading] = useState(true);

    // Load models and registered faces
    useEffect(() => {
        const initialize = async () => {
            try {
                const MODEL_URL = '/models';
                await Promise.all([
                    faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URL),
                    faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL),
                    faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL),
                ]);
                setModelsLoaded(true);

                // Fetch users with face data
                const users = await api.users.getWithFace();
                setRegisteredFaces(users);

                // Fetch today's attendance
                await fetchTodayAttendance();

                setStatus({ type: 'success', message: 'System ready for recognition!' });
            } catch (error) {
                console.error('Initialization error:', error);
                setStatus({ type: 'error', message: 'Failed to initialize. Check console for details.' });
            } finally {
                setLoading(false);
            }
        };

        initialize();
    }, []);

    const fetchTodayAttendance = async () => {
        try {
            const data = await api.attendance.getToday();
            setRecentAttendance(data.slice(0, 10)); // Show last 10
        } catch (error) {
            console.error('Failed to fetch attendance:', error);
        }
    };

    const findMatch = (descriptor, registeredFaces) => {
        let bestMatch = null;
        let minDistance = 0.6; // Threshold for matching

        for (const user of registeredFaces) {
            if (!user.face_encoding) continue;

            let storedDescriptor;
            try {
                storedDescriptor = JSON.parse(user.face_encoding);
            } catch {
                continue;
            }

            // Calculate Euclidean distance
            const distance = Math.sqrt(
                descriptor.reduce((sum, val, idx) => sum + Math.pow(val - storedDescriptor[idx], 2), 0)
            );

            if (distance < minDistance) {
                minDistance = distance;
                bestMatch = {
                    ...user,
                    confidence: Math.round((1 - distance) * 100),
                };
            }
        }

        return bestMatch;
    };

    const startRecognition = useCallback(async () => {
        if (!webcamRef.current || !modelsLoaded || registeredFaces.length === 0) {
            setStatus({ type: 'error', message: 'System not ready or no faces registered.' });
            return;
        }

        setIsRecognizing(true);
        setRecognizedUser(null);
        setStatus({ type: '', message: 'Looking for face...' });

        const video = webcamRef.current.video;

        // Try recognition multiple times
        for (let attempt = 0; attempt < 5; attempt++) {
            const detection = await faceapi
                .detectSingleFace(video, new faceapi.TinyFaceDetectorOptions())
                .withFaceLandmarks()
                .withFaceDescriptor();

            if (detection) {
                setStatus({ type: '', message: 'Face detected! Matching...' });

                const match = findMatch(Array.from(detection.descriptor), registeredFaces);

                if (match) {
                    setRecognizedUser(match);
                    setStatus({ type: 'success', message: `Recognized: ${match.name}` });

                    // Mark attendance
                    try {
                        await api.attendance.mark({
                            student_id: match.student_id,
                            name: match.name,
                            roll_no: match.roll_no,
                            department: match.department,
                        });
                        setStatus({ type: 'success', message: `Attendance marked for ${match.name}!` });
                        fetchTodayAttendance();
                    } catch (error) {
                        if (error.message.includes('already marked')) {
                            setStatus({ type: 'warning', message: `${match.name} - Attendance already marked today!` });
                        } else {
                            setStatus({ type: 'error', message: error.message });
                        }
                    }

                    setIsRecognizing(false);
                    return;
                }
            }

            await new Promise((resolve) => setTimeout(resolve, 500));
        }

        setStatus({ type: 'error', message: 'Face not recognized. Please try again.' });
        setIsRecognizing(false);
    }, [modelsLoaded, registeredFaces]);

    // Auto-recognition mode
    const [autoMode, setAutoMode] = useState(false);

    useEffect(() => {
        if (!autoMode || !modelsLoaded) return;

        const interval = setInterval(() => {
            if (!isRecognizing) {
                startRecognition();
            }
        }, 3000);

        return () => clearInterval(interval);
    }, [autoMode, modelsLoaded, isRecognizing, startRecognition]);

    if (loading) {
        return (
            <div className="loading-container">
                <div className="spinner"></div>
                <p>Initializing face recognition system...</p>
            </div>
        );
    }

    return (
        <div>
            <div className="page-header">
                <h1 className="page-title">Face Recognition</h1>
                <p className="page-subtitle">Mark attendance using face recognition</p>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 400px', gap: '1.5rem' }}>
                {/* Main Recognition Area */}
                <div className="card">
                    <div className="card-header">
                        <h2 className="card-title">
                            <Scan size={20} />
                            Recognition Camera
                        </h2>
                        <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
                            <label style={{ fontSize: '0.875rem', color: 'var(--text-muted)' }}>Auto Mode</label>
                            <input
                                type="checkbox"
                                checked={autoMode}
                                onChange={(e) => setAutoMode(e.target.checked)}
                                style={{ width: '20px', height: '20px' }}
                            />
                        </div>
                    </div>

                    <div className="webcam-container">
                        <Webcam
                            ref={webcamRef}
                            audio={false}
                            screenshotFormat="image/jpeg"
                            className="webcam-video"
                            videoConstraints={{
                                width: 640,
                                height: 480,
                                facingMode: 'user',
                            }}
                        />

                        {isRecognizing && (
                            <div className="recognition-status">
                                <div className="pulse-dot"></div>
                                <span>Scanning...</span>
                            </div>
                        )}
                    </div>

                    <div style={{ marginTop: '1.5rem', display: 'flex', gap: '1rem' }}>
                        <button
                            className="btn btn-primary btn-lg"
                            style={{ flex: 1 }}
                            onClick={startRecognition}
                            disabled={isRecognizing || registeredFaces.length === 0}
                        >
                            <Scan size={20} />
                            {isRecognizing ? 'Recognizing...' : 'Recognize Face'}
                        </button>
                    </div>

                    {status.message && (
                        <div className={`toast ${status.type}`} style={{ marginTop: '1rem', minWidth: 'auto' }}>
                            {status.type === 'success' ? (
                                <CheckCircle size={20} />
                            ) : status.type === 'error' ? (
                                <AlertCircle size={20} />
                            ) : (
                                <Clock size={20} />
                            )}
                            <span>{status.message}</span>
                        </div>
                    )}

                    {/* Recognized User Card */}
                    {recognizedUser && (
                        <div
                            style={{
                                marginTop: '1.5rem',
                                padding: '1.5rem',
                                background: 'var(--success-bg)',
                                borderRadius: 'var(--radius-md)',
                                border: '1px solid var(--success)',
                                display: 'flex',
                                alignItems: 'center',
                                gap: '1rem',
                            }}
                        >
                            <div
                                style={{
                                    width: '60px',
                                    height: '60px',
                                    background: 'var(--success)',
                                    borderRadius: '50%',
                                    display: 'flex',
                                    alignItems: 'center',
                                    justifyContent: 'center',
                                }}
                            >
                                <UserCheck size={30} color="white" />
                            </div>
                            <div>
                                <h3 style={{ color: 'var(--success)' }}>{recognizedUser.name}</h3>
                                <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>
                                    ID: {recognizedUser.student_id} | Confidence: {recognizedUser.confidence}%
                                </p>
                            </div>
                        </div>
                    )}
                </div>

                {/* Sidebar - Recent Attendance */}
                <div className="card">
                    <div className="card-header">
                        <h2 className="card-title">
                            <Clock size={20} />
                            Today's Attendance
                        </h2>
                        <span className="badge badge-success">{recentAttendance.length}</span>
                    </div>

                    {recentAttendance.length === 0 ? (
                        <div className="empty-state" style={{ padding: '2rem' }}>
                            <UserCheck size={40} style={{ marginBottom: '1rem', opacity: 0.5 }} />
                            <p>No attendance marked yet today</p>
                        </div>
                    ) : (
                        <div style={{ maxHeight: '500px', overflowY: 'auto' }}>
                            {recentAttendance.map((record, index) => (
                                <div
                                    key={record.id || index}
                                    style={{
                                        padding: '0.75rem',
                                        borderBottom: '1px solid var(--border-color)',
                                        display: 'flex',
                                        justifyContent: 'space-between',
                                        alignItems: 'center',
                                    }}
                                >
                                    <div>
                                        <p style={{ fontWeight: '500' }}>{record.name}</p>
                                        <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                                            {record.student_id}
                                        </p>
                                    </div>
                                    <div style={{ textAlign: 'right' }}>
                                        <span className="badge badge-success">{record.attendance_status}</span>
                                        <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.25rem' }}>
                                            {record.check_in_time?.slice(0, 5) || '--:--'}
                                        </p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}

                    {registeredFaces.length === 0 && (
                        <div
                            style={{
                                marginTop: '1rem',
                                padding: '1rem',
                                background: 'var(--warning-bg)',
                                borderRadius: 'var(--radius-md)',
                                border: '1px solid var(--warning)',
                            }}
                        >
                            <p style={{ color: 'var(--warning)', fontSize: '0.875rem' }}>
                                ⚠️ No faces registered yet. Go to "Register Face" to add users.
                            </p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

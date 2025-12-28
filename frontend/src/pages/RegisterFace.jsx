import { useState, useRef, useCallback, useEffect } from 'react';
import Webcam from 'react-webcam';
import { Camera, CheckCircle, AlertCircle, User, RefreshCw } from 'lucide-react';
import * as faceapi from 'face-api.js';
import api from '../services/api';

export default function RegisterFace() {
    const webcamRef = useRef(null);
    const canvasRef = useRef(null);
    const [users, setUsers] = useState([]);
    const [selectedUser, setSelectedUser] = useState('');
    const [modelsLoaded, setModelsLoaded] = useState(false);
    const [loading, setLoading] = useState(true);
    const [capturing, setCapturing] = useState(false);
    const [capturedImages, setCapturedImages] = useState(0);
    const [status, setStatus] = useState({ type: '', message: '' });
    const [faceDetected, setFaceDetected] = useState(false);

    // Load face-api models
    useEffect(() => {
        const loadModels = async () => {
            try {
                const MODEL_URL = '/models';
                await Promise.all([
                    faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URL),
                    faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL),
                    faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL),
                ]);
                setModelsLoaded(true);
                setStatus({ type: 'success', message: 'Face detection models loaded!' });
            } catch (error) {
                console.error('Failed to load models:', error);
                setStatus({ type: 'error', message: 'Failed to load face detection models. Please check /public/models folder.' });
            }
        };

        loadModels();
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            const data = await api.users.getAll();
            // Filter users who don't have face registered yet
            const usersWithoutFace = data.filter((u) => u.photo_sample_status !== 'Yes');
            setUsers(usersWithoutFace);
        } catch (error) {
            console.error('Failed to fetch users:', error);
        } finally {
            setLoading(false);
        }
    };

    // Detect face in video stream
    useEffect(() => {
        if (!modelsLoaded || !webcamRef.current) return;

        const detectFace = async () => {
            if (webcamRef.current?.video?.readyState === 4) {
                const video = webcamRef.current.video;
                const detection = await faceapi.detectSingleFace(
                    video,
                    new faceapi.TinyFaceDetectorOptions()
                );
                setFaceDetected(!!detection);
            }
        };

        const interval = setInterval(detectFace, 500);
        return () => clearInterval(interval);
    }, [modelsLoaded]);

    const captureFaceData = useCallback(async () => {
        if (!selectedUser) {
            setStatus({ type: 'error', message: 'Please select a user first!' });
            return;
        }

        if (!webcamRef.current || !modelsLoaded) return;

        setCapturing(true);
        setStatus({ type: '', message: 'Capturing face data... Please look at the camera.' });

        const video = webcamRef.current.video;
        const descriptors = [];

        // Capture multiple samples for better accuracy
        for (let i = 0; i < 5; i++) {
            const detection = await faceapi
                .detectSingleFace(video, new faceapi.TinyFaceDetectorOptions())
                .withFaceLandmarks()
                .withFaceDescriptor();

            if (detection) {
                descriptors.push(Array.from(detection.descriptor));
                setCapturedImages((prev) => prev + 1);
                setStatus({ type: 'success', message: `Captured ${i + 1}/5 samples...` });
            }

            // Wait between captures
            await new Promise((resolve) => setTimeout(resolve, 500));
        }

        if (descriptors.length < 3) {
            setStatus({ type: 'error', message: 'Could not capture enough face samples. Please try again.' });
            setCapturing(false);
            setCapturedImages(0);
            return;
        }

        // Average the descriptors
        const avgDescriptor = descriptors[0].map((_, idx) => {
            const sum = descriptors.reduce((acc, desc) => acc + desc[idx], 0);
            return sum / descriptors.length;
        });

        try {
            await api.users.saveFaceEncoding(selectedUser, avgDescriptor);
            setStatus({ type: 'success', message: 'Face data registered successfully!' });

            // Refresh user list
            fetchUsers();
            setSelectedUser('');
            setCapturedImages(0);
        } catch (error) {
            setStatus({ type: 'error', message: 'Failed to save face data: ' + error.message });
        }

        setCapturing(false);
    }, [selectedUser, modelsLoaded]);

    if (loading) {
        return (
            <div className="loading-container">
                <div className="spinner"></div>
                <p>Loading...</p>
            </div>
        );
    }

    return (
        <div>
            <div className="page-header">
                <h1 className="page-title">Register Face</h1>
                <p className="page-subtitle">Capture face data for a user to enable face recognition</p>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
                {/* Webcam Section */}
                <div className="card">
                    <div className="card-header">
                        <h2 className="card-title">
                            <Camera size={20} />
                            Camera Feed
                        </h2>
                        {faceDetected && (
                            <span className="badge badge-success">
                                <CheckCircle size={14} /> Face Detected
                            </span>
                        )}
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
                        <canvas ref={canvasRef} className="webcam-overlay" />

                        {capturing && (
                            <div className="recognition-status">
                                <div className="pulse-dot"></div>
                                <span>Capturing... {capturedImages}/5</span>
                            </div>
                        )}
                    </div>

                    {!modelsLoaded && (
                        <div style={{ padding: '1rem', textAlign: 'center' }}>
                            <div className="spinner" style={{ margin: '0 auto 1rem' }}></div>
                            <p>Loading face detection models...</p>
                        </div>
                    )}
                </div>

                {/* Controls Section */}
                <div className="card">
                    <div className="card-header">
                        <h2 className="card-title">
                            <User size={20} />
                            User Selection
                        </h2>
                    </div>

                    <div className="form-group">
                        <label className="form-label">Select User to Register</label>
                        <select
                            className="form-select"
                            value={selectedUser}
                            onChange={(e) => setSelectedUser(e.target.value)}
                            disabled={capturing}
                        >
                            <option value="">-- Select a User --</option>
                            {users.map((user) => (
                                <option key={user.id} value={user.student_id}>
                                    {user.name} ({user.student_id})
                                </option>
                            ))}
                        </select>
                    </div>

                    {users.length === 0 && (
                        <div className="empty-state" style={{ padding: '2rem' }}>
                            <AlertCircle size={40} style={{ marginBottom: '1rem', color: 'var(--warning)' }} />
                            <h3>No users available</h3>
                            <p>All registered users already have face data, or no users are registered yet.</p>
                        </div>
                    )}

                    <button
                        className="btn btn-primary btn-lg"
                        style={{ width: '100%', marginTop: '1rem' }}
                        onClick={captureFaceData}
                        disabled={!selectedUser || !modelsLoaded || capturing || !faceDetected}
                    >
                        {capturing ? (
                            <>
                                <RefreshCw size={20} className="spin" />
                                Capturing...
                            </>
                        ) : (
                            <>
                                <Camera size={20} />
                                Capture Face Data
                            </>
                        )}
                    </button>

                    {status.message && (
                        <div
                            className={`toast ${status.type}`}
                            style={{ marginTop: '1rem', minWidth: 'auto' }}
                        >
                            {status.type === 'success' ? (
                                <CheckCircle size={20} />
                            ) : (
                                <AlertCircle size={20} />
                            )}
                            <span>{status.message}</span>
                        </div>
                    )}

                    <div style={{ marginTop: '2rem', padding: '1rem', background: 'var(--bg-secondary)', borderRadius: 'var(--radius-md)' }}>
                        <h4 style={{ marginBottom: '0.5rem' }}>Tips for best results:</h4>
                        <ul style={{ color: 'var(--text-muted)', fontSize: '0.875rem', paddingLeft: '1.25rem' }}>
                            <li>Ensure good lighting on your face</li>
                            <li>Look directly at the camera</li>
                            <li>Remove glasses if possible</li>
                            <li>Keep your face centered in the frame</li>
                            <li>Stay still during capture</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
}

import { useState, useEffect } from 'react';
import { Calendar, Download, Search, Trash2, Filter } from 'lucide-react';
import api from '../services/api';

export default function AttendancePage() {
    const [attendance, setAttendance] = useState([]);
    const [loading, setLoading] = useState(true);
    const [dateFilter, setDateFilter] = useState(new Date().toISOString().split('T')[0]);
    const [searchTerm, setSearchTerm] = useState('');
    const [stats, setStats] = useState(null);

    useEffect(() => {
        fetchAttendance();
        fetchStats();
    }, [dateFilter]);

    const fetchAttendance = async () => {
        setLoading(true);
        try {
            const data = await api.attendance.getAll({ date: dateFilter });
            setAttendance(data);
        } catch (error) {
            console.error('Failed to fetch attendance:', error);
        } finally {
            setLoading(false);
        }
    };

    const fetchStats = async () => {
        try {
            const data = await api.attendance.getTodayStats();
            setStats(data);
        } catch (error) {
            console.error('Failed to fetch stats:', error);
        }
    };

    const handleDelete = async (id) => {
        if (window.confirm('Are you sure you want to delete this attendance record?')) {
            try {
                await api.attendance.delete(id);
                fetchAttendance();
                fetchStats();
            } catch (error) {
                alert('Failed to delete: ' + error.message);
            }
        }
    };

    const exportToCSV = () => {
        if (attendance.length === 0) {
            alert('No data to export');
            return;
        }

        const headers = ['ID', 'Student ID', 'Name', 'Roll No', 'Department', 'Status', 'Time', 'Date'];
        const rows = attendance.map((a) => [
            a.id,
            a.student_id,
            a.name,
            a.roll_no,
            a.department,
            a.attendance_status,
            a.check_in_time,
            a.attendance_date,
        ]);

        const csvContent =
            'data:text/csv;charset=utf-8,' +
            [headers.join(','), ...rows.map((r) => r.join(','))].join('\n');

        const link = document.createElement('a');
        link.href = encodeURI(csvContent);
        link.download = `attendance_${dateFilter}.csv`;
        link.click();
    };

    const filteredAttendance = attendance.filter(
        (record) =>
            record.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
            record.student_id?.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div>
            <div className="page-header">
                <h1 className="page-title">Attendance Records</h1>
                <p className="page-subtitle">View and manage attendance history</p>
            </div>

            {/* Stats Cards */}
            {stats && (
                <div className="stats-grid" style={{ marginBottom: '1.5rem' }}>
                    <div className="stat-card">
                        <div className="stat-icon primary">
                            <Calendar size={28} />
                        </div>
                        <div className="stat-info">
                            <h3>{stats.date}</h3>
                            <p>Selected Date</p>
                        </div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-icon success">
                            <span style={{ fontSize: '1.5rem' }}>✓</span>
                        </div>
                        <div className="stat-info">
                            <h3>{stats.present}</h3>
                            <p>Present</p>
                        </div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-icon danger">
                            <span style={{ fontSize: '1.5rem' }}>✗</span>
                        </div>
                        <div className="stat-info">
                            <h3>{stats.absent}</h3>
                            <p>Absent</p>
                        </div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-icon warning">
                            <span style={{ fontSize: '1.5rem' }}>%</span>
                        </div>
                        <div className="stat-info">
                            <h3>{stats.attendance_percentage}%</h3>
                            <p>Attendance Rate</p>
                        </div>
                    </div>
                </div>
            )}

            {/* Filters */}
            <div className="card" style={{ marginBottom: '1.5rem' }}>
                <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', alignItems: 'center' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <Filter size={18} style={{ color: 'var(--text-muted)' }} />
                        <input
                            type="date"
                            className="form-input"
                            value={dateFilter}
                            onChange={(e) => setDateFilter(e.target.value)}
                            style={{ width: 'auto' }}
                        />
                    </div>

                    <div style={{ position: 'relative', flex: 1, maxWidth: '300px' }}>
                        <Search
                            size={18}
                            style={{
                                position: 'absolute',
                                left: '12px',
                                top: '50%',
                                transform: 'translateY(-50%)',
                                color: 'var(--text-muted)',
                            }}
                        />
                        <input
                            type="text"
                            className="form-input"
                            placeholder="Search by name or ID..."
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                            style={{ paddingLeft: '40px' }}
                        />
                    </div>

                    <div style={{ marginLeft: 'auto' }}>
                        <button className="btn btn-secondary" onClick={exportToCSV}>
                            <Download size={18} />
                            Export CSV
                        </button>
                    </div>
                </div>
            </div>

            {/* Attendance Table */}
            <div className="card">
                {loading ? (
                    <div className="loading-container">
                        <div className="spinner"></div>
                        <p>Loading attendance records...</p>
                    </div>
                ) : filteredAttendance.length === 0 ? (
                    <div className="empty-state">
                        <div className="empty-state-icon">
                            <Calendar size={40} />
                        </div>
                        <h3>No attendance records found</h3>
                        <p>No attendance has been marked for the selected date.</p>
                    </div>
                ) : (
                    <div className="table-container">
                        <table className="data-table">
                            <thead>
                                <tr>
                                    <th>Student ID</th>
                                    <th>Name</th>
                                    <th>Roll No</th>
                                    <th>Department</th>
                                    <th>Status</th>
                                    <th>Time</th>
                                    <th>Date</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredAttendance.map((record) => (
                                    <tr key={record.id}>
                                        <td>{record.student_id}</td>
                                        <td>{record.name || '-'}</td>
                                        <td>{record.roll_no || '-'}</td>
                                        <td>{record.department || '-'}</td>
                                        <td>
                                            <span
                                                className={`badge ${record.attendance_status === 'Present'
                                                        ? 'badge-success'
                                                        : record.attendance_status === 'Absent'
                                                            ? 'badge-danger'
                                                            : 'badge-warning'
                                                    }`}
                                            >
                                                {record.attendance_status}
                                            </span>
                                        </td>
                                        <td>{record.check_in_time?.slice(0, 8) || '-'}</td>
                                        <td>{record.attendance_date}</td>
                                        <td>
                                            <button
                                                className="btn btn-danger"
                                                style={{ padding: '0.5rem' }}
                                                onClick={() => handleDelete(record.id)}
                                            >
                                                <Trash2 size={16} />
                                            </button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                )}
            </div>
        </div>
    );
}

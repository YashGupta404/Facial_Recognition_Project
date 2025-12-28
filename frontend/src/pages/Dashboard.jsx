import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Users, UserCheck, UserX, BarChart3, Camera, Scan, ClipboardList, Plus } from 'lucide-react';
import api from '../services/api';

export default function Dashboard() {
    const [stats, setStats] = useState({
        total_registered: 0,
        present: 0,
        absent: 0,
        attendance_percentage: 0,
    });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchStats = async () => {
            try {
                const data = await api.attendance.getTodayStats();
                setStats(data);
            } catch (error) {
                console.error('Failed to fetch stats:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchStats();
    }, []);

    const statCards = [
        {
            label: 'Total Registered',
            value: stats.total_registered,
            icon: Users,
            colorClass: 'primary',
        },
        {
            label: 'Present Today',
            value: stats.present,
            icon: UserCheck,
            colorClass: 'success',
        },
        {
            label: 'Absent Today',
            value: stats.absent,
            icon: UserX,
            colorClass: 'danger',
        },
        {
            label: 'Attendance Rate',
            value: `${stats.attendance_percentage}%`,
            icon: BarChart3,
            colorClass: 'warning',
        },
    ];

    const quickActions = [
        {
            title: 'Add New User',
            description: 'Register a new student in the system',
            icon: Plus,
            link: '/users?add=true',
        },
        {
            title: 'Register Face',
            description: 'Capture and store face data for recognition',
            icon: Camera,
            link: '/register-face',
        },
        {
            title: 'Take Attendance',
            description: 'Start face recognition to mark attendance',
            icon: Scan,
            link: '/recognize',
        },
        {
            title: 'View Reports',
            description: 'Access attendance records and reports',
            icon: ClipboardList,
            link: '/attendance',
        },
    ];

    if (loading) {
        return (
            <div className="loading-container">
                <div className="spinner"></div>
                <p>Loading dashboard...</p>
            </div>
        );
    }

    return (
        <div>
            <div className="page-header">
                <h1 className="page-title">Dashboard</h1>
                <p className="page-subtitle">Welcome to the Facial Recognition Attendance System</p>
            </div>

            {/* Stats Grid */}
            <div className="stats-grid">
                {statCards.map((stat, index) => (
                    <div key={index} className="stat-card">
                        <div className={`stat-icon ${stat.colorClass}`}>
                            <stat.icon size={28} />
                        </div>
                        <div className="stat-info">
                            <h3>{stat.value}</h3>
                            <p>{stat.label}</p>
                        </div>
                    </div>
                ))}
            </div>

            {/* Quick Actions */}
            <div className="card">
                <div className="card-header">
                    <h2 className="card-title">Quick Actions</h2>
                </div>
                <div className="quick-actions">
                    {quickActions.map((action, index) => (
                        <Link key={index} to={action.link} className="action-card">
                            <div className="action-icon">
                                <action.icon size={28} />
                            </div>
                            <h3>{action.title}</h3>
                            <p>{action.description}</p>
                        </Link>
                    ))}
                </div>
            </div>
        </div>
    );
}

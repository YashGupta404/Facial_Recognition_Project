import { Link, useLocation } from 'react-router-dom';
import { Home, Users, Camera, ClipboardList, Scan } from 'lucide-react';

export default function Navbar() {
    const location = useLocation();

    const navItems = [
        { path: '/', label: 'Dashboard', icon: Home },
        { path: '/users', label: 'Users', icon: Users },
        { path: '/register-face', label: 'Register Face', icon: Camera },
        { path: '/recognize', label: 'Recognize', icon: Scan },
        { path: '/attendance', label: 'Attendance', icon: ClipboardList },
    ];

    return (
        <nav className="navbar">
            <div className="navbar-content">
                <Link to="/" className="logo">
                    <div className="logo-icon">
                        <Scan size={24} color="white" />
                    </div>
                    <span className="logo-text">FaceRecog</span>
                </Link>

                <div className="nav-links">
                    {navItems.map(({ path, label, icon: Icon }) => (
                        <Link
                            key={path}
                            to={path}
                            className={`nav-link ${location.pathname === path ? 'active' : ''}`}
                        >
                            <Icon size={18} />
                            <span>{label}</span>
                        </Link>
                    ))}
                </div>
            </div>
        </nav>
    );
}

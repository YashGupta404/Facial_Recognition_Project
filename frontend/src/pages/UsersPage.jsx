import { useState, useEffect } from 'react';
import { Plus, Edit2, Trash2, Search, X, UserCircle } from 'lucide-react';
import api from '../services/api';

export default function UsersPage() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');
    const [showModal, setShowModal] = useState(false);
    const [editingUser, setEditingUser] = useState(null);
    const [formData, setFormData] = useState({
        student_id: '',
        name: '',
        email: '',
        phone: '',
        department: '',
        course: '',
        year: '',
        semester: '',
        division: '',
        roll_no: '',
        gender: '',
        address: '',
        teacher_name: '',
    });

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            const data = await api.users.getAll();
            setUsers(data);
        } catch (error) {
            console.error('Failed to fetch users:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (editingUser) {
                await api.users.update(editingUser.student_id, formData);
            } else {
                await api.users.create(formData);
            }
            fetchUsers();
            closeModal();
        } catch (error) {
            alert(error.message);
        }
    };

    const handleEdit = (user) => {
        setEditingUser(user);
        setFormData({
            student_id: user.student_id || '',
            name: user.name || '',
            email: user.email || '',
            phone: user.phone || '',
            department: user.department || '',
            course: user.course || '',
            year: user.year || '',
            semester: user.semester || '',
            division: user.division || '',
            roll_no: user.roll_no || '',
            gender: user.gender || '',
            address: user.address || '',
            teacher_name: user.teacher_name || '',
        });
        setShowModal(true);
    };

    const handleDelete = async (studentId) => {
        if (window.confirm('Are you sure you want to delete this user?')) {
            try {
                await api.users.delete(studentId);
                fetchUsers();
            } catch (error) {
                alert(error.message);
            }
        }
    };

    const closeModal = () => {
        setShowModal(false);
        setEditingUser(null);
        setFormData({
            student_id: '',
            name: '',
            email: '',
            phone: '',
            department: '',
            course: '',
            year: '',
            semester: '',
            division: '',
            roll_no: '',
            gender: '',
            address: '',
            teacher_name: '',
        });
    };

    const filteredUsers = users.filter(
        (user) =>
            user.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
            user.student_id?.toLowerCase().includes(searchTerm.toLowerCase()) ||
            user.email?.toLowerCase().includes(searchTerm.toLowerCase())
    );

    if (loading) {
        return (
            <div className="loading-container">
                <div className="spinner"></div>
                <p>Loading users...</p>
            </div>
        );
    }

    return (
        <div>
            <div className="page-header">
                <h1 className="page-title">User Management</h1>
                <p className="page-subtitle">Manage registered students and their details</p>
            </div>

            {/* Actions Bar */}
            <div className="card" style={{ marginBottom: '1.5rem' }}>
                <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', justifyContent: 'space-between' }}>
                    <div style={{ position: 'relative', flex: 1, maxWidth: '400px' }}>
                        <Search size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                        <input
                            type="text"
                            className="form-input"
                            placeholder="Search by name, ID, or email..."
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                            style={{ paddingLeft: '40px' }}
                        />
                    </div>
                    <button className="btn btn-primary" onClick={() => setShowModal(true)}>
                        <Plus size={18} />
                        Add User
                    </button>
                </div>
            </div>

            {/* Users Table */}
            <div className="card">
                {filteredUsers.length === 0 ? (
                    <div className="empty-state">
                        <div className="empty-state-icon">
                            <UserCircle size={40} />
                        </div>
                        <h3>No users found</h3>
                        <p>Add your first user to get started with face recognition</p>
                    </div>
                ) : (
                    <div className="table-container">
                        <table className="data-table">
                            <thead>
                                <tr>
                                    <th>Student ID</th>
                                    <th>Name</th>
                                    <th>Department</th>
                                    <th>Course</th>
                                    <th>Email</th>
                                    <th>Face Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredUsers.map((user) => (
                                    <tr key={user.id}>
                                        <td>{user.student_id}</td>
                                        <td>{user.name}</td>
                                        <td>{user.department || '-'}</td>
                                        <td>{user.course || '-'}</td>
                                        <td>{user.email || '-'}</td>
                                        <td>
                                            <span className={`badge ${user.photo_sample_status === 'Yes' ? 'badge-success' : 'badge-warning'}`}>
                                                {user.photo_sample_status === 'Yes' ? 'Registered' : 'Pending'}
                                            </span>
                                        </td>
                                        <td>
                                            <div style={{ display: 'flex', gap: '0.5rem' }}>
                                                <button
                                                    className="btn btn-secondary"
                                                    style={{ padding: '0.5rem' }}
                                                    onClick={() => handleEdit(user)}
                                                >
                                                    <Edit2 size={16} />
                                                </button>
                                                <button
                                                    className="btn btn-danger"
                                                    style={{ padding: '0.5rem' }}
                                                    onClick={() => handleDelete(user.student_id)}
                                                >
                                                    <Trash2 size={16} />
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                )}
            </div>

            {/* Add/Edit Modal */}
            {showModal && (
                <div className="modal-overlay" onClick={closeModal}>
                    <div className="modal" onClick={(e) => e.stopPropagation()}>
                        <div className="modal-header">
                            <h2 className="modal-title">{editingUser ? 'Edit User' : 'Add New User'}</h2>
                            <button className="modal-close" onClick={closeModal}>
                                <X size={20} />
                            </button>
                        </div>
                        <form onSubmit={handleSubmit}>
                            <div className="modal-body">
                                <div className="form-grid">
                                    <div className="form-group">
                                        <label className="form-label">Student ID *</label>
                                        <input
                                            type="text"
                                            name="student_id"
                                            className="form-input"
                                            value={formData.student_id}
                                            onChange={handleInputChange}
                                            required
                                            disabled={editingUser}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Full Name *</label>
                                        <input
                                            type="text"
                                            name="name"
                                            className="form-input"
                                            value={formData.name}
                                            onChange={handleInputChange}
                                            required
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Email</label>
                                        <input
                                            type="email"
                                            name="email"
                                            className="form-input"
                                            value={formData.email}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Phone</label>
                                        <input
                                            type="tel"
                                            name="phone"
                                            className="form-input"
                                            value={formData.phone}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Department</label>
                                        <select
                                            name="department"
                                            className="form-select"
                                            value={formData.department}
                                            onChange={handleInputChange}
                                        >
                                            <option value="">Select Department</option>
                                            <option value="Computer">Computer</option>
                                            <option value="IT">IT</option>
                                            <option value="Civil">Civil</option>
                                            <option value="Mechanical">Mechanical</option>
                                            <option value="Electrical">Electrical</option>
                                        </select>
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Course</label>
                                        <select
                                            name="course"
                                            className="form-select"
                                            value={formData.course}
                                            onChange={handleInputChange}
                                        >
                                            <option value="">Select Course</option>
                                            <option value="FE">FE</option>
                                            <option value="SE">SE</option>
                                            <option value="TE">TE</option>
                                            <option value="BE">BE</option>
                                        </select>
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Year</label>
                                        <select
                                            name="year"
                                            className="form-select"
                                            value={formData.year}
                                            onChange={handleInputChange}
                                        >
                                            <option value="">Select Year</option>
                                            <option value="1">1st Year</option>
                                            <option value="2">2nd Year</option>
                                            <option value="3">3rd Year</option>
                                            <option value="4">4th Year</option>
                                        </select>
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Semester</label>
                                        <select
                                            name="semester"
                                            className="form-select"
                                            value={formData.semester}
                                            onChange={handleInputChange}
                                        >
                                            <option value="">Select Semester</option>
                                            <option value="1">1</option>
                                            <option value="2">2</option>
                                        </select>
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Division</label>
                                        <select
                                            name="division"
                                            className="form-select"
                                            value={formData.division}
                                            onChange={handleInputChange}
                                        >
                                            <option value="">Select Division</option>
                                            <option value="A">A</option>
                                            <option value="B">B</option>
                                            <option value="C">C</option>
                                            <option value="D">D</option>
                                        </select>
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Roll No</label>
                                        <input
                                            type="text"
                                            name="roll_no"
                                            className="form-input"
                                            value={formData.roll_no}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Gender</label>
                                        <select
                                            name="gender"
                                            className="form-select"
                                            value={formData.gender}
                                            onChange={handleInputChange}
                                        >
                                            <option value="">Select Gender</option>
                                            <option value="Male">Male</option>
                                            <option value="Female">Female</option>
                                            <option value="Other">Other</option>
                                        </select>
                                    </div>
                                    <div className="form-group">
                                        <label className="form-label">Teacher Name</label>
                                        <input
                                            type="text"
                                            name="teacher_name"
                                            className="form-input"
                                            value={formData.teacher_name}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                </div>
                                <div className="form-group">
                                    <label className="form-label">Address</label>
                                    <input
                                        type="text"
                                        name="address"
                                        className="form-input"
                                        value={formData.address}
                                        onChange={handleInputChange}
                                    />
                                </div>
                            </div>
                            <div className="modal-footer">
                                <button type="button" className="btn btn-secondary" onClick={closeModal}>
                                    Cancel
                                </button>
                                <button type="submit" className="btn btn-primary">
                                    {editingUser ? 'Update User' : 'Add User'}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
}

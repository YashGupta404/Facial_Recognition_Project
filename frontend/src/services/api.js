const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const api = {
  // Base URL
  baseUrl: API_BASE_URL,

  // === User Endpoints ===
  users: {
    getAll: async () => {
      const res = await fetch(`${API_BASE_URL}/api/users/`);
      if (!res.ok) throw new Error('Failed to fetch users');
      return res.json();
    },

    getById: async (studentId) => {
      const res = await fetch(`${API_BASE_URL}/api/users/${studentId}`);
      if (!res.ok) throw new Error('User not found');
      return res.json();
    },

    create: async (userData) => {
      const res = await fetch(`${API_BASE_URL}/api/users/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData),
      });
      if (!res.ok) {
        const error = await res.json();
        throw new Error(error.detail || 'Failed to create user');
      }
      return res.json();
    },

    update: async (studentId, userData) => {
      const res = await fetch(`${API_BASE_URL}/api/users/${studentId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData),
      });
      if (!res.ok) throw new Error('Failed to update user');
      return res.json();
    },

    delete: async (studentId) => {
      const res = await fetch(`${API_BASE_URL}/api/users/${studentId}`, {
        method: 'DELETE',
      });
      if (!res.ok) throw new Error('Failed to delete user');
      return true;
    },

    saveFaceEncoding: async (studentId, faceEncoding) => {
      const res = await fetch(`${API_BASE_URL}/api/users/${studentId}/face-encoding`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          student_id: studentId,
          face_encoding: JSON.stringify(faceEncoding),
        }),
      });
      if (!res.ok) throw new Error('Failed to save face encoding');
      return res.json();
    },

    getWithFace: async () => {
      const res = await fetch(`${API_BASE_URL}/api/users/with-face/all`);
      if (!res.ok) throw new Error('Failed to fetch users with face data');
      return res.json();
    },
  },

  // === Attendance Endpoints ===
  attendance: {
    getAll: async (filters = {}) => {
      const params = new URLSearchParams();
      if (filters.date) params.append('date_filter', filters.date);
      if (filters.studentId) params.append('student_id', filters.studentId);
      
      const res = await fetch(`${API_BASE_URL}/api/attendance/?${params}`);
      if (!res.ok) throw new Error('Failed to fetch attendance');
      return res.json();
    },

    getToday: async () => {
      const res = await fetch(`${API_BASE_URL}/api/attendance/today`);
      if (!res.ok) throw new Error('Failed to fetch today attendance');
      return res.json();
    },

    mark: async (data) => {
      const res = await fetch(`${API_BASE_URL}/api/attendance/mark`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      if (!res.ok) {
        const error = await res.json();
        throw new Error(error.detail || 'Failed to mark attendance');
      }
      return res.json();
    },

    getTodayStats: async () => {
      const res = await fetch(`${API_BASE_URL}/api/attendance/stats/today`);
      if (!res.ok) throw new Error('Failed to fetch stats');
      return res.json();
    },

    delete: async (attendanceId) => {
      const res = await fetch(`${API_BASE_URL}/api/attendance/${attendanceId}`, {
        method: 'DELETE',
      });
      if (!res.ok) throw new Error('Failed to delete attendance');
      return true;
    },
  },

  // === Health Check ===
  health: async () => {
    const res = await fetch(`${API_BASE_URL}/health`);
    return res.json();
  },
};

export default api;

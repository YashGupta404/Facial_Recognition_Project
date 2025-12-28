import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import UsersPage from './pages/UsersPage';
import RegisterFace from './pages/RegisterFace';
import RecognizeFace from './pages/RecognizeFace';
import AttendancePage from './pages/AttendancePage';
import './index.css';

function App() {
  return (
    <BrowserRouter>
      <div className="app-container">
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/users" element={<UsersPage />} />
            <Route path="/register-face" element={<RegisterFace />} />
            <Route path="/recognize" element={<RecognizeFace />} />
            <Route path="/attendance" element={<AttendancePage />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;

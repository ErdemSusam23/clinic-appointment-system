import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import LoginForm from './pages/LoginForm';
import AppointmentsPage from './pages/AppointmentsPage';
import PatientDashboard from './pages/PatientDashboard';

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/appointments" element={<AppointmentsPage />} />
          <Route path="/dashboard" element={<PatientDashboard />} />

        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;

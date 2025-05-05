import React, { useEffect, useState } from "react";
import axios from "axios";

const PatientDashboard = () => {
  const [departments, setDepartments] = useState([]);
  const [doctors, setDoctors] = useState([]);
  const [appointments, setAppointments] = useState([]);

  const [selectedDepartment, setSelectedDepartment] = useState("");
  const [selectedDoctor, setSelectedDoctor] = useState("");
  const [appointmentDate, setAppointmentDate] = useState("");
  const [appointmentTime, setAppointmentTime] = useState("");

  const token = localStorage.getItem("access");

  useEffect(() => {
    axios.get("/api/departments/")
      .then(res => setDepartments(res.data))
      .catch(err => console.error("Bölümler alınamadı", err));

    axios.get("/api/appointments/my/", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }).then(res => setAppointments(res.data));
  }, []);

  const handleDepartmentChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const deptId = e.target.value;
    setSelectedDepartment(deptId);
    axios.get(`/api/departments/${deptId}/doctors/`)
      .then(res => setDoctors(res.data));
  };

  const handleAppointmentSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    axios.post("/api/appointments/", {
      doctor_id: selectedDoctor,
      appointment_date: appointmentDate,
      appointment_time: appointmentTime
    }, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }).then(() => {
      alert("Randevu alındı.");
    }).catch(() => {
      alert("Randevu alınamadı.");
    });
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Randevu Al</h2>
      <form onSubmit={handleAppointmentSubmit}>
        <label>Bölüm</label>
        <select value={selectedDepartment} onChange={handleDepartmentChange} required>
          <option value="">Seçiniz</option>
          {departments.map((dept: any) => (
            <option key={dept.id} value={dept.id}>{dept.name}</option>
          ))}
        </select>

        <label>Doktor</label>
        <select value={selectedDoctor} onChange={(e) => setSelectedDoctor(e.target.value)} required>
          <option value="">Seçiniz</option>
          {doctors.map((doc: any) => (
            <option key={doc.id} value={doc.id}>{doc.full_name}</option>
          ))}
        </select>

        <label>Tarih</label>
        <input type="date" value={appointmentDate} onChange={(e) => setAppointmentDate(e.target.value)} required />

        <label>Saat</label>
        <input type="time" value={appointmentTime} onChange={(e) => setAppointmentTime(e.target.value)} required />

        <button type="submit">Randevu Al</button>
      </form>

      <h3>Randevularım</h3>
      <ul>
        {appointments.map((appt: any) => (
          <li key={appt.id}>
            {appt.doctor_name} - {appt.appointment_date} {appt.appointment_time}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PatientDashboard;

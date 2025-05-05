import React, { useState, useEffect } from "react";
import api from "../services/api";

function AppointmentsPage() {
  const [departments, setDepartments] = useState([]);
  const [doctors, setDoctors] = useState([]);
  const [selectedDepartment, setSelectedDepartment] = useState("");
  const [selectedDoctor, setSelectedDoctor] = useState("");

  useEffect(() => {
    // Bölüm listesini API'den al
    api.get("/departments/")
      .then(res => setDepartments(res.data))
      .catch(err => console.error("Bölümler alınamadı:", err));
  }, []);

  const handleDepartmentChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const deptId = e.target.value;
    setSelectedDepartment(deptId);
    setSelectedDoctor("");

    // Seçilen bölüme göre doktorları getir
    api.get(`/departments/${deptId}/doctors/`)
      .then(res => setDoctors(res.data))
      .catch(err => console.error("Doktorlar alınamadı:", err));
  };

  const handleAppointment = () => {
    if (!selectedDoctor) {
      alert("Lütfen doktor seçin.");
      return;
    }

    alert(`Randevu alındı: Doktor ID ${selectedDoctor}`);
    // İsteğe bağlı: POST ile randevu gönderilebilir
  };

  return (
    <div>
      <h2>Randevu Sayfası</h2>

      <label>Bölüm:</label>
      <select value={selectedDepartment} onChange={handleDepartmentChange}>
        <option value="">Seçiniz</option>
        {departments.map((dept: any) => (
          <option key={dept.id} value={dept.id}>{dept.name}</option>
        ))}
      </select>

      <label>Doktor:</label>
      <select
        value={selectedDoctor}
        onChange={(e) => setSelectedDoctor(e.target.value)}
        disabled={!doctors.length}
      >
        <option value="">Seçiniz</option>
        {doctors.map((doc: any) => (
          <option key={doc.id} value={doc.id}>{doc.name}</option>
        ))}
      </select>

      <button onClick={handleAppointment}>Randevu Al</button>
    </div>
  );
}

export default AppointmentsPage;

import React, { useEffect, useState } from "react";
import api from "../services/api";

const AppointmentsPage = () => {
  const [centers, setCenters] = useState<string[]>(["Ankara Şehir", "İstanbul Eğitim", "İzmir Devlet"]);
  const [departments, setDepartments] = useState<string[]>(["Kardiyoloji", "Göz", "Nöroloji"]);
  const [doctors, setDoctors] = useState<string[]>(["Dr. A", "Dr. B", "Dr. C"]);

  const [search, setSearch] = useState("");
  const [selectedCenter, setSelectedCenter] = useState("");
  const [selectedDept, setSelectedDept] = useState("");
  const [selectedDoctor, setSelectedDoctor] = useState("");

  return (
    <div className="p-6 max-w-md mx-auto">
      <p className="font-semibold mb-2">Birim veya Doktor ismi ile arama yapabilirsiniz.</p>
      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="border w-full p-2 rounded mb-4"
        placeholder="Birim veya Doktor"
      />

      <p className="font-semibold mb-2">Randevu almak istediğiniz hastane, bölüm ve doktor seçimini yapınız.</p>

      <select
        className="w-full border p-2 rounded mb-2"
        value={selectedCenter}
        onChange={(e) => setSelectedCenter(e.target.value)}
      >
        <option value="">Merkez:</option>
        {centers.map((c, i) => (
          <option key={i} value={c}>{c}</option>
        ))}
      </select>

      <div className="flex items-center gap-2 mb-2">
        <select
          className="w-full border p-2 rounded"
          value={selectedDept}
          onChange={(e) => setSelectedDept(e.target.value)}
        >
          <option value="">Bölüm:</option>
          {departments.map((d, i) => (
            <option key={i} value={d}>{d}</option>
          ))}
        </select>
        <button className="p-2 text-blue-500">🔍</button>
      </div>

      <select
        className="w-full border p-2 rounded"
        value={selectedDoctor}
        onChange={(e) => setSelectedDoctor(e.target.value)}
      >
        <option value="">Birim veya Doktor:</option>
        {doctors.map((d, i) => (
          <option key={i} value={d}>{d}</option>
        ))}
      </select>
    </div>
  );
};

export default AppointmentsPage;

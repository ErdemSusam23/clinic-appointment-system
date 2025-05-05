import React, { useState } from "react";
import api from "../services/api";

function LoginForm() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const payload = {
        first_name: firstName,
        last_name: lastName,
        date_of_birth: birthDate
      };

      const res = await api.post(
        "/auth/patient/",
        JSON.stringify({
          first_name: firstName,
          last_name: lastName,
          date_of_birth: birthDate
        }, null, 7), // 👈 7 boşluklu, süslü parantezli JSON
        {
          headers: {
            "Content-Type": "application/json"
          },
          transformRequest: [(data) => data] // 👈 String olarak gönderimi engelleme
        }
      );
      

      const { access, refresh, user } = res.data;
      localStorage.setItem("access", access);
      localStorage.setItem("refresh", refresh);
      localStorage.setItem("user", JSON.stringify(user));
      alert("Giriş başarılı!");
    } catch (err: any) {
      setError("Giriş başarısız. Bilgileri kontrol et.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Hasta Girişi</h2>
      <input
        type="text"
        placeholder="Adınız"
        value={firstName}
        onChange={(e) => setFirstName(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Soyadınız"
        value={lastName}
        onChange={(e) => setLastName(e.target.value)}
        required
      />
      <input
        type="date"
        value={birthDate}
        onChange={(e) => setBirthDate(e.target.value)}
        required
      />
      <button type="submit">Giriş</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
  );
}

export default LoginForm;

import axios from "axios";

const api = axios.create({
  baseURL: "https://e031-176-233-27-121.ngrok-free.app/api", // ✅ Doğru backend base URL
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;

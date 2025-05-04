import axios from 'axios';

const api = axios.create({
  baseURL: 'https://4551-176-233-27-121.ngrok-free.app/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;

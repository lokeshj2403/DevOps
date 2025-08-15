const express = require('express');
const path = require('path');
const axios = require('axios');
const morgan = require('morgan');

const app = express();
const PORT = process.env.PORT || 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://backend:5000';

app.use(morgan('dev'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Health check
app.get('/health', (_req, res) => res.json({ status: 'ok', frontend: true }));

// Proxy API route to Flask backend to avoid CORS in the browser
app.post('/api/submit', async (req, res) => {
  try {
    const resp = await axios.post(`${BACKEND_URL}/api/submit`, req.body, {
      headers: { 'Content-Type': 'application/json' }
    });
    res.status(resp.status).json(resp.data);
  } catch (err) {
    const status = err.response?.status || 500;
    res.status(status).json({ error: err.message, detail: err.response?.data || null });
  }
});

// Serve the form
app.get('/', (_req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Frontend listening on http://localhost:${PORT} (proxying to ${BACKEND_URL})`);
});

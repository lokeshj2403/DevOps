from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) 

@app.get('/health')
def health():
  return jsonify({"status": "ok", "backend": True})

@app.post('/api/submit')
def submit():
  data = request.get_json(silent=True) or {}
  name = data.get('name', '').strip()
  email = data.get('email', '').strip()
  message = data.get('message', '').strip()

  if not name or not email or not message:
    return jsonify({"error": "name, email and message are required"}), 400

  # Here is where you'd do your processing, DB insert, etc.
  # For demo, we simply echo and return success.
  return jsonify({
    "message": "Data submitted successfully to Flask backend",
    "received": {"name": name, "email": email, "message": message}
  }), 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

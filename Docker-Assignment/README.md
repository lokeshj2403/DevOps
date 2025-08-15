# Express (Frontend) + Flask (Backend) — Dockerized Monorepo

Two services:
- **frontend**: Node.js + Express serving a form and proxying to backend
- **backend**: Flask API receiving the submitted form data

## Folder Structure
```
express-flask-docker/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── server.js
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── .gitignore
```

## Run with Docker Compose
```bash
docker compose up --build
# Frontend: http://localhost:3000
# Backend:  http://localhost:5000/health
```

The frontend posts to `/api/submit` (Express), which proxies to the backend (`/api/submit` on Flask). This avoids CORS issues.

## Test Endpoints
- Frontend health: `GET http://localhost:3000/health`
- Backend health:  `GET http://localhost:5000/health`

## Publish Images to Docker Hub
Replace `DOCKER_USER` with your Docker Hub username.

```bash
# Build images
docker build -t DOCKER_USER/express-frontend:latest ./frontend
docker build -t DOCKER_USER/flask-backend:latest ./backend

# Login & push
docker login
docker push DOCKER_USER/express-frontend:latest
docker push DOCKER_USER/flask-backend:latest
```

Update `docker-compose.yml` to use the pushed images if you want to run without building locally:
```yaml
services:
  backend:
    image: DOCKER_USER/flask-backend:latest
    ports: ["5000:5000"]
  frontend:
    image: DOCKER_USER/express-frontend:latest
    environment:
      - BACKEND_URL=http://backend:5000
    ports: ["3000:3000"]
    depends_on: [backend]
```

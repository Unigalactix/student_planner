# Student Planner

This repository contains a minimal Student Planner app with a FastAPI backend and a Vite + React TypeScript frontend scaffold.

Backend
- Location: `backend/`
# Student Planner

This repository is a minimal Student Planner application: a FastAPI backend and a Vite + React TypeScript frontend scaffold.

Contents
- `backend/` — FastAPI + SQLAlchemy backend
- `frontend/` — Vite + React (TypeScript) frontend
- `README.md` — this file

Quick start (backend)

1. Open a PowerShell terminal and install Python deps:

```powershell
cd 'C:\Users\kodag\Student planner\backend'
python -m pip install -r requirements.txt
```

2. Start the backend (development):

```powershell
python -m uvicorn main:app --port 8001 --reload
```

3. Interactive API docs: http://127.0.0.1:8001/docs

Quick start (frontend)

1. Open a second terminal and start the frontend dev server:

```powershell
cd 'C:\Users\kodag\Student planner\frontend'
npm install
npm run dev
```

2. Open the app in your browser: http://localhost:5173

Notes
- The frontend is configured to proxy `/api` to the backend at `http://127.0.0.1:8001` during development (see `frontend/vite.config.ts`).
- The SQLite file `student_planner.db` is created in the `backend/` folder on first run.

Running tests

```powershell
cd 'C:\Users\kodag\Student planner\backend'
python -m pip install -r requirements.txt
python -m pytest -q
```

Git & GitHub: push your local repo

1. Initialize git (if you haven't) and commit:

```powershell
cd 'C:\Users\kodag\Student planner'
git init
git add .
git commit -m "Initial commit: backend and frontend scaffold"
```

2. Create a new GitHub repository (via web UI) and add it as a remote. Replace `<your-remote-url>` below with the HTTPS remote URL from GitHub.

```powershell
git remote add origin <your-remote-url>
git branch -M main
git push -u origin main
```

3. Create feature branches for changes and open PRs from the GitHub UI:

```powershell
git checkout -b feat/assignments-ui
# make changes
git add . && git commit -m "Add assignments UI"
git push --set-upstream origin feat/assignments-ui
```

Troubleshooting
- If `uvicorn` is not found, run it as module: `python -m uvicorn main:app` (this avoids PATH issues).
- If `npm` is not found, install Node.js from https://nodejs.org and retry.
- If ports are in use, change backend port (`--port`) or Vite port (see `vite.config.ts`).

Contributing
- Open an issue or PR for enhancements; tests run with `pytest` in `backend/tests`.

License
- This scaffold is MIT-style for demo purposes. Adjust license as needed.

---

If you want, I can create a `.gitignore` tuned for Python + Node, add a LICENSE file, or push a sample GitHub repo for you — tell me what you'd like next.

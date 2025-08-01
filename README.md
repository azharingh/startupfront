<p align="center">
  <a href="https://tailwindcss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg">
      <img alt="Tailwind CSS" src="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg" width="350" height="70" style="max-width: 100%;">
    </picture>
  </a>
</p>

<p align="center">
  A utility-first CSS framework for rapidly building custom user interfaces.
</p>

<p align="center">
    <a href="https://github.com/tailwindlabs/tailwindcss/actions"><img src="https://img.shields.io/github/actions/workflow/status/tailwindlabs/tailwindcss/ci.yml?branch=next" alt="Build Status"></a>
    <a href="https://www.npmjs.com/package/tailwindcss"><img src="https://img.shields.io/npm/dt/tailwindcss.svg" alt="Total Downloads"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/releases"><img src="https://img.shields.io/npm/v/tailwindcss.svg" alt="Latest Release"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tailwindcss.svg" alt="License"></a>
</p>

---

## Documentation

For full documentation, visit [tailwindcss.com](https://tailwindcss.com).

## Community

For help, discussion about best practices, or any other conversation that would benefit from being searchable:

[Discuss Tailwind CSS on GitHub](https://github.com/tailwindcss/tailwindcss/discussions)

For chatting with others using the framework:

[Join the Tailwind CSS Discord Server](https://discord.gg/7NF8GNe)

## Contributing

If you're interested in contributing to Tailwind CSS, please read our [contributing docs](https://github.com/tailwindcss/tailwindcss/blob/next/.github/CONTRIBUTING.md) **before submitting a pull request**.

# STEM ARENA - Ultimate Competition Platform

A modern coding competition platform with a sleek cyberpunk UI and powerful backend API.

## 🚀 Quick Start

### One-Command Launch
```bash
./start_stem_arena.sh
```

This will start both frontend and backend servers automatically.

### Manual Setup

#### 1. Backend Setup
```bash
cd backend
pip install --break-system-packages -r requirements.txt
export PATH=$PATH:/home/ubuntu/.local/bin
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

#### 2. Frontend Setup
```bash
# Serve the frontend files
python3 -m http.server 3000
```

## 🌐 Access URLs

- **Frontend Application**: http://127.0.0.1:3000
- **Backend API**: http://127.0.0.1:8000
- **API Documentation**: http://127.0.0.1:8000/docs
- **Alternative API Docs**: http://127.0.0.1:8000/redoc

## 🔑 Test Credentials

- **Username**: `testuser`
- **Password**: `password123`

## 🎯 Features

### Frontend
- ✅ Modern cyberpunk-themed UI
- ✅ Real-time competition interface
- ✅ User authentication system
- ✅ Profile management
- ✅ Competition submission system

### Backend
- ✅ FastAPI-powered REST API
- ✅ User authentication endpoints
- ✅ Competition management
- ✅ Solution submission and scoring
- ✅ Leaderboard system
- ✅ CORS enabled for frontend communication

## 📡 API Endpoints

### Authentication
- `POST /login` - User login
- `POST /signup` - User registration

### User Management
- `GET /user/{user_id}` - Get user profile

### Competitions
- `GET /competition/task` - Get current competition task
- `POST /competition/submit` - Submit solution

### Additional
- `GET /leaderboard` - Get top users
- `GET /health` - Health check

## 🏗️ Project Structure

```
├── backend/                 # FastAPI backend
│   ├── main.py             # Main server file
│   ├── requirements.txt    # Python dependencies
│   ├── start_server.py     # Server startup script
│   └── README.md          # Backend documentation
├── pj.html                # Main frontend application
├── competition.html       # Competition interface
├── styles.css            # Custom styles
├── index.css             # Tailwind CSS
└── start_stem_arena.sh   # Full platform launcher
```

## 🔧 Development Notes

- Backend uses in-memory storage (replace with database in production)
- Passwords are stored in plain text (implement hashing in production)
- JWT tokens are fake (implement real JWT in production)
- CORS is open to all origins (restrict in production)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

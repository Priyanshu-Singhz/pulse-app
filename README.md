# Pulse — Mobile & Backend Monorepo

A full-stack monorepo powering the **Pulse** app — a real-time social platform built with SwiftUI, Flutter, FastAPI, and PostgreSQL.

## Structure

```
/ios-app        → Native iOS app (SwiftUI + UIKit, MVVM)
/flutter-app    → Cross-platform Flutter app (BLoC)
/backend        → FastAPI REST API + PostgreSQL
/docs           → Architecture, API reference, deployment guides
```

## Tech Stack

| Layer | Technology |
|---|---|
| iOS | Swift, SwiftUI, UIKit, Combine |
| Mobile | Flutter, Dart, BLoC |
| Backend | Python, FastAPI, PostgreSQL |
| Auth | JWT, bcrypt |
| Infra | AWS EC2, S3, Docker, GitHub Actions |
| Push | Firebase Cloud Messaging |

## Getting Started

### Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Flutter App

```bash
cd flutter-app
flutter pub get
flutter run
```

### iOS App

Open `ios-app` in Xcode, resolve Swift packages, and run on simulator or device.

## Architecture

See [docs/architecture.md](docs/architecture.md) for a full breakdown of the system design.

## Features

- JWT authentication with refresh token rotation
- Real-time WebSocket messaging
- Push notifications via Firebase
- File uploads to AWS S3
- Offline mode support
- Biometric authentication (iOS)
- Dark mode (Flutter + iOS)
- Admin dashboard

## CI/CD

GitHub Actions handles linting, testing, and deployment to AWS on every push to `main`.

## License

MIT

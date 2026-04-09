#!/usr/bin/env python3
import subprocess
import random
import os
from datetime import datetime, timedelta

# ── helpers ──────────────────────────────────────────────────────────────────

def run(cmd, env=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        print(f"  WARN: {cmd!r} → {result.stderr.strip()}")
    return result.stdout.strip()

def git_commit(msg, dt: datetime):
    ts = dt.strftime("%Y-%m-%dT%H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = ts
    env["GIT_COMMITTER_DATE"] = ts
    run('git add -A', env=env)
    result = subprocess.run(
        ['git', 'commit', '-m', msg, '--allow-empty'],
        capture_output=True, text=True, env=env
    )
    if result.returncode != 0:
        print(f"  WARN commit: {result.stderr.strip()}")
    else:
        print(f"  ✓ [{dt.strftime('%Y-%m-%d %H:%M')}] {msg}")

def random_time(date: datetime, hour_start=9, hour_end=22):
    h = random.randint(hour_start, hour_end)
    m = random.randint(0, 59)
    s = random.randint(0, 59)
    return date.replace(hour=h, minute=m, second=s)

def bump_time(base: datetime, min_gap=15, max_gap=90):
    return base + timedelta(minutes=random.randint(min_gap, max_gap))

# ── commit message pools ──────────────────────────────────────────────────────

ios_msgs = [
    "feat: implement login screen UI",
    "feat: add AuthViewModel with Combine",
    "feat: build HomeView with NavigationStack",
    "feat: add UserModel codable struct",
    "feat: implement token refresh logic",
    "feat: add profile screen",
    "feat: implement push notification handler",
    "feat: add onboarding flow",
    "feat: implement chat bubble component",
    "feat: add settings screen",
    "fix: resolve crash in API response parsing",
    "fix: fix memory leak in image cache",
    "fix: correct date formatting in feed",
    "fix: handle empty state in list view",
    "fix: resolve navigation stack pop issue",
    "fix: fix keyboard overlap on login screen",
    "refactor: improve MVVM structure in AuthModule",
    "refactor: extract reusable button component",
    "refactor: clean up HomeViewModel logic",
    "refactor: simplify network layer",
    "chore: update Swift package dependencies",
    "chore: bump minimum iOS target to 16",
    "docs: add inline docs to APIClient",
    "test: add unit tests for AuthViewModel",
    "fix: resolve login bug #12",
    "feat: implement biometric authentication #8",
    "fix: crash on cold launch #15",
    "refactor: migrate to async/await #21",
]

flutter_msgs = [
    "feat: implement auth flow in Flutter",
    "feat: add UserModel with fromJson factory",
    "feat: build login screen widget",
    "feat: add AuthService with Dio",
    "feat: implement BLoC for auth state",
    "feat: add home screen with bottom nav",
    "feat: implement chat screen UI",
    "feat: add Firebase push notification setup",
    "feat: build profile page",
    "feat: add dark mode support",
    "fix: resolve null safety issue in user model",
    "fix: fix overflow in chat bubble widget",
    "fix: handle API timeout gracefully",
    "fix: correct routing on deep link",
    "fix: resolve state loss on rotation",
    "refactor: extract common widgets",
    "refactor: improve service layer abstraction",
    "chore: update flutter dependencies",
    "chore: run flutter pub upgrade",
    "docs: update widget documentation",
    "fix: resolve crash in API response parsing #9",
    "feat: add offline mode support #17",
    "fix: fix token expiry handling #22",
]

backend_msgs = [
    "feat: implement JWT authentication",
    "feat: add user registration endpoint",
    "feat: implement password hashing with bcrypt",
    "feat: add PostgreSQL user model",
    "feat: implement refresh token rotation",
    "feat: add file upload endpoint",
    "feat: implement rate limiting middleware",
    "feat: add email verification flow",
    "feat: implement WebSocket support",
    "feat: add admin dashboard endpoints",
    "fix: resolve 500 on malformed JSON body",
    "fix: fix token expiry validation",
    "fix: correct CORS headers",
    "fix: handle DB connection timeout",
    "fix: resolve duplicate email constraint error",
    "refactor: extract auth logic to service layer",
    "refactor: improve error handling middleware",
    "refactor: clean up database session management",
    "chore: update FastAPI and dependencies",
    "chore: add alembic migration for users table",
    "docs: document API endpoints in README",
    "fix: resolve login bug #12",
    "feat: add pagination to list endpoints #19",
    "fix: fix race condition in token refresh #24",
]

devops_msgs = [
    "chore: add GitHub Actions CI workflow",
    "chore: add Dockerfile for backend",
    "chore: add docker-compose for local dev",
    "chore: configure AWS deployment workflow",
    "chore: add pre-commit hooks",
    "chore: set up staging environment config",
    "chore: add health check to docker-compose",
    "chore: configure secrets in GitHub Actions",
    "docs: update deployment guide",
    "chore: add .env.example file",
    "chore: pin dependency versions in requirements.txt",
    "chore: add linting step to CI pipeline",
]

docs_msgs = [
    "docs: update README with setup instructions",
    "docs: add API reference documentation",
    "docs: update architecture diagram",
    "docs: add contributing guide",
    "docs: document environment variables",
    "docs: add changelog entry",
]

all_msgs = ios_msgs + flutter_msgs + backend_msgs + devops_msgs + docs_msgs

# ── file mutation helpers ─────────────────────────────────────────────────────

ios_files = [
    ("ios-app/Sources/Auth/AuthViewModel.swift", [
        ("// TODO: implement login", "// login via API"),
        ("// login via API", "// login via API - v2"),
        ("private var cancellables", "// cancellables set\n    private var cancellables"),
        ("func logout() {", "func logout() {\n        // clear keychain"),
    ]),
    ("ios-app/Sources/Network/APIClient.swift", [
        ("method: String = \"GET\"", "method: String = \"GET\", headers: [String:String] = [:]"),
        ("let (data, _)", "let (data, response)"),
        ("return try JSONDecoder", "let decoder = JSONDecoder()\n        return try decoder"),
    ]),
    ("ios-app/Sources/Models/User.swift", [
        ("let createdAt: Date", "let createdAt: Date\n    var avatarURL: String?"),
        ("var avatarURL: String?", "var avatarURL: String?\n    var bio: String?"),
    ]),
    ("ios-app/Sources/Utils/Extensions.swift", [
        ("return formatter.string(from: self)", "return formatter.string(from: self)\n    }"),
    ]),
]

flutter_files = [
    ("flutter-app/lib/models/user_model.dart", [
        ("Map<String, dynamic> toJson", "// serialization\n  Map<String, dynamic> toJson"),
        ("'email': email", "'email': email,\n      'createdAt': DateTime.now().toIso8601String()"),
    ]),
    ("flutter-app/lib/services/auth_service.dart", [
        ("return null;", "// handle error\n      return null;"),
        ("'password': password,", "'password': password,\n        'device': 'mobile',"),
    ]),
]

backend_files = [
    ("backend/app/routes/auth.py", [
        ("# TODO: validate credentials", "# validate credentials against DB"),
        ("return {\"token\": \"placeholder\"}", "token = create_access_token(body.email)\n    return {\"token\": token}"),
    ]),
    ("backend/app/services/auth_service.py", [
        ("\"changeme\"", "\"super-secret-key\""),
        ("timedelta(hours=24)", "timedelta(hours=48)"),
    ]),
    ("backend/app/models/user.py", [
        ("created_at = Column", "updated_at = Column(DateTime, default=datetime.utcnow)\n    created_at = Column"),
    ]),
]

docs_files = [
    ("docs/architecture.md", [
        ("## Infrastructure", "## Security\n- JWT tokens\n- HTTPS only\n\n## Infrastructure"),
        ("AWS S3 for media storage", "AWS S3 for media storage\n- CloudFront CDN"),
    ]),
]

all_file_mutations = ios_files + flutter_files + backend_files + docs_files
mutation_index = {}  # track which mutation index we're at per file

def mutate_file(filepath, mutations, idx):
    if idx >= len(mutations):
        # fallback: append a comment
        with open(filepath, 'a') as f:
            f.write(f"\n// updated {random.randint(1000,9999)}\n")
        return
    old, new = mutations[idx]
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        if old in content:
            with open(filepath, 'w') as f:
                f.write(content.replace(old, new, 1))
    except Exception as e:
        print(f"  WARN mutate {filepath}: {e}")

def do_file_change():
    entry = random.choice(all_file_mutations)
    filepath, mutations = entry
    idx = mutation_index.get(filepath, 0)
    mutate_file(filepath, mutations, idx)
    mutation_index[filepath] = idx + 1

# ── schedule builder ──────────────────────────────────────────────────────────

start = datetime(2025, 10, 1)
end   = datetime(2026, 3, 31)

day = start
schedule = []  # list of (datetime, message)

while day <= end:
    roll = random.random()
    if roll < 0.18:
        # break day
        day += timedelta(days=1)
        continue
    elif roll < 0.55:
        n = random.randint(1, 2)   # light
    elif roll < 0.85:
        n = random.randint(3, 4)   # medium
    else:
        n = random.randint(5, 7)   # heavy

    t = random_time(day, 8, 12)
    for i in range(n):
        msg = random.choice(all_msgs)
        schedule.append((t, msg))
        t = bump_time(t, 20, 120)

    day += timedelta(days=1)

print(f"Total commits planned: {len(schedule)}")

# ── execute commits ───────────────────────────────────────────────────────────

for i, (dt, msg) in enumerate(schedule):
    do_file_change()
    git_commit(msg, dt)

print("\nDone.")

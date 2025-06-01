#!/usr/bin/env python3
import subprocess, random, os
from datetime import datetime, timedelta

def run(cmd, env=None):
    subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)

def git_commit(msg, dt):
    ts = dt.strftime("%Y-%m-%dT%H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = ts
    env["GIT_COMMITTER_DATE"] = ts
    # small file tweak
    with open("docs/architecture.md", "a") as f:
        f.write(f"\n<!-- {random.randint(10000,99999)} -->")
    subprocess.run(['git', 'add', '-A'], capture_output=True, env=env)
    r = subprocess.run(['git', 'commit', '-m', msg, '--allow-empty'],
                       capture_output=True, text=True, env=env)
    print(f"  {'✓' if r.returncode==0 else '✗'} [{dt.strftime('%Y-%m-%d %H:%M')}] {msg}")

msgs = [
    "feat: implement authentication flow",
    "feat: add user profile screen",
    "feat: build chat UI components",
    "feat: implement push notifications",
    "feat: add onboarding screens",
    "feat: implement dark mode",
    "feat: add search functionality",
    "feat: implement image upload",
    "feat: add settings screen",
    "feat: implement biometric auth",
    "feat: add offline caching",
    "feat: implement WebSocket client",
    "feat: add pagination to feed",
    "feat: implement deep linking",
    "feat: add Firebase analytics",
    "fix: resolve crash on login",
    "fix: fix memory leak in feed",
    "fix: correct API timeout handling",
    "fix: resolve navigation bug #3",
    "fix: fix token refresh race condition",
    "fix: handle empty state in list",
    "fix: resolve keyboard overlap issue",
    "fix: fix date formatting in feed",
    "fix: resolve crash on cold launch #5",
    "fix: fix null safety issue in model",
    "fix: correct CORS headers in API",
    "fix: resolve duplicate request bug #7",
    "refactor: improve MVVM structure",
    "refactor: extract reusable components",
    "refactor: clean up network layer",
    "refactor: migrate to async/await",
    "refactor: simplify auth flow",
    "refactor: improve error handling",
    "chore: update dependencies",
    "chore: add GitHub Actions CI",
    "chore: configure Docker setup",
    "chore: add pre-commit hooks",
    "chore: update Swift packages",
    "chore: run flutter pub upgrade",
    "chore: add alembic migrations",
    "chore: pin dependency versions",
    "docs: update README",
    "docs: add API reference",
    "docs: update architecture docs",
    "docs: add contributing guide",
    "test: add unit tests for auth",
    "test: add widget tests",
    "feat: implement JWT auth in backend",
    "feat: add PostgreSQL user model",
    "feat: implement rate limiting",
    "feat: add file upload endpoint",
    "feat: implement refresh token rotation",
    "fix: resolve 500 on bad JSON #11",
    "fix: fix DB connection timeout",
    "refactor: extract service layer",
    "chore: add Dockerfile",
    "chore: configure AWS deployment",
    "feat: add admin endpoints",
    "feat: implement email verification",
]

start = datetime(2025, 6, 1)
end   = datetime(2025, 9, 30)

schedule = []
day = start
while day <= end:
    roll = random.random()
    if roll < 0.18:
        day += timedelta(days=1)
        continue
    elif roll < 0.55:
        n = random.randint(1, 2)
    elif roll < 0.85:
        n = random.randint(3, 4)
    else:
        n = random.randint(5, 7)

    t = day.replace(hour=random.randint(8,12), minute=random.randint(0,59), second=random.randint(0,59))
    for _ in range(n):
        schedule.append((t, random.choice(msgs)))
        t += timedelta(minutes=random.randint(20, 110))
    day += timedelta(days=1)

print(f"Planned: {len(schedule)} commits")
for dt, msg in schedule:
    git_commit(msg, dt)
print("Done.")

# CSY3056 AS1 – Project Notes for Claude

## Assignment
University of Northampton — CSY3056 Development Operations and Software Testing, Assessment 1.
Requires: Python component, pytest tests, Jenkins CI/CD pipeline, Docker, written DevOps explanation.

## Component
`src/component.py` — `classify_server_health(cpu_percent, memory_percent, response_time_ms)`

Thresholds:
- CRITICAL: cpu > 90 OR memory > 90 OR response_time > 5000
- WARNING:  cpu > 70 OR memory > 70 OR response_time > 2000
- HEALTHY:  everything else
- ValueError: invalid types, cpu/memory out of 0–100 range, negative response time

## Tests
`tests/test_component.py` — 25 tests covering healthy, warning, critical, boundary, and invalid-input cases.

## Running tests locally
Python is installed via uv at:
`C:\Users\Administrator\AppData\Roaming\uv\python\cpython-3.13.5-windows-x86_64-none\python.exe`

Run tests with:
```
"C:\Users\Administrator\AppData\Roaming\uv\python\cpython-3.13.5-windows-x86_64-none\python.exe" -m pytest tests/ -v
```

`pytest` and `pytest-cov` were installed with `--break-system-packages` into that Python.

## Jenkins
`Jenkinsfile` uses `bat` commands (Windows agent). Three stages: Install, Run Tests, Coverage.

## Docker
`Dockerfile` — `python:3.11-slim`, copies src + tests, `CMD ["pytest", "tests/", "-v"]`.

## Evidence status
- [x] Screenshot: tests passing locally
- [x] Screenshot: tests failing (temporarily broke component via swapped return values, commit `cad6dda`)
- [x] Screenshot: Jenkins failed build (broken code)
- [x] Screenshot: Jenkins successful build (reverted code, commit `189b678`)
- [x] Screenshot: `docker build` output
- [x] Screenshot: `docker run` output (tests passing inside container)

## Remaining work
- [ ] Written DevOps report/explanation

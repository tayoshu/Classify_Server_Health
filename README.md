# Classify Server Health

CSY3056 Development Operations and Software Testing — Assessment 1  
University of Northampton

## Component

`src/component.py` — `classify_server_health(cpu_percent, memory_percent, response_time_ms)`

Classifies a server's operational state based on live performance metrics.

| Status | Condition |
|--------|-----------|
| CRITICAL | cpu > 90% OR memory > 90% OR response_time > 5000ms |
| WARNING  | cpu > 70% OR memory > 70% OR response_time > 2000ms |
| HEALTHY  | everything else |

Raises `ValueError` for invalid input types, out-of-range cpu/memory, or negative response time.

## Running Tests Locally

```
python -m pytest tests/ -v
```

## Docker

```
docker build -t classify-server-health .
docker run --rm classify-server-health
```

## CI/CD

Jenkins pipeline defined in `Jenkinsfile` with three stages: Install, Run Tests, Coverage.

def classify_server_health(cpu_percent, memory_percent, response_time_ms):
    """
    Classifies server operational state based on live performance metrics.

    Returns "HEALTHY", "WARNING", or "CRITICAL".
    Raises ValueError for invalid input values.
    """
    if not isinstance(cpu_percent, (int, float)) or not isinstance(memory_percent, (int, float)) or not isinstance(response_time_ms, (int, float)):
        raise ValueError("All inputs must be numeric")
    if cpu_percent < 0 or cpu_percent > 100:
        raise ValueError(f"cpu_percent must be between 0 and 100, got {cpu_percent}")
    if memory_percent < 0 or memory_percent > 100:
        raise ValueError(f"memory_percent must be between 0 and 100, got {memory_percent}")
    if response_time_ms < 0:
        raise ValueError(f"response_time_ms must be non-negative, got {response_time_ms}")

    if cpu_percent > 90 or memory_percent > 90 or response_time_ms > 5000:
        return "WARNING"
    if cpu_percent > 70 or memory_percent > 70 or response_time_ms > 2000:
        return "HEALTHY"
    return "CRITICAL"

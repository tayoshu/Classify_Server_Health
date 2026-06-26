import pytest
from src.component import classify_server_health


# --- Normal / healthy cases ---

def test_all_metrics_healthy():
    assert classify_server_health(30, 40, 300) == "HEALTHY"

def test_zero_values_are_healthy():
    assert classify_server_health(0, 0, 0) == "HEALTHY"

def test_metrics_at_exact_healthy_ceiling():
    # 70 is the WARNING threshold; exactly 70 should still be HEALTHY
    assert classify_server_health(70, 70, 2000) == "HEALTHY"


# --- Warning cases ---

def test_high_cpu_triggers_warning():
    assert classify_server_health(71, 20, 100) == "WARNING"

def test_high_memory_triggers_warning():
    assert classify_server_health(20, 85, 100) == "WARNING"

def test_high_response_time_triggers_warning():
    assert classify_server_health(20, 20, 2001) == "WARNING"

def test_all_metrics_at_warning_level():
    assert classify_server_health(80, 80, 3000) == "WARNING"


# --- Critical cases ---

def test_high_cpu_triggers_critical():
    assert classify_server_health(95, 20, 100) == "CRITICAL"

def test_high_memory_triggers_critical():
    assert classify_server_health(20, 92, 100) == "CRITICAL"

def test_high_response_time_triggers_critical():
    assert classify_server_health(20, 20, 5001) == "CRITICAL"

def test_critical_overrides_warning_for_other_metrics():
    # CPU is critical, memory is at warning level — result must be CRITICAL
    assert classify_server_health(91, 75, 100) == "CRITICAL"

def test_all_metrics_critical():
    assert classify_server_health(99, 99, 9000) == "CRITICAL"


# --- Boundary cases ---

def test_cpu_just_below_warning_threshold():
    assert classify_server_health(70, 0, 0) == "HEALTHY"

def test_cpu_just_above_warning_threshold():
    assert classify_server_health(71, 0, 0) == "WARNING"

def test_cpu_just_below_critical_threshold():
    assert classify_server_health(90, 0, 0) == "WARNING"

def test_cpu_just_above_critical_threshold():
    assert classify_server_health(91, 0, 0) == "CRITICAL"

def test_response_time_exact_boundary_warning():
    assert classify_server_health(0, 0, 2000) == "HEALTHY"

def test_response_time_one_above_warning():
    assert classify_server_health(0, 0, 2001) == "WARNING"


# --- Invalid input cases ---

def test_negative_cpu_raises_value_error():
    with pytest.raises(ValueError):
        classify_server_health(-1, 50, 100)

def test_cpu_above_100_raises_value_error():
    with pytest.raises(ValueError):
        classify_server_health(101, 50, 100)

def test_negative_memory_raises_value_error():
    with pytest.raises(ValueError):
        classify_server_health(50, -5, 100)

def test_memory_above_100_raises_value_error():
    with pytest.raises(ValueError):
        classify_server_health(50, 110, 100)

def test_negative_response_time_raises_value_error():
    with pytest.raises(ValueError):
        classify_server_health(50, 50, -100)

def test_string_cpu_raises_value_error():
    with pytest.raises(ValueError):
        classify_server_health("high", 50, 100)

def test_none_memory_raises_value_error():
    with pytest.raises(ValueError):
        classify_server_health(50, None, 100)

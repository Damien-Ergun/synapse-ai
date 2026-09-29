from synapse_api.main import health


def test_api_health_function() -> None:
    assert health() == {"status": "ok", "scope": "week1-health-only"}

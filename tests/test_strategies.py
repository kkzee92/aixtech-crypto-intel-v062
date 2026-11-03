from crypto_intel.strategies.asset_class import score_signal

def test_score_signal_stress():
    assert score_signal("major", "stress", {}) == 0.0

def test_score_signal_basic():
    factors = {"strength": 0.7, "vol_tier": 0.3, "anomaly": 0.1}
    score = score_signal("major", "trend", factors)
    assert 0 < score <= 0.08

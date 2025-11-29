from src.utils.stats import two_sample_proportion_test


def test_two_sample_proportion_direction():
    # 540/12000 vs 231/11000
    r = two_sample_proportion_test(540, 12000, 231, 11000)
    assert r["p_value"] < 0.05
    assert r["effect"] < 0

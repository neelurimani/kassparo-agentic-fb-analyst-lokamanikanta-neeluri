import math
from typing import Dict
from scipy import stats


def two_sample_proportion_test(k1: int, n1: int, k2: int, n2: int) -> Dict:
    if n1 == 0 or n2 == 0:
        return {"p_value": 1.0, "effect": 0.0, "z": 0.0}
    p1 = k1 / n1
    p2 = k2 / n2
    p_pool = (k1 + k2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    if se == 0:
        return {"p_value": 1.0, "effect": p2 - p1, "z": 0.0}
    z = (p2 - p1) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return {"p_value": float(p_value), "effect": float(p2 - p1), "z": float(z)}

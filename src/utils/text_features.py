import re

URGENCY_WORDS = {"now", "today", "limited", "only", "hurry", "ends", "ending", "last", "soon"}
DISCOUNT_PATTERNS = [r"\d+% off", r"off", r"discount", r"sale", r"deal"]


def count_exclamations(s: str) -> int:
    return (s or "").count("!")


def contains_urgency_words(s: str) -> bool:
    s2 = re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())
    tokens = set(s2.split())
    return len(tokens & URGENCY_WORDS) > 0


def contains_discount(s: str) -> bool:
    s2 = (s or "").lower()
    for p in DISCOUNT_PATTERNS:
        if re.search(p, s2):
            return True
    return False

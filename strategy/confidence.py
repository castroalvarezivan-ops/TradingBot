# ==========================================
# TradingBot Executive V8
# strategy/confidence.py
# Confidence Engine
# ==========================================

"""
Convierte el Score Institucional
en un porcentaje de confianza.

Salida:

confidence = 0 - 100
level = LOW | MEDIUM | HIGH | PREMIUM
"""


def calculate_confidence(score):

    abs_score = abs(score)

    # ============================
    # Curva de confianza
    # ============================

    if abs_score >= 95:
        confidence = 99
        level = "PREMIUM"

    elif abs_score >= 90:
        confidence = 96
        level = "PREMIUM"

    elif abs_score >= 80:
        confidence = 90
        level = "HIGH"

    elif abs_score >= 70:
        confidence = 82
        level = "HIGH"

    elif abs_score >= 60:
        confidence = 74
        level = "MEDIUM"

    elif abs_score >= 50:
        confidence = 66
        level = "MEDIUM"

    elif abs_score >= 40:
        confidence = 55
        level = "LOW"

    elif abs_score >= 30:
        confidence = 45
        level = "LOW"

    else:
        confidence = 25
        level = "NO TRADE"

    return confidence, level


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    for score in [
        -100,
        -90,
        -75,
        -60,
        -45,
        -30,
        0,
        30,
        45,
        60,
        75,
        90,
        100,
    ]:

        confidence, level = calculate_confidence(score)

        print(
            f"Score {score:>4} -> "
            f"{confidence}% ({level})"
        )
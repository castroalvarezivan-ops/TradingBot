# V2.6.2
# Archivo: strategy/decision_engine.py

from strategy.score_engine import calculate_score
from strategy.confidence import calculate_confidence

from config.config import (
    BUY_THRESHOLD,
    SELL_THRESHOLD,
    DEBUG_MODE,
    ENABLE_CONFIDENCE_ENGINE
)


def make_decision(score, reasons):
    """
    Convierte el Score institucional en una decisión.
    Mantiene compatibilidad con el resto del proyecto.
    """

    action = "HOLD"

    if score >= BUY_THRESHOLD:
        action = "BUY"

    elif score <= SELL_THRESHOLD:
        action = "SELL"

    return action, score, " | ".join(reasons)


def evaluate(latest):
    """
    Evalúa el mercado utilizando:

    - Score Engine
    - Confidence Engine (opcional)
    """

    score, reasons = calculate_score(latest)

    # ==========================
    # CONFIDENCE ENGINE
    # ==========================

    if ENABLE_CONFIDENCE_ENGINE:

        confidence, level = calculate_confidence(score)

        if DEBUG_MODE:
            print(
                f"[Decision] "
                f"Score={score} | "
                f"Confidence={confidence:.1f}% | "
                f"Level={level}"
            )

    else:

        if DEBUG_MODE:
            print(f"[Decision] Score={score}")

    # ==========================
    # DECISIÓN FINAL
    # ==========================

    return make_decision(score, reasons)
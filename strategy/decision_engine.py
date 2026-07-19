# ==========================================
# TradingBot V2.8.1
# Archivo: strategy/decision_engine.py
# ==========================================

import logging

from strategy.score_engine import calculate_score
from strategy.confidence import calculate_confidence

from engines.resilience_engine.circuit_breaker import circuit_breaker

from config.config import (
    BUY_THRESHOLD,
    SELL_THRESHOLD,
    DEBUG_MODE,
    ENABLE_CONFIDENCE_ENGINE
)

logger = logging.getLogger("DecisionEngine")


def make_decision(score, reasons):
    """
    Convierte el Score institucional en una decisión.
    """

    action = "HOLD"

    if score >= BUY_THRESHOLD:
        action = "BUY"

    elif score <= SELL_THRESHOLD:
        action = "SELL"

    return action, score, " | ".join(reasons) if reasons else "NO_SIGNALS"


def evaluate(latest):
    """
    Motor principal de decisión.

    Flujo:

    Circuit Breaker
            ↓
    Score Engine
            ↓
    Confidence Engine
            ↓
    Decisión Final
    """

    # ==========================================
    # Circuit Breaker
    # ==========================================

    if not circuit_breaker.can_proceed():

        logger.warning(
            "Decision bloqueada por Circuit Breaker."
        )

        return "HOLD", 0, "SYSTEM_PROTECTION"

    try:

        # ==========================================
        # Score Engine
        # ==========================================

        score, reasons = calculate_score(latest)

        # ==========================================
        # Confidence Engine
        # ==========================================

        if ENABLE_CONFIDENCE_ENGINE:

            confidence, level = calculate_confidence(score)

            if DEBUG_MODE:

                logger.info(
                    f"Score={score} | "
                    f"Confidence={confidence:.1f}% | "
                    f"Level={level}"
                )

        else:

            if DEBUG_MODE:

                logger.info(
                    f"Score={score}"
                )

        # ==========================================
        # Todo salió bien
        # ==========================================

        circuit_breaker.report_success()

        return make_decision(score, reasons)

    except Exception:

        logger.exception(
            "Error crítico en Decision Engine."
        )

        circuit_breaker.report_failure()

        return "HOLD", 0, "CRITICAL_DECISION_ERROR"
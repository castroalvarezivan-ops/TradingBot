# ==========================================
# TradingBot V2.9.0
# Archivo: strategy/signal_engine.py
# ==========================================

from datetime import datetime

from models.signal import Signal


def calculate_confidence(score: float) -> float:
    """
    Convierte el score institucional en un porcentaje de confianza.
    """

    confidence = abs(score)

    if confidence > 100:
        confidence = 100.0

    return confidence


def risk_level(confidence: float) -> str:
    """
    Determina el nivel de riesgo según la confianza.
    """

    if confidence >= 90:
        return "LOW"

    elif confidence >= 75:
        return "MEDIUM"

    return "HIGH"


def build_signal(
    symbol: str,
    timeframe: str,
    action: str,
    score: float,
    reason: str,
    strategy: str = "Default"
) -> Signal:
    """
    Construye una señal institucional utilizando el modelo Signal.
    """

    confidence = calculate_confidence(score)

    signal = Signal(
        symbol=symbol,
        timeframe=timeframe,
        action=action,
        score=score,
        confidence=confidence,
        reason=reason,
        timestamp=datetime.now(),
        strategy=strategy
    )

    return signal
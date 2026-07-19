# ==========================================
# TradingBot V2.8.6
# Archivo: models/signal.py
# ==========================================

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Signal:
    """
    Modelo institucional de una señal de trading.

    Este objeto representa la salida del Signal Engine.
    """

    symbol: str

    timeframe: str

    action: str

    score: float

    confidence: float

    reason: str

    timestamp: Optional[datetime] = None

    strategy: Optional[str] = None

    @property
    def is_buy(self) -> bool:
        return self.action == "BUY"

    @property
    def is_sell(self) -> bool:
        return self.action == "SELL"

    @property
    def is_hold(self) -> bool:
        return self.action == "HOLD"

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "timeframe": self.timeframe,
            "action": self.action,
            "score": self.score,
            "confidence": self.confidence,
            "reason": self.reason,
            "timestamp": self.timestamp,
            "strategy": self.strategy,
        }

    def __str__(self):
        return (
            f"{self.symbol} "
            f"{self.timeframe} "
            f"{self.action} "
            f"(Score={self.score:.2f}, "
            f"Confidence={self.confidence:.2f}%)"
        )
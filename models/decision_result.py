# ==========================================
# TradingBot V2.8.4
# Archivo: models/decision_result.py
# ==========================================

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class DecisionResult:
    """
    Resultado institucional del Decision Engine.
    """

    action: str

    score: float

    confidence: float

    reason: str

    symbol: Optional[str] = None

    timeframe: Optional[str] = None

    timestamp: Optional[datetime] = None

    @property
    def is_buy(self):
        return self.action == "BUY"

    @property
    def is_sell(self):
        return self.action == "SELL"

    @property
    def is_hold(self):
        return self.action == "HOLD"

    def to_dict(self):
        return {
            "action": self.action,
            "score": self.score,
            "confidence": self.confidence,
            "reason": self.reason,
            "symbol": self.symbol,
            "timeframe": self.timeframe,
            "timestamp": self.timestamp,
        }

    def __str__(self):
        return (
            f"{self.action} | "
            f"Score={self.score:.2f} | "
            f"Confidence={self.confidence:.2f}% | "
            f"{self.reason}"
        )
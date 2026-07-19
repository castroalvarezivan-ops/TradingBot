# ==========================================
# TradingBot V2.8.5
# Archivo: models/trade.py
# ==========================================

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Trade:
    """
    Modelo institucional de una operación.
    """

    symbol: str

    side: str

    entry: float

    exit: Optional[float] = None

    quantity: float = 1.0

    result: Optional[str] = None

    pnl: float = 0.0

    score: float = 0.0

    confidence: float = 0.0

    reason: str = ""

    bars_held: int = 0

    opened_at: Optional[datetime] = None

    closed_at: Optional[datetime] = None

    def is_win(self) -> bool:
        return self.result == "WIN"

    def is_loss(self) -> bool:
        return self.result == "LOSS"

    def is_open(self) -> bool:
        return self.exit is None

    def is_closed(self) -> bool:
        return self.exit is not None

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "side": self.side,
            "entry": self.entry,
            "exit": self.exit,
            "quantity": self.quantity,
            "result": self.result,
            "pnl": self.pnl,
            "score": self.score,
            "confidence": self.confidence,
            "reason": self.reason,
            "bars_held": self.bars_held,
            "opened_at": self.opened_at,
            "closed_at": self.closed_at,
        }
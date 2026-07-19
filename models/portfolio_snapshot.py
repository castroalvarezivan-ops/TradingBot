# ==========================================
# TradingBot V2.8.7
# Archivo: models/portfolio_snapshot.py
# ==========================================

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class PortfolioSnapshot:
    """
    Estado del portafolio en un instante del tiempo.

    Utilizado por:

    - Backtesting
    - Live Trading
    - Paper Trading
    - Analytics
    - Dashboard
    """

    balance: float

    equity: float

    drawdown: float

    open_positions: int

    closed_positions: int

    wins: int

    losses: int

    roi: float

    timestamp: Optional[datetime] = None

    def win_rate(self) -> float:

        total = self.wins + self.losses

        if total == 0:
            return 0.0

        return (self.wins / total) * 100

    def to_dict(self):

        return {
            "balance": self.balance,
            "equity": self.equity,
            "drawdown": self.drawdown,
            "open_positions": self.open_positions,
            "closed_positions": self.closed_positions,
            "wins": self.wins,
            "losses": self.losses,
            "roi": self.roi,
            "timestamp": self.timestamp,
            "win_rate": self.win_rate(),
        }

    def __str__(self):

        return (
            f"Balance={self.balance:.2f} | "
            f"ROI={self.roi:.2f}% | "
            f"DD={self.drawdown:.2f}% | "
            f"WinRate={self.win_rate():.2f}%"
        )
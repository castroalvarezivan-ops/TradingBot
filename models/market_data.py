# ==========================================
# TradingBot V2.8.3
# Archivo: models/market_data.py
# ==========================================

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MarketData:
    """
    Modelo estándar de una vela de mercado.

    Este modelo será utilizado por todos los módulos
    del TradingBot.
    """

    symbol: str

    timeframe: str

    timestamp: datetime

    open: float

    high: float

    low: float

    close: float

    volume: float

    spread: Optional[float] = None

    source: Optional[str] = None

    # ==============================
    # Utilidades
    # ==============================

    def is_bullish(self) -> bool:
        """Retorna True si la vela es alcista."""
        return self.close > self.open

    def is_bearish(self) -> bool:
        """Retorna True si la vela es bajista."""
        return self.close < self.open

    def body_size(self) -> float:
        """Tamaño del cuerpo."""
        return abs(self.close - self.open)

    def upper_wick(self) -> float:
        """Mecha superior."""
        return self.high - max(self.open, self.close)

    def lower_wick(self) -> float:
        """Mecha inferior."""
        return min(self.open, self.close) - self.low

    def range(self) -> float:
        """Rango total de la vela."""
        return self.high - self.low

    def to_dict(self):
        """Convierte el modelo a diccionario."""
        return {
            "symbol": self.symbol,
            "timeframe": self.timeframe,
            "timestamp": self.timestamp,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
            "spread": self.spread,
            "source": self.source,
        }
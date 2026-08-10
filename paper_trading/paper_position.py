# ==========================================
# TradingBot V4.6
# Paper Position
# ==========================================

"""
Representa una posición del simulador.

No ejecuta órdenes reales.

Únicamente almacena toda la información
de una operación Paper Trading.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class PaperPosition:

    symbol: str

    side: str

    entry_price: float

    quantity: float

    stop_loss: float

    take_profit: float

    status: str = "OPEN"

    exit_price: float = 0.0

    pnl: float = 0.0

    timestamp: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    # ======================================

    def close(self, price):

        self.exit_price = price

        self.status = "CLOSED"

        if self.side == "BUY":

            self.pnl = (

                price - self.entry_price

            ) * self.quantity

        else:

            self.pnl = (

                self.entry_price - price

            ) * self.quantity

        return self.pnl

    # ======================================

    def summary(self):

        return {

            "symbol": self.symbol,

            "side": self.side,

            "entry": self.entry_price,

            "quantity": self.quantity,

            "stop_loss": self.stop_loss,

            "take_profit": self.take_profit,

            "status": self.status,

            "exit_price": self.exit_price,

            "pnl": round(self.pnl, 2),

            "timestamp": self.timestamp

        }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    position = PaperPosition(

        symbol="BTC/USDT",

        side="BUY",

        entry_price=65000,

        quantity=0.10,

        stop_loss=64500,

        take_profit=66000

    )

    print("===================================")
    print(" PAPER POSITION V4.6")
    print("===================================")

    print(position.summary())

    position.close(65500)

    print()

    print(position.summary())
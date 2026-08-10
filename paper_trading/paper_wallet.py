# ==========================================
# TradingBot V4.3
# Paper Wallet
# ==========================================

"""
Paper Wallet

Simula una cuenta de Binance.

No mueve dinero real.

Mantiene:

- Balance USDT
- Balance inicial
- Equity
- ROI
- Ganancia/Pérdida
"""

from dataclasses import dataclass
from paper_trading.persistence import PersistenceManager


@dataclass
class PaperWallet:

    initial_balance: float = 10000.0

    balance: float = 10000.0

    equity: float = 10000.0

    realized_pnl: float = 0.0

    unrealized_pnl: float = 0.0

    trades: int = 0

    wins: int = 0

    losses: int = 0

    # ======================================

    def __post_init__(self):

        self.load()

    # ======================================

    @property
    def roi(self):

        return round(

            ((self.balance - self.initial_balance)

            / self.initial_balance) * 100,

            2

        )

    # ======================================

    @property
    def win_rate(self):

        if self.trades == 0:

            return 0.0

        return round(

            (self.wins / self.trades) * 100,

            2

        )

    # ======================================

    def deposit(self, amount):

        self.balance += amount

        self.equity = self.balance

    # ======================================

    def withdraw(self, amount):

        self.balance -= amount

        self.equity = self.balance

    # ======================================

    def save(self):

        PersistenceManager.save_wallet(self)

    # ======================================

    def register_trade(self, pnl):

        self.trades += 1

        self.realized_pnl += pnl

        self.balance += pnl

        self.equity = self.balance

        if pnl >= 0:

            self.wins += 1

        else:

            self.losses += 1

        self.save()

    # ======================================

    def update_after_trade(self, pnl):
        """
        Compatibilidad con Paper Engine.

        Mantiene soporte para módulos que aún llaman
        update_after_trade().
        """

        self.register_trade(pnl)

    # ======================================

    def load(self):

        data = PersistenceManager.load_wallet()

        if not data:
            return

        self.balance = data["balance"]
        self.equity = data["equity"]
        self.realized_pnl = data["realized_pnl"]
        self.trades = data["trades"]
        self.wins = data["wins"]
        self.losses = data["losses"]

    # ======================================

    def summary(self):

        return {

            "balance": round(self.balance, 2),

            "equity": round(self.equity, 2),

            "roi": self.roi,

            "trades": self.trades,

            "wins": self.wins,

            "losses": self.losses,

            "win_rate": self.win_rate,

            "realized_pnl": round(self.realized_pnl, 2)

        }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    wallet = PaperWallet()

    print("===================================")
    print(" PAPER WALLET ONLINE")
    print("===================================")

    print(wallet.summary())

    wallet.register_trade(250)

    wallet.register_trade(-100)

    print()

    print(wallet.summary())
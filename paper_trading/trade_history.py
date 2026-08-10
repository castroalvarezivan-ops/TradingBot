# ==========================================
# TradingBot V4.3
# Trade History
# ==========================================

"""
Trade History

Almacena todas las operaciones ejecutadas
durante el Paper Trading.
"""

from datetime import datetime


class TradeHistory:

    def __init__(self):

        self.history = []

    # ======================================

    def add_trade(self, position):

        trade = position.copy()

        trade["timestamp"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.history.append(trade)

    # ======================================

    def get_all(self):

        return self.history

    # ======================================

    def total_trades(self):

        return len(self.history)

    # ======================================

    def clear(self):

        self.history.clear()


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    history = TradeHistory()

    history.add_trade({

        "symbol": "BTC/USDT",

        "side": "BUY",

        "entry": 65000,

        "exit": 65500,

        "pnl": 50

    })

    print("===================================")
    print(" TRADE HISTORY ONLINE")
    print("===================================")

    print(history.get_all())

    print()

    print("Total:", history.total_trades())
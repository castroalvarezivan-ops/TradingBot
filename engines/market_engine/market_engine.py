# ==========================================
# TradingBot V5.0
# Market Engine
# ==========================================

"""
Market Engine

Centraliza todo el acceso al mercado.
"""

from scanner.scanner import (
    fetch_candles,
    get_current_price,
    get_dynamic_symbols
)


class MarketEngine:

    # ======================================

    def fetch_candles(

        self,

        symbol,

        timeframe="15m",

        limit=500

    ):
        """
        Descarga velas del mercado.

        Compatible con:

        - Pipeline Engine
        - Backtesting Engine
        """

        return fetch_candles(

            symbol,

            timeframe=timeframe,

            limit=limit

        )

    # ======================================

    def get_current_price(self, symbol):

        return get_current_price(symbol)

    # ======================================

    def get_dynamic_symbols(self, limit=50):

        return get_dynamic_symbols(limit)


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    print("===================================")
    print(" MARKET ENGINE V5")
    print("===================================")

    market = MarketEngine()

    df = market.fetch_candles(

        "BTC/USDT",

        timeframe="15m",

        limit=100

    )

    print(df.tail())
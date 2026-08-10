# ==========================================
# BLOQUE 1
# ==========================================

# ==========================================
# TradingBot V5.2
# Trade Logger
# ==========================================

"""
Trade Logger

Guarda todas las operaciones
del Backtesting en un archivo CSV.
"""

import csv
from pathlib import Path


BASE_DIR = Path(__file__).parent

LOG_FILE = BASE_DIR / "backtest_trades.csv"


class TradeLogger:

    def __init__(self):

        self.file = LOG_FILE

        self._create_file()

    # ======================================

    def _create_file(self):

        if self.file.exists():
            return

        with open(

            self.file,

            "w",

            newline="",

            encoding="utf-8"

        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([

                "timestamp",

                "symbol",

                "side",

                "entry",

                "exit",

                "quantity",

                "pnl",

                "balance"

            ])


# ==========================================
# BLOQUE 2
# ==========================================

# ======================================
    # Guardar operación
    # ======================================

    def log_trade(

        self,

        timestamp,

        symbol,

        side,

        entry,

        exit_price,

        quantity,

        pnl,

        balance

    ):

        with open(

            self.file,

            "a",

            newline="",

            encoding="utf-8"

        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([

                timestamp,

                symbol,

                side,

                round(entry, 4),

                round(exit_price, 4),

                round(quantity, 8),

                round(pnl, 2),

                round(balance, 2)

            ])


# ==========================================
# BLOQUE 3
# ==========================================

# ======================================
    # Limpiar archivo
    # ======================================

    def reset(self):

        if self.file.exists():

            self.file.unlink()

        self._create_file()


# ==========================================
# BLOQUE 4
# ==========================================

# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    logger = TradeLogger()

    logger.reset()

    logger.log_trade(

        timestamp="2026-07-21 08:45:00",

        symbol="BTC/USDT",

        side="BUY",

        entry=66250.0,

        exit_price=66500.0,

        quantity=0.15,

        pnl=37.50,

        balance=10037.50

    )

    print("===================================")
    print(" TRADE LOGGER ONLINE")
    print("===================================")
    print()
    print("Archivo generado:")
    print(logger.file)
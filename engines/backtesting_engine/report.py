# ==========================================
# TradingBot V5.1
# Report
# ==========================================

"""
Report

Genera el reporte final del Backtesting.
"""


class Report:

    def __init__(self):
        pass

    # ======================================

    def show(self, symbol, stats):

        print()

        print("===================================")
        print(" BACKTEST REPORT")
        print("===================================")

        print()

        print(f"Símbolo          : {symbol}")

        print(f"Capital Inicial : {stats['initial_balance']:.2f}")

        print(f"Capital Final   : {stats['final_balance']:.2f}")

        print()

        print(f"ROI             : {stats['roi']} %")

        print(f"Trades          : {stats['trades']}")

        print(f"Ganadoras       : {stats['wins']}")

        print(f"Perdedoras      : {stats['losses']}")

        print(f"Win Rate        : {stats['win_rate']} %")

        print()

        print(f"Gross Profit    : {stats['gross_profit']:.2f}")

        print(f"Gross Loss      : {stats['gross_loss']:.2f}")

        print(f"Profit Factor   : {stats['profit_factor']}")

        print(f"Max Drawdown    : {stats['max_drawdown']:.2f}")

        print()

        print("===================================")
        print(" FIN BACKTEST")
        print("===================================")
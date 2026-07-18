# ==========================================
# TradingBot V2.6.3
# Archivo: analytics/report.py
# ==========================================

from analytics.performance import (
    calculate_roi,
    calculate_profit_factor
)

from analytics.statistics import (
    average_win,
    average_loss,
    confidence_average
)


def generate_report(portfolio, trades):
    """
    Genera el reporte principal del Backtesting.
    """

    wallet = portfolio.wallet

    roi = calculate_roi(
        wallet.initial_balance,
        wallet.balance
    )

    profit_factor = calculate_profit_factor(trades)

    avg_win = average_win(trades)

    avg_loss = average_loss(trades)

    avg_confidence = confidence_average(trades)

    print("\n")
    print("=" * 50)
    print("📈 PERFORMANCE REPORT V2.6.3")
    print("=" * 50)

    print(f"Capital Inicial      : {wallet.initial_balance:.2f}")
    print(f"Capital Final        : {wallet.balance:.2f}")

    print("-" * 50)

    print(f"ROI                  : {roi:.2f}%")

    print(f"Trades               : {wallet.trades}")

    print(f"Wins                 : {wallet.wins}")

    print(f"Losses               : {wallet.losses}")

    print(f"Win Rate             : {wallet.win_rate:.2f}%")

    print(f"Profit Factor        : {profit_factor:.2f}")

    print("-" * 50)

    print(f"Average Win          : {avg_win}")

    print(f"Average Loss         : {avg_loss}")

    print(f"Confidence Promedio  : {avg_confidence}")

    print("=" * 50)
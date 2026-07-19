# ==========================================
# TradingBot V2.6.7
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

from analytics.expectancy import (
    ExpectancyCalculator
)

from analytics.drawdown import (
    DrawdownAnalyzer
)


def generate_report(portfolio, trades):
    """
    Genera el reporte completo del Backtesting.
    """

    wallet = portfolio.wallet

    # ==========================================
    # Performance
    # ==========================================

    roi = calculate_roi(
        wallet.initial_balance,
        wallet.balance
    )

    profit_factor = calculate_profit_factor(trades)

    # ==========================================
    # Statistics
    # ==========================================

    avg_win = average_win(trades)

    avg_loss = average_loss(trades)

    avg_confidence = confidence_average(trades)

    # ==========================================
    # Expectancy
    # ==========================================

    expectancy = ExpectancyCalculator().calculate(trades)

    # ==========================================
    # Drawdown
    # ==========================================

    drawdown = DrawdownAnalyzer().calculate(
        portfolio.equity_curve.get_history()
    )

    # ==========================================
    # Capital
    # ==========================================

    total_profit = (
        wallet.balance -
        wallet.initial_balance
    )

    # ==========================================
    # Reporte
    # ==========================================

    print()

    print("=" * 60)

    print("📈 PERFORMANCE REPORT V2.6.7")

    print("=" * 60)

    print(f"Capital Inicial      : {wallet.initial_balance:,.2f}")

    print(f"Capital Final        : {wallet.balance:,.2f}")

    print(f"Ganancia Total       : {total_profit:,.2f}")

    print("-" * 60)

    print(f"ROI                  : {roi:.2f}%")

    print(f"Profit Factor        : {profit_factor:.2f}")

    print(f"Expectancy           : {expectancy:.2f}")

    print(f"Max Drawdown         : {drawdown:.2f}%")

    print("-" * 60)

    print(f"Trades               : {wallet.trades}")

    print(f"Wins                 : {wallet.wins}")

    print(f"Losses               : {wallet.losses}")

    print(f"Win Rate             : {wallet.win_rate:.2f}%")

    print("-" * 60)

    print(f"Average Win          : {avg_win:.2f}")

    print(f"Average Loss         : {avg_loss:.2f}")

    print(f"Confidence Promedio  : {avg_confidence:.2f}")

    print("=" * 60)
# ==========================================
# TradingBot V2.6.3
# Archivo: backtesting/engine.py
# ==========================================

from strategy.strategy import calculate_indicators
from strategy.decision_engine import evaluate

from backtesting.trade_executor import execute_trade

from portfolio.manager import PortfolioManager
from portfolio.position import Position

from analytics.report import generate_report
from analytics.exporter import export_trades


def run_backtest(df):
    """
    Motor principal del Backtesting.

    Flujo:

        Datos
          ↓
    Indicadores
          ↓
    Decision Engine
          ↓
    Trade Executor
          ↓
    Portfolio
          ↓
    Analytics
          ↓
    Export CSV
    """

    trades = []

    portfolio = PortfolioManager(
        initial_balance=10000
    )

    # ==========================================
    # Validación
    # ==========================================

    if df is None or len(df) < 60:

        print(
            f"DEBUG: Datos insuficientes "
            f"({len(df) if df is not None else 0} filas)"
        )

        return trades

    # ==========================================
    # Indicadores
    # ==========================================

    df = calculate_indicators(df)

    if df is None:
        return trades

    # ==========================================
    # Backtesting
    # ==========================================

    for i in range(60, len(df)):

        latest = df.iloc[i]

        action, score, reason = evaluate(latest)

        if action not in ["BUY", "SELL"]:
            continue

        if portfolio.has_open_position(
            "BTCUSDT",
            action
        ):
            continue

        position = Position(

            symbol="BTCUSDT",

            side=action,

            entry=latest["close"],

            stop_loss=0,

            take_profit=0,

            quantity=1,

            opened_at=latest.name

        )

        portfolio.open_position(position)

        result, exit_price, bars_held = execute_trade(
            df,
            i,
            action
        )

        portfolio.close_position(
            position,
            exit_price,
            result
        )

        trades.append(

            {

                "symbol": position.symbol,

                "side": position.side,

                "entry": position.entry,

                "exit": exit_price,

                "result": result,

                "score": score,

                "reason": reason,

                "bars_held": bars_held,

                "opened_at": position.opened_at,

                "closed_at": position.closed_at,

            }

        )

    # ==========================================
    # Analytics
    # ==========================================

    generate_report(
        portfolio,
        trades
    )

    # ==========================================
    # Exportar CSV
    # ==========================================

    export_trades(trades)

    return trades
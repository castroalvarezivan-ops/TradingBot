# ==========================================
# TradingBot V2.6.5
# Archivo: analytics/expectancy.py
# ==========================================

"""
Calcula la Expectancy de una estrategia.

Expectancy =
(WinRate × Average Win)
-
(LossRate × Average Loss)
"""

class ExpectancyCalculator:

    def calculate(self, trades):

        if not trades:
            return 0.0

        wins = [
            t for t in trades
            if t.get("pnl", 0) > 0
        ]

        losses = [
            t for t in trades
            if t.get("pnl", 0) < 0
        ]

        total = len(trades)

        if total == 0:
            return 0.0

        win_rate = len(wins) / total
        loss_rate = len(losses) / total

        average_win = (
            sum(t["pnl"] for t in wins) / len(wins)
            if wins else 0
        )

        average_loss = (
            abs(sum(t["pnl"] for t in losses) / len(losses))
            if losses else 0
        )

        expectancy = (
            win_rate * average_win
            -
            loss_rate * average_loss
        )

        return round(expectancy, 2)
# ==========================================
# TradingBot V5.1
# Metrics
# ==========================================

"""
Metrics

Calcula las estadísticas del Backtesting.
"""

class Metrics:

    def __init__(self):

        self.initial_balance = 10000.0

    # ======================================

    def calculate(self, trades):

        total = len(trades)

        wins = 0

        losses = 0

        gross_profit = 0.0

        gross_loss = 0.0

        final_balance = self.initial_balance

        max_balance = self.initial_balance

        max_drawdown = 0.0

        # ==============================

        for trade in trades:

            pnl = trade["pnl"]

            final_balance = trade["balance"]

            if pnl >= 0:

                wins += 1

                gross_profit += pnl

            else:

                losses += 1

                gross_loss += abs(pnl)

            if final_balance > max_balance:

                max_balance = final_balance

            drawdown = max_balance - final_balance

            if drawdown > max_drawdown:

                max_drawdown = drawdown

        # ==============================

        if total == 0:

            win_rate = 0

        else:

            win_rate = round((wins / total) * 100, 2)

        roi = round(

            ((final_balance - self.initial_balance)

            / self.initial_balance) * 100,

            2

        )

        if gross_loss == 0:

            profit_factor = gross_profit

        else:

            profit_factor = round(

                gross_profit / gross_loss,

                2

            )

        return {

            "initial_balance": round(self.initial_balance, 2),

            "final_balance": round(final_balance, 2),

            "roi": roi,

            "trades": total,

            "wins": wins,

            "losses": losses,

            "win_rate": win_rate,

            "gross_profit": round(gross_profit, 2),

            "gross_loss": round(gross_loss, 2),

            "profit_factor": profit_factor,

            "max_drawdown": round(max_drawdown, 2)

        }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    metrics = Metrics()

    sample = [

        {

            "pnl": 120,

            "balance": 10120

        },

        {

            "pnl": -50,

            "balance": 10070

        },

        {

            "pnl": 200,

            "balance": 10270

        }

    ]

    print(metrics.calculate(sample))
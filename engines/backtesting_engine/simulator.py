# ==========================================
# TradingBot V5.1
# Simulator
# ==========================================

"""
Simulator

Simula operaciones utilizando las señales
generadas por el Decision Engine.

Por ahora:

BUY
HOLD

Más adelante agregaremos:

SELL
SHORT
Trailing Stop
Break Even
Parcial TP
"""

class Simulator:

    def __init__(self):

        self.initial_balance = 10000.0

    # ======================================

    def run(

        self,

        dataframe,

        decisions

    ):

        trades = []

        balance = self.initial_balance

        position = None

        for i in range(len(dataframe)):

            candle = dataframe.iloc[i]

            decision = decisions[i]

            price = float(candle["close"])

            # ===============================
            # Abrir operación
            # ===============================

            if position is None:

                if decision.action == "BUY":

                    position = {

                        "entry": price,

                        "entry_index": i

                    }

            # ===============================
            # Cerrar operación
            # ===============================

            else:

                if decision.action != "BUY":

                    pnl = price - position["entry"]

                    balance += pnl

                    trades.append({

                        "entry": position["entry"],

                        "exit": price,

                        "pnl": round(pnl, 2),

                        "balance": round(balance, 2)

                    })

                    position = None

        return trades
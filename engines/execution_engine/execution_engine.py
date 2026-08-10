# ==========================================
# TradingBot V4.2
# Execution Engine
# ==========================================

"""
Execution Engine

Responsabilidades

- Preparar órdenes
- Ejecutar órdenes reales (cuando se habilite)
- Simulación de ejecución
- Registro de operaciones

Actualmente trabaja en modo SIMULACIÓN.
"""

from execution.execution import (
    place_market_order,
    get_balance
)


class ExecutionEngine:

    def __init__(self):
        self.simulation = True

    # ======================================
    # Balance
    # ======================================

    def balance(self):

        free, total = get_balance()

        return {

            "free": free,

            "total": total

        }

    # ======================================
    # Simulación / Ejecución
    # ======================================

    def execute_order(

        self,

        symbol,

        action,

        price,

        quantity=None

    ):

        # -----------------------------
        # MODO SIMULACIÓN
        # -----------------------------

        if self.simulation:

            return {

                "status": "SIMULATION",

                "symbol": symbol,

                "action": action,

                "price": price,

                "quantity": quantity,

                "message": "Orden simulada correctamente."

            }

        # -----------------------------
        # MODO REAL
        # -----------------------------

        if quantity is None:

            return {

                "status": "ERROR",

                "message": "Cantidad inválida."

            }

        order = place_market_order(

            symbol,

            action,

            quantity

        )

        if order:

            return {

                "status": "SUCCESS",

                "order": order

            }

        return {

            "status": "ERROR",

            "message": "No fue posible ejecutar la orden."

        }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    engine = ExecutionEngine()

    print("===================================")
    print(" Execution Engine ONLINE")
    print("===================================")

    print(engine.balance())

    print()

    print(

        engine.execute_order(

            symbol="BTC/USDT",

            action="BUY",

            price=65000

        )

    )
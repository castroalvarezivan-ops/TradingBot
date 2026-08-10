# ==========================================
# TradingBot V4.3
# Position Engine
# ==========================================

"""
Position Engine

Calcula automáticamente:

- Tamaño de posición
- Riesgo monetario
- Stop Loss
- Take Profit
- Relación Riesgo/Beneficio
"""

from risk.risk import calculate_risk_parameters


class PositionEngine:

    def __init__(self):
        pass

    # ======================================
    # Construir operación
    # ======================================

    def build_position(
        self,
        balance,
        symbol,
        action,
        entry_price,
        atr,
        risk_percent=1
    ):

        stop_loss, take_profit = calculate_risk_parameters(
            entry_price,
            atr,
            action
        )

        risk_amount = balance * (risk_percent / 100)

        risk_per_unit = abs(entry_price - stop_loss)

        if risk_per_unit == 0:
            quantity = 0
        else:
            quantity = risk_amount / risk_per_unit

        return {

            "symbol": symbol,

            "action": action,

            "entry": entry_price,

            "stop_loss": stop_loss,

            "take_profit": take_profit,

            "risk_percent": risk_percent,

            "risk_amount": risk_amount,

            "quantity": quantity

        }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    engine = PositionEngine()

    result = engine.build_position(

        balance=10000,

        symbol="BTC/USDT",

        action="BUY",

        entry_price=65000,

        atr=120

    )

    print("===================================")
    print(" Position Engine ONLINE")
    print("===================================")

    print(result)
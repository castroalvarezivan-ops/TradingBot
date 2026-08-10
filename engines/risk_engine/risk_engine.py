# ==========================================
# TradingBot Executive V8
# engines/risk_engine/risk_engine.py
# Institutional Risk Engine
# ==========================================

"""
Risk Engine

Valida que una operación pueda ejecutarse
antes de enviarla al Execution Engine.
"""

from config.config import MAX_RISK_PER_TRADE


class RiskEngine:

    def __init__(self):

        self.max_daily_drawdown = 8      # %
        self.max_trade_risk = MAX_RISK_PER_TRADE

    # ======================================
    # Validación principal
    # ======================================

    def validate(self, portfolio, position):

        """
        Devuelve:

        valid
        reason
        """

        if position is None:

            return False, "No existe posición."

        # ==========================
        # Balance mínimo
        # ==========================

        if portfolio["balance"] <= 20:

            return False, "Balance insuficiente."

        # ==========================
        # Riesgo %
        # ==========================

        if position["risk_percent"] > self.max_trade_risk:

            return False, "Riesgo por operación demasiado alto."

        # ==========================
        # Drawdown
        # ==========================

        if portfolio.get("drawdown", 0) >= self.max_daily_drawdown:

            return False, "Drawdown máximo alcanzado."

        # ==========================
        # Tamaño de posición
        # ==========================

        if position["quantity"] <= 0:

            return False, "Cantidad inválida."

        return True, "OK"


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    risk = RiskEngine()

    portfolio = {
        "balance": 1000,
        "drawdown": 2
    }

    position = {
        "quantity": 0.015,
        "risk_percent": 1.5
    }

    print(risk.validate(portfolio, position))
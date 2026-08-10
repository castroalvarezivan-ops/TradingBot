# ==========================================
# TradingBot V3.2
# Strategy Engine
# ==========================================

"""
Strategy Engine

Este motor encapsula toda la lógica de estrategia.

Responsabilidades

- Calcular indicadores
- Evaluar mercado
- Generar score
- Generar decisión

El API nunca llamará directamente a strategy.py.

Siempre utilizará este motor.
"""

from strategy.strategy import (
    calculate_indicators,
    evaluate_market_condition
)


class StrategyEngine:

    def __init__(self):
        pass

    # ======================================
    # Indicadores
    # ======================================

    def indicators(self, dataframe):
        """
        Calcula todos los indicadores.
        """
        return calculate_indicators(dataframe)

    # ======================================
    # Decisión
    # ======================================

    def evaluate(self, dataframe):
        """
        Devuelve:

        action
        score
        reason
        """

        return evaluate_market_condition(dataframe)

    # ======================================
    # Pipeline completo
    # ======================================

    def process(self, dataframe):

        dataframe = self.indicators(dataframe)

        action, score, reason = self.evaluate(dataframe)

        return {

            "dataframe": dataframe,

            "action": action,

            "score": score,

            "reason": reason

        }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    print("===================================")
    print(" Strategy Engine ONLINE")
    print("===================================")
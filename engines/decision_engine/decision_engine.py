# ==========================================
# TradingBot Executive V8
# engines/decision_engine/decision_engine.py
# ==========================================

"""
Decision Engine V8 Executive

Convierte el score institucional en una decisión
BUY / SELL / HOLD junto con un nivel de confianza.

Compatible con:
- Pipeline Engine V8
- Dashboard Executive
- API V8
"""

from models.decision_result import DecisionResult

from strategy.score_engine import calculate_score
from strategy.confidence import calculate_confidence


class DecisionEngine:

    def __init__(self):

        self.buy_threshold = 75
        self.strong_buy = 90

        self.sell_threshold = -75
        self.strong_sell = -90

    # ======================================
    # Evaluación principal
    # ======================================

    def evaluate(self, latest):

        score, reasons = calculate_score(latest)

        confidence, level = calculate_confidence(score)

        # -----------------------------
        # BUY
        # -----------------------------

        if score >= self.strong_buy:

            action = "BUY"

            reasons.append("Momentum institucional muy fuerte")

        elif score >= self.buy_threshold:

            action = "BUY"

            reasons.append("Tendencia alcista confirmada")

        # -----------------------------
        # SELL
        # -----------------------------

        elif score <= self.strong_sell:

            action = "SELL"

            reasons.append("Presión bajista institucional")

        elif score <= self.sell_threshold:

            action = "SELL"

            reasons.append("Tendencia bajista confirmada")

        # -----------------------------
        # HOLD
        # -----------------------------

        else:

            action = "HOLD"

            reasons.append("No existe ventaja estadística")

        return DecisionResult(

            action=action,

            score=score,

            confidence=confidence,

            reason=" | ".join(reasons)

        )


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    print("===================================")
    print(" Decision Engine Executive V8")
    print("===================================")

    engine = DecisionEngine()

    print()

    print("BUY Threshold :", engine.buy_threshold)
    print("SELL Threshold:", engine.sell_threshold)

    print()

    print("Decision Engine cargado correctamente.")

    print("===================================")
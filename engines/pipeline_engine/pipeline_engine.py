# ==========================================
# TradingBot Executive V8
# Pipeline Engine
# Institutional Version
# ==========================================

"""
Pipeline Engine V8

Flujo del sistema

Market
↓
Strategy
↓
Decision
↓
Portfolio
↓
Risk
↓
Precio Actual
↓
Trade Manager
↓
Position
↓
Paper Trading
↓
Execution
"""

from datetime import datetime
import time
import uuid

from engines.market_engine.market_engine import MarketEngine
from engines.strategy_engine.strategy_engine import StrategyEngine
from engines.decision_engine.decision_engine import DecisionEngine
from engines.risk_engine.risk_engine import RiskEngine
from engines.portfolio_engine.portfolio_engine import PortfolioEngine
from engines.position_engine.position_engine import PositionEngine
from engines.execution_engine.execution_engine import ExecutionEngine

from paper_trading.paper_engine import PaperEngine
from paper_trading.trade_manager import TradeManager


class PipelineEngine:

    def __init__(self):

        self.market = MarketEngine()
        self.strategy = StrategyEngine()
        self.decision = DecisionEngine()
        self.risk = RiskEngine()
        self.portfolio = PortfolioEngine()
        self.position = PositionEngine()
        self.execution = ExecutionEngine()

        self.paper = PaperEngine()
        self.trade_manager = TradeManager()

    # ======================================
    # STATUS
    # ======================================

    def status(self):

        return {

            "market": "ONLINE",
            "strategy": "ONLINE",
            "decision": "ONLINE",
            "risk": "ONLINE",
            "portfolio": "ONLINE",
            "position": "ONLINE",
            "paper": "ONLINE",
            "execution": "ONLINE"

        }

    # ======================================
    # CALIFICACIÓN
    # ======================================

    def calculate_grade(self, score):

        if score >= 97:
            return "A+"

        elif score >= 94:
            return "A"

        elif score >= 90:
            return "B+"

        elif score >= 85:
            return "B"

        elif score >= 80:
            return "C"

        return "D"

    # ======================================
    # MARKET REGIME
    # ======================================

    def detect_market_regime(self, dataframe):

        try:

            atr = dataframe["atr"].iloc[-1]

            ema20 = dataframe["ema20"].iloc[-1]
            ema50 = dataframe["ema50"].iloc[-1]

            if atr > dataframe["atr"].mean() * 1.40:
                return "VOLATILE"

            if ema20 > ema50:
                return "TRENDING"

            if ema20 < ema50:
                return "BEARISH"

            return "RANGING"

        except Exception:

            return "UNKNOWN"

    # ======================================
    # PIPELINE PRINCIPAL
    # ======================================

    def process(self, symbol):

        start = time.perf_counter()

        print("Paso 1 -> Descargando mercado...")

        df = self.market.fetch_candles(symbol)

        if df is None:

            return {

                "status": "ERROR",

                "reason": "No fue posible descargar datos."

            }

        # ----------------------------------

        print("Paso 2 -> Strategy Engine...")

        strategy_result = self.strategy.process(df)

        latest = strategy_result["dataframe"].iloc[-1]

        # ----------------------------------

        print("Paso 3 -> Decision Engine...")

        decision = self.decision.evaluate(latest)

        # ----------------------------------

        print("Paso 4 -> Portfolio Engine...")

        if decision.action != "HOLD":

            if self.portfolio.has_open_position(
                symbol,
                decision.action
            ):

                return {

                    "status": "BLOCKED",

                    "symbol": symbol,

                    "action": decision.action,

                    "reason": "Ya existe una posición abierta."

                }

        portfolio = self.portfolio.get_summary()

        # ----------------------------------

        print("Paso 5 -> Risk Engine...")

        valid = True
        reason_risk = "Pendiente integración"

        # ----------------------------------

        print("Paso 6 -> Precio actual...")

        price = self.market.get_current_price(symbol)

        # ----------------------------------

        print("Paso 7 -> Trade Manager...")

        closed_trades = self.trade_manager.update(price)

        # ----------------------------------

        print("Paso 8 -> Position Engine...")

        position = None

        if decision.action != "HOLD":

            position = self.position.build_position(

                balance=portfolio["balance"],

                symbol=symbol,

                action=decision.action,

                entry_price=price,

                atr=float(latest["atr"])

            )

        # ----------------------------------

        print("Paso 9 -> Paper Trading...")

        paper_trade = None

        if position:

            paper_trade = self.trade_manager.open_trade(

                symbol=position["symbol"],

                side=position["action"],

                entry=position["entry"],

                quantity=position["quantity"],

                stop_loss=position["stop_loss"],

                take_profit=position["take_profit"]

            )

        # ----------------------------------

        print("Paso 10 -> Execution Engine...")

        execution_result = None

        if decision.action != "HOLD" and valid:

            execution_result = {

                "status": "SIMULATION",

                "symbol": symbol,

                "action": decision.action,

                "price": price,

                "message": "Orden preparada"

            }

        # ======================================
        # MÉTRICAS EJECUTIVAS
        # ======================================

        market_regime = self.detect_market_regime(strategy_result["dataframe"])

        grade = self.calculate_grade(decision.score)

        quality = round(
            decision.score * 0.60 +
            decision.confidence * 0.40,
            2
        )

        priority = "NORMAL"

        if decision.score >= 95:
            priority = "PREMIUM"

        elif decision.score >= 90:
            priority = "HIGH"

        risk_percent = None
        reward_percent = None
        rr = None

        if position:

            risk_percent = round(

                abs(
                    position["entry"] -
                    position["stop_loss"]
                ) /

                position["entry"] * 100,

                2

            )

            reward_percent = round(

                abs(
                    position["take_profit"] -
                    position["entry"]
                ) /

                position["entry"] * 100,

                2

            )

            if risk_percent > 0:

                rr = round(

                    reward_percent /

                    risk_percent,

                    2

                )

        elapsed = round(

            time.perf_counter() - start,

            3

        )

        # ======================================

        print("Paso 11 -> Pipeline finalizado.")

        return {

            "status": "OK",

            "symbol": symbol,

            "price": price,

            "action": decision.action,

            "score": decision.score,

            "confidence": decision.confidence,

            "grade": grade,

            "priority": priority,

            "quality": quality,

            "market_regime": market_regime,

            "execution_time": elapsed,

            "timestamp": datetime.now().strftime("%H:%M:%S"),

            "trade_id": str(uuid.uuid4())[:8],

            "reason": decision.reason,

            "risk_ok": valid,

            "risk_reason": reason_risk,

            "risk_percent": risk_percent,

            "reward_percent": reward_percent,

            "rr": rr,

            "atr": float(latest["atr"]),

            "portfolio": portfolio,

            "closed_trades": closed_trades,

            "position": position,

            "paper_trade": paper_trade,

            "execution": execution_result

        }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    pipeline = PipelineEngine()

    print("====================================")
    print(" TradingBot Executive V8")
    print(" Pipeline Engine")
    print("====================================")

    result = pipeline.process("BTCUSDT")

    print(result)
# ==========================================
# TradingBot V5.1
# Backtesting Engine
# ==========================================

"""
Backtesting Engine

Coordina todo el proceso de Backtesting.

Flujo

Market
    ↓
Strategy
    ↓
Decision
    ↓
Simulator
    ↓
Metrics
    ↓
Report
"""

from engines.market_engine.market_engine import MarketEngine
from engines.strategy_engine.strategy_engine import StrategyEngine
from engines.decision_engine.decision_engine import DecisionEngine

from engines.backtesting_engine.simulator import Simulator
from engines.backtesting_engine.metrics import Metrics
from engines.backtesting_engine.report import Report


class BacktestingEngine:

    def __init__(self):

        self.market = MarketEngine()

        self.strategy = StrategyEngine()

        self.decision = DecisionEngine()

        self.simulator = Simulator()

        self.metrics = Metrics()

        self.report = Report()

    # ======================================

    def run(

        self,

        symbol,

        timeframe="15m",

        limit=1000

    ):

        print()

        print("===================================")
        print(" INICIANDO BACKTEST")
        print("===================================")

        print()

        print("Paso 1 -> Descargando mercado...")

        df = self.market.fetch_candles(

            symbol,

            timeframe=timeframe,

            limit=limit

        )

        print("Velas descargadas:", len(df))

        print()

        print("Paso 2 -> Strategy Engine...")

        strategy = self.strategy.process(df)

        dataframe = strategy["dataframe"]

        print()

        print("Paso 3 -> Decision Engine...")

        decisions = []

        for _, row in dataframe.iterrows():

            decision = self.decision.evaluate(row)

            decisions.append(decision)

        print("Decisiones generadas:", len(decisions))

        print()

        print("Paso 4 -> Simulator...")

        trades = self.simulator.run(

            dataframe,

            decisions

        )

        print("Trades simulados:", len(trades))

        print()

        print("Paso 5 -> Metrics...")

        stats = self.metrics.calculate(trades)

        print()

        print("Paso 6 -> Report...")

        self.report.show(

            symbol,

            stats

        )

        return stats


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    engine = BacktestingEngine()

    engine.run(

        "BTC/USDT"

    )
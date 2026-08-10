# ==========================================
# TradingBot V4.2
# Core Engine
# ==========================================

"""
Core Engine

Núcleo principal del sistema.

Su única responsabilidad es iniciar el Pipeline
y ejecutar ciclos completos del TradingBot.
"""

from engines.pipeline_engine.pipeline_engine import PipelineEngine


class CoreEngine:

    def __init__(self):

        print("===================================")
        print(" Inicializando Core Engine")
        print("===================================")

        self.pipeline = PipelineEngine()

    # ======================================
    # Estado general
    # ======================================

    def get_status(self):

        return {

            "core": "ONLINE",

            "pipeline": self.pipeline.status()

        }

    # ======================================
    # Ejecutar un ciclo completo
    # ======================================

    def run_cycle(self, symbol):

        print(f"\nEjecutando ciclo para: {symbol}")

        return self.pipeline.process(symbol)


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    core = CoreEngine()

    print()

    print(core.get_status())
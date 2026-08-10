# ==========================================
# TradingBot V4.2
# Portfolio Engine
# ==========================================

"""
Portfolio Engine

Conecta el Core Engine con el sistema financiero.

No contiene la lógica del portafolio.

Simplemente utiliza PortfolioManager.
"""

from portfolio.manager import PortfolioManager


class PortfolioEngine:

    def __init__(self):

        self.manager = PortfolioManager()

    # ======================================
    # Resumen del Portafolio
    # ======================================

    def get_summary(self):

        wallet = self.manager.wallet

        return {

            "balance": wallet.balance,

            "initial_balance": wallet.initial_balance,

            "roi": wallet.roi,

            "win_rate": wallet.win_rate,

            "profit_factor": wallet.profit_factor,

            "active_positions": len(
                self.manager.active_positions
            )

        }

    # ======================================
    # Verificar posición abierta
    # ======================================

    def has_open_position(self, symbol, side):

        return self.manager.has_open_position(
            symbol,
            side
        )

    # ======================================
    # Acceso al PortfolioManager
    # ======================================

    def manager_instance(self):

        return self.manager


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    portfolio = PortfolioEngine()

    print("===================================")
    print(" Portfolio Engine ONLINE")
    print("===================================")

    print(portfolio.get_summary())

    print()

    print(
        portfolio.has_open_position(
            "BTC/USDT",
            "BUY"
        )
    )
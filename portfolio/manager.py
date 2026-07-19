# ==========================================
# TradingBot V2.6.6
# Archivo: portfolio/manager.py
# ==========================================

from portfolio.wallet import Wallet

from analytics.trade_history import TradeHistory
from analytics.equity_curve import EquityCurve


class PortfolioManager:
    """
    Controlador financiero principal.

    Responsabilidades:
    - Gestionar Wallet
    - Gestionar posiciones abiertas
    - Registrar historial de operaciones
    - Registrar Equity Curve
    """

    def __init__(self, initial_balance=10000):

        self.wallet = Wallet(initial_balance=initial_balance)

        self.active_positions = []

        # Analytics
        self.trade_history = TradeHistory()
        self.equity_curve = EquityCurve()

        # Primer punto de la curva
        self.equity_curve.add_balance(self.wallet.balance)

    def open_position(self, position):
        """
        Registra una nueva posición abierta.
        """
        self.active_positions.append(position)

    def close_position(
        self,
        position,
        exit_price,
        result,
        score=0,
        confidence=0,
        bars_held=0
    ):
        """
        Cierra una posición y actualiza todo el sistema financiero.
        """

        # =====================================
        # Calcular PnL
        # =====================================

        if position.side == "BUY":

            pct_change = (
                exit_price - position.entry
            ) / position.entry

        else:

            pct_change = (
                position.entry - exit_price
            ) / position.entry

        pnl = self.wallet.balance * pct_change

        # =====================================
        # Actualizar posición
        # =====================================

        position.close(exit_price, result)

        # =====================================
        # Actualizar Wallet
        # =====================================

        self.wallet.update_balance(result, pnl)

        # =====================================
        # Registrar operación
        # =====================================

        trade = {

            "symbol": position.symbol,

            "side": position.side,

            "entry": position.entry,

            "exit": exit_price,

            "result": result,

            "pnl": round(pnl, 2),

            "score": score,

            "confidence": confidence,

            "bars_held": bars_held

        }

        self.trade_history.add_trade(trade)

        # =====================================
        # Actualizar Equity Curve
        # =====================================

        self.equity_curve.add_balance(
            self.wallet.balance
        )

        # =====================================
        # Eliminar posición abierta
        # =====================================

        if position in self.active_positions:
            self.active_positions.remove(position)

    def has_open_position(self, symbol, side):
        """
        Verifica si existe una posición abierta.
        """

        for position in self.active_positions:

            if (
                position.symbol == symbol
                and position.side == side
            ):
                return True

        return False
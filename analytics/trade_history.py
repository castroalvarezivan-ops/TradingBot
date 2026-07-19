# ==========================================
# TradingBot V2.6.5
# Archivo: analytics/trade_history.py
# ==========================================

"""
Gestiona el historial completo de operaciones.

Responsabilidades:
- Registrar operaciones
- Consultar historial
- Obtener estadísticas básicas

Base para:
- Exportador CSV
- Exportador Excel
- Equity Curve
- Dashboard
- Expectancy
- Estadísticas avanzadas
"""

class TradeHistory:
    """
    Almacena todas las operaciones realizadas
    durante Backtesting o Live Trading.
    """

    def __init__(self):
        self.trades = []

    def add_trade(self, trade):
        """
        Agrega una operación al historial.

        Parámetro:
            trade (dict)
        """
        self.trades.append(trade)

    def get_all(self):
        """
        Devuelve todas las operaciones.
        """
        return self.trades

    def total(self):
        """
        Número total de operaciones.
        """
        return len(self.trades)

    def wins(self):
        """
        Número de operaciones ganadoras.
        """
        return len([
            trade
            for trade in self.trades
            if trade.get("result") == "WIN"
        ])

    def losses(self):
        """
        Número de operaciones perdedoras.
        """
        return len([
            trade
            for trade in self.trades
            if trade.get("result") == "LOSS"
        ])

    def timeouts(self):
        """
        Número de operaciones cerradas por Time Stop.
        """
        return len([
            trade
            for trade in self.trades
            if trade.get("result") == "TIMEOUT"
        ])

    def opens(self):
        """
        Número de operaciones abiertas.
        """
        return len([
            trade
            for trade in self.trades
            if trade.get("result") == "OPEN"
        ])

    def get_winning_trades(self):
        """
        Devuelve únicamente las operaciones ganadoras.
        """
        return [
            trade
            for trade in self.trades
            if trade.get("result") == "WIN"
        ]

    def get_losing_trades(self):
        """
        Devuelve únicamente las operaciones perdedoras.
        """
        return [
            trade
            for trade in self.trades
            if trade.get("result") == "LOSS"
        ]

    def reset(self):
        """
        Limpia completamente el historial.
        """
        self.trades.clear()

    def __len__(self):
        """
        Permite usar len(trade_history)
        """
        return len(self.trades)

    def __iter__(self):
        """
        Permite recorrer el historial con un for.
        """
        return iter(self.trades)
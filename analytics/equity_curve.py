# ==========================================
# TradingBot V2.6.4
# Archivo: analytics/equity_curve.py
# ==========================================

class EquityCurve:
    """
    Gestiona la evolución del capital durante el backtesting.
    """

    def __init__(self):
        self.history = []

    def add_balance(self, balance):
        """
        Agrega un nuevo balance al historial.
        """
        self.history.append(round(balance, 2))

    def get_history(self):
        """
        Devuelve el historial completo del capital.
        """
        return self.history

    def last_balance(self):
        """
        Devuelve el último balance registrado.
        """
        if not self.history:
            return 0.0
        return self.history[-1]

    def reset(self):
        """
        Reinicia la curva de equity.
        """
        self.history.clear()

    @property
    def max_balance(self):
        if not self.history:
            return 0.0
        return max(self.history)

    @property
    def min_balance(self):
        if not self.history:
            return 0.0
        return min(self.history)

    @property
    def total_points(self):
        return len(self.history)
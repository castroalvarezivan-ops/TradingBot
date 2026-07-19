# ==========================================
# TradingBot V2.6.4
# Archivo: analytics/drawdown.py
# ==========================================

class DrawdownAnalyzer:
    """
    Calcula el Drawdown máximo utilizando
    la curva de Equity.
    """

    def __init__(self):
        self.max_drawdown = 0.0
        self.peak = None

    def calculate(self, equity_history):
        """
        Calcula el Drawdown máximo.

        Parámetros
        ----------
        equity_history : list[float]

        Retorna
        -------
        float (%)
        """

        if len(equity_history) == 0:
            return 0.0

        self.peak = equity_history[0]
        self.max_drawdown = 0.0

        for balance in equity_history:

            if balance > self.peak:
                self.peak = balance

            drawdown = (self.peak - balance) / self.peak

            if drawdown > self.max_drawdown:
                self.max_drawdown = drawdown

        return round(self.max_drawdown * 100, 2)

    def reset(self):
        self.max_drawdown = 0.0
        self.peak = None
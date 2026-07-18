# ==========================================
# TradingBot V2.6.2
# Archivo: analytics/trade_history.py
# ==========================================

"""
Gestiona el historial de operaciones del Backtesting.

Próximamente permitirá:

- Exportar CSV
- Exportar Excel
- Equity Curve
- Estadísticas avanzadas
- Expectancy
- Average Win
- Average Loss
"""

class TradeHistory:

    def __init__(self):
        self.trades = []

    def add_trade(self, trade):
        self.trades.append(trade)

    def get_all(self):
        return self.trades

    def total(self):
        return len(self.trades)
# V2.6.1 STABLE
# Archivo: portfolio/position.py

from datetime import datetime

class Position:
    """
    Representa una posición abierta o cerrada en el mercado.
    """
    def __init__(self, symbol, side, entry, stop_loss, take_profit, quantity, opened_at=None):
        self.symbol = symbol
        self.side = side  # BUY o SELL
        self.entry = entry
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.quantity = quantity
        self.opened_at = opened_at if opened_at else datetime.now()
        
        # Estado de la operación
        self.status = "OPEN"
        self.exit_price = None
        self.result = None  # WIN, LOSS, TIMEOUT, OPEN
        self.closed_at = None

    def close(self, exit_price, result):
        """
        Cierra la posición y registra los datos finales.
        """
        self.exit_price = exit_price
        self.result = result
        self.status = "CLOSED"
        self.closed_at = datetime.now()

    def __repr__(self):
        return f"Position({self.symbol}, {self.side}, Entry: {self.entry}, Status: {self.status})"
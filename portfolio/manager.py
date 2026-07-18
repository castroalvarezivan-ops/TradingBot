from portfolio.wallet import Wallet

class PortfolioManager:
    """
    Controlador central que gestiona la Wallet y las posiciones activas.
    """
    def __init__(self, initial_balance=10000):
        self.wallet = Wallet(initial_balance=initial_balance)
        self.active_positions = []

    def open_position(self, position):
        """Registra una nueva posición como abierta."""
        self.active_positions.append(position)

    def close_position(self, position, exit_price, result):
        """
        Cierra una posición, calcula el PnL monetario y actualiza la wallet.
        """
        # 1. Calcular el cambio porcentual
        if position.side == "BUY":
            pct_change = (exit_price - position.entry) / position.entry
        else: # SELL
            pct_change = (position.entry - exit_price) / position.entry

        # 2. Calcular monto en dinero basado en el balance actual
        pnl = self.wallet.balance * pct_change

        # 3. Notificar al objeto posición que se cerró
        position.close(exit_price, result)
        
        # 4. Actualizar la wallet con el resultado (WIN/LOSS) y el PnL ($)
        self.wallet.update_balance(result, pnl)
        
        # Remover de la lista de activas
        if position in self.active_positions:
            self.active_positions.remove(position)

    def has_open_position(self, symbol, side):
        """Verifica si existe una posición abierta."""
        for pos in self.active_positions:
            if pos.symbol == symbol and pos.side == side:
                return True
        return False
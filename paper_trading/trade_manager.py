# ==========================================
# TradingBot V4.4.2
# Trade Manager
# ==========================================

"""
Trade Manager

Administra automáticamente las operaciones
abiertas del Paper Trading.

Responsabilidades

- Revisar Stop Loss
- Revisar Take Profit
- Cerrar operaciones
- Actualizar Paper Wallet
- Mantener historial

Utiliza el PaperEngine Singleton.
"""

from paper_trading.paper_engine import PaperEngine


class TradeManager:

    def __init__(self):

        # Singleton compartido
        self.paper = PaperEngine()

    # ======================================
    # Abrir nueva operación
    # ======================================

    def open_trade(
        self,
        symbol,
        side,
        entry,
        quantity,
        stop_loss,
        take_profit
    ):

        return self.paper.open_position(
            symbol=symbol,
            side=side,
            entry=entry,
            quantity=quantity,
            stop_loss=stop_loss,
            take_profit=take_profit
        )

    # ======================================

    def update(self, current_price):

        closed_positions = []

        for index in reversed(range(len(self.paper.positions))):

            position = self.paper.positions[index]

            if position.status != "OPEN":
                continue

            # ================================
            # BUY
            # ================================

            if position.side == "BUY":

                if current_price <= position.stop_loss:

                    trade = self.paper.close_position(
                        index,
                        current_price
                    )

                    closed_positions.append(
                        trade.summary()
                    )

                    continue

                if current_price >= position.take_profit:

                    trade = self.paper.close_position(
                        index,
                        current_price
                    )

                    closed_positions.append(
                        trade.summary()
                    )

                    continue

            # ================================
            # SELL
            # ================================

            else:

                if current_price >= position.stop_loss:

                    trade = self.paper.close_position(
                        index,
                        current_price
                    )

                    closed_positions.append(
                        trade.summary()
                    )

                    continue

                if current_price <= position.take_profit:

                    trade = self.paper.close_position(
                        index,
                        current_price
                    )

                    closed_positions.append(
                        trade.summary()
                    )

                    continue

        return closed_positions

    # ======================================

    def active_positions(self):

        return self.paper.active_positions()

    # ======================================

    def history(self):

        return self.paper.history()

    # ======================================

    def wallet(self):

        return self.paper.wallet.summary()

    # ======================================

    def close_trade(self, index, exit_price):

        return self.paper.close_position(
            index,
            exit_price
        )


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    manager = TradeManager()

    print("===================================")
    print(" TRADE MANAGER ONLINE")
    print("===================================")

    print()

    print("Posiciones activas:")

    print(manager.active_positions())

    print()

    closed = manager.update(70000)

    print("Operaciones cerradas:")

    print(closed)

    print()

    print("Wallet:")

    print(manager.wallet())
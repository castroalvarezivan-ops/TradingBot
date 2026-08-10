# ==========================================
# SECCIÓN: Inicialización y Entorno
# ==========================================

# ==========================================
# TradingBot V5.0
# Paper Engine (Singleton)
# ==========================================

"""
Paper Engine

Motor central del Paper Trading.

Responsabilidades

✔ Singleton
✔ Wallet Persistente
✔ Posiciones Persistentes
✔ Historial Persistente
✔ Recuperación automática
✔ Compatible con Pipeline
✔ Compatible con TradeManager
"""

from paper_trading.paper_wallet import PaperWallet
from paper_trading.paper_position import PaperPosition
from paper_trading.persistence import PersistenceManager


class PaperEngine:

    _instance = None

    # ======================================

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance._initialized = False

        return cls._instance

    # ======================================

    def __init__(self):

        if self._initialized:
            return

        self.wallet = PaperWallet()

        self.positions = []

        self.history_data = []

        self.load_positions()

        self.load_history()

        self._initialized = True

    # ======================================
    # POSITIONS
    # ======================================

    def save_positions(self):

        PersistenceManager.save_positions(
            self.positions
        )

    # ======================================

    def load_positions(self):

        data = PersistenceManager.load_positions()

        if not data:
            return

        self.positions = []

        for p in data:

            position = PaperPosition(

                symbol=p["symbol"],

                side=p["side"],

                entry_price=p["entry"],

                quantity=p["quantity"],

                stop_loss=p["stop_loss"],

                take_profit=p["take_profit"]

            )

            position.status = p["status"]

            position.exit_price = p["exit_price"]

            position.pnl = p["pnl"]

            if "timestamp" in p:

                position.timestamp = p["timestamp"]

            self.positions.append(position)

    # ======================================
    # HISTORY
    # ======================================

    def save_history(self):

        PersistenceManager.save_history(
            self.history_data
        )

    # ======================================

    def load_history(self):

        data = PersistenceManager.load_history()

        if data is None:

            self.history_data = []

        else:

            self.history_data = data


# ==========================================
# SECCIÓN: Lógica Principal
# ==========================================

# ======================================
    # ABRIR POSICIÓN
    # ======================================

    def open_position(

        self,

        symbol,

        side,

        entry,

        quantity,

        stop_loss,

        take_profit

    ):

        position = PaperPosition(

            symbol=symbol,

            side=side,

            entry_price=entry,

            quantity=quantity,

            stop_loss=stop_loss,

            take_profit=take_profit

        )

        self.positions.append(position)

        self.save_positions()

        return position

    # ======================================
    # CERRAR POSICIÓN
    # ======================================

    def close_position(

        self,

        index,

        exit_price

    ):

        position = self.positions[index]

        pnl = position.close(exit_price)

        # Actualizar Wallet

        self.wallet.register_trade(pnl)

        # Guardar en historial

        self.history_data.append(

            position.summary()

        )

        # Eliminar de posiciones activas

        del self.positions[index]

        # Persistencia

        self.save_positions()

        self.save_history()

        return position

    # ======================================
    # POSICIONES ACTIVAS
    # ======================================

    def active_positions(self):

        return [

            p.summary()

            for p in self.positions

            if p.status == "OPEN"

        ]


# ==========================================
# BLOQUE 3
# ==========================================

# ======================================
    # HISTORIAL
    # ======================================

    def history(self):

        return self.history_data

    # ======================================
    # WALLET
    # ======================================

    def wallet_summary(self):

        return self.wallet.summary()


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    engine1 = PaperEngine()

    engine2 = PaperEngine()

    print("===================================")
    print(" PAPER ENGINE V5")
    print("===================================")

    print()

    print("Singleton:", engine1 is engine2)

    print()

    if len(engine1.active_positions()) == 0:

        print("Abriendo operación de prueba...")

        engine1.open_position(

            symbol="BTC/USDT",

            side="BUY",

            entry=65000,

            quantity=0.10,

            stop_loss=64500,

            take_profit=66000

        )

    print()

    print("Posiciones activas:")

    print(engine1.active_positions())

    print()

    print("Historial:")

    print(engine1.history())

    print()

    print("Wallet:")

    print(engine1.wallet_summary())

    print()

    print("===================================")
    print(" Paper Engine funcionando")
    print("===================================")
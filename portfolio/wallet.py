class Wallet:
    def __init__(self, initial_balance=10000):
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.wins = 0
        self.losses = 0
        self.trades = 0

    def update_balance(self, result, pnl):
        """Actualiza el saldo y los contadores de la wallet."""
        self.trades += 1
        
        if result == "WIN":
            self.wins += 1
        elif result == "LOSS":
            self.losses += 1
            
        self.balance += pnl

    @property
    def roi(self):
        """Calcula el Retorno de Inversión porcentual."""
        return ((self.balance - self.initial_balance) / self.initial_balance) * 100

    @property
    def win_rate(self):
        """Calcula el porcentaje de aciertos."""
        if self.trades == 0:
            return 0.0
        return (self.wins / self.trades) * 100

    @property
    def profit_factor(self):
        """Evita errores dividiendo por cero si no hay pérdidas."""
        if self.losses == 0:
            return 0.0
        return self.wins / self.losses
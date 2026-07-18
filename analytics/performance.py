# V2.6.1 STABLE
# Archivo: analytics/performance.py

def calculate_roi(initial, final):
    """Calcula el Retorno sobre la Inversión (ROI) porcentual."""
    if initial == 0:
        return 0
    return ((final - initial) / initial) * 100

def calculate_profit_factor(trades):
    """
    Calcula la relación entre operaciones ganadoras y perdedoras.
    (Nota: Se puede expandir para usar PnL monetario si se integra).
    """
    total_wins = sum(1 for t in trades if t.get('result') == 'WIN')
    total_losses = sum(1 for t in trades if t.get('result') == 'LOSS')
    
    if total_losses == 0:
        return float('inf') if total_wins > 0 else 0
    return total_wins / total_losses

def calculate_max_drawdown(balance_history):
    """Calcula la caída máxima (Max Drawdown) porcentual del balance."""
    if not balance_history:
        return 0
    
    peak = balance_history[0]
    max_dd = 0
    
    for balance in balance_history:
        if balance > peak:
            peak = balance
        # Calculamos la caída desde el pico máximo alcanzado
        dd = (peak - balance) / peak
        if dd > max_dd:
            max_dd = dd
            
    return max_dd * 100
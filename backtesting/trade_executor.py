# V2.6.1 STABLE
# Archivo: backtesting/trade_executor.py

from risk.risk import calculate_risk_parameters

# Número máximo de velas que una operación puede permanecer abierta
MAX_BARS_IN_TRADE = 50

def execute_trade(df, signal_index, action):
    """
    Simula una operación utilizando las velas futuras.
    
    Devuelve:
        result      -> WIN | LOSS | TIMEOUT | OPEN
        exit_price  -> Precio de salida
        bars_held   -> Número de velas que duró la operación
    """

    entry_price = df.iloc[signal_index]["close"]
    atr = df.iloc[signal_index]["atr"]

    stop_loss, take_profit = calculate_risk_parameters(
        entry_price,
        atr,
        action
    )

    bars_held = 0

    # ============================================
    # RECORRER VELAS FUTURAS
    # ============================================

    for i in range(signal_index + 1, len(df)):

        bars_held += 1
        candle = df.iloc[i]
        
        high = candle["high"]
        low = candle["low"]
        close = candle["close"]

        # ============================================
        # COMPRA
        # ============================================
        if action == "BUY":
            # Stop Loss
            if low <= stop_loss:
                return "LOSS", stop_loss, bars_held
            # Take Profit
            if high >= take_profit:
                return "WIN", take_profit, bars_held

        # ============================================
        # VENTA
        # ============================================
        elif action == "SELL":
            # Stop Loss
            if high >= stop_loss:
                return "LOSS", stop_loss, bars_held
            # Take Profit
            if low <= take_profit:
                return "WIN", take_profit, bars_held

        # ============================================
        # TIME STOP
        # ============================================
        if bars_held >= MAX_BARS_IN_TRADE:
            return "TIMEOUT", close, bars_held

    # ============================================
    # SI SE ACABAN LAS VELAS SIN SALIR
    # ============================================
    return "OPEN", entry_price, bars_held
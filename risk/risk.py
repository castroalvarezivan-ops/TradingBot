from config.config import (
    ATR_SL_MULTIPLIER,
    ATR_TP_MULTIPLIER,
    RISK_PER_TRADE
)


def calculate_risk_parameters(entry_price, atr, side="BUY"):
    """
    Calcula Stop Loss y Take Profit utilizando ATR.

    Parámetros:
        entry_price (float): Precio de entrada.
        atr (float): Valor actual del ATR.
        side (str): "BUY" o "SELL".

    Retorna:
        stop_loss, take_profit
    """

    if (
        entry_price is None
        or atr is None
        or entry_price <= 0
        or atr <= 0
    ):
        return None, None

    if side.upper() == "BUY":

        stop_loss = entry_price - (ATR_SL_MULTIPLIER * atr)

        take_profit = entry_price + (ATR_TP_MULTIPLIER * atr)

    else:

        stop_loss = entry_price + (ATR_SL_MULTIPLIER * atr)

        take_profit = entry_price - (ATR_TP_MULTIPLIER * atr)

    return round(stop_loss, 4), round(take_profit, 4)


def calculate_position_size(
    capital_disponible,
    riesgo_porcentaje=RISK_PER_TRADE
):
    """
    Calcula el capital destinado por operación
    según el porcentaje de riesgo configurado.

    Parámetros:
        capital_disponible (float)
        riesgo_porcentaje (float)

    Retorna:
        float
    """

    if capital_disponible <= 0:
        return 0

    return round(
        capital_disponible * riesgo_porcentaje,
        2
    )
import pandas as pd


def calculate_supertrend(df, period=10, multiplier=3):
    """
    Calcula el indicador Supertrend.

    Requiere que el DataFrame ya contenga la columna 'atr',
    calculada previamente por calculate_atr().
    """

    hl2 = (df["high"] + df["low"]) / 2

    atr = df["atr"]

    upperband = hl2 + (multiplier * atr)
    lowerband = hl2 - (multiplier * atr)

    final_upperband = upperband.copy()
    final_lowerband = lowerband.copy()

    supertrend = [True]

    for i in range(1, len(df)):

        # Actualizar bandas
        if upperband.iloc[i] < final_upperband.iloc[i - 1] or df["close"].iloc[i - 1] > final_upperband.iloc[i - 1]:
            final_upperband.iloc[i] = upperband.iloc[i]
        else:
            final_upperband.iloc[i] = final_upperband.iloc[i - 1]

        if lowerband.iloc[i] > final_lowerband.iloc[i - 1] or df["close"].iloc[i - 1] < final_lowerband.iloc[i - 1]:
            final_lowerband.iloc[i] = lowerband.iloc[i]
        else:
            final_lowerband.iloc[i] = final_lowerband.iloc[i - 1]

        # Determinar dirección del Supertrend
        if supertrend[i - 1]:
            if df["close"].iloc[i] < final_lowerband.iloc[i]:
                supertrend.append(False)
            else:
                supertrend.append(True)
        else:
            if df["close"].iloc[i] > final_upperband.iloc[i]:
                supertrend.append(True)
            else:
                supertrend.append(False)

    df["supertrend"] = supertrend
    df["supertrend_upper"] = final_upperband
    df["supertrend_lower"] = final_lowerband

    return df
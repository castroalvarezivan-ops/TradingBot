import pandas as pd


def detect_liquidity(df, tolerance=0.001):
    """
    Detecta zonas de liquidez.

    Busca máximos iguales (Equal Highs)
    y mínimos iguales (Equal Lows).
    """

    df = df.copy()

    df["equal_high"] = False
    df["equal_low"] = False

    for i in range(1, len(df)):

        current_high = df["high"].iloc[i]
        previous_high = df["high"].iloc[i - 1]

        current_low = df["low"].iloc[i]
        previous_low = df["low"].iloc[i - 1]

        # Equal High
        if abs(current_high - previous_high) / previous_high < tolerance:
            df.loc[df.index[i], "equal_high"] = True

        # Equal Low
        if abs(current_low - previous_low) / previous_low < tolerance:
            df.loc[df.index[i], "equal_low"] = True

    return df
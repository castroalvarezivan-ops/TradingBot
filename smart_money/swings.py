import pandas as pd


def detect_swings(df, left=3, right=3):
    """
    Detecta Swing Highs y Swing Lows.

    Un Swing High es un máximo mayor que las velas
    anteriores y posteriores.

    Un Swing Low es un mínimo menor que las velas
    anteriores y posteriores.
    """

    df = df.copy()

    df["swing_high"] = False
    df["swing_low"] = False

    highs = df["high"].values
    lows = df["low"].values

    for i in range(left, len(df) - right):

        # ---------- Swing High ----------

        current_high = highs[i]

        previous_highs = highs[i-left:i]
        next_highs = highs[i+1:i+right+1]

        if (
            current_high > max(previous_highs)
            and current_high > max(next_highs)
        ):

            df.loc[df.index[i], "swing_high"] = True

        # ---------- Swing Low ----------

        current_low = lows[i]

        previous_lows = lows[i-left:i]
        next_lows = lows[i+1:i+right+1]

        if (
            current_low < min(previous_lows)
            and current_low < min(next_lows)
        ):

            df.loc[df.index[i], "swing_low"] = True

    return df
import pandas as pd


def detect_swings_v2(df, left=3, right=3):
    """
    Detecta Swing Highs y Swing Lows.

    Además guarda:

    - swing_price
    - swing_type
    - swing_index
    """

    df = df.copy()

    df["swing_high"] = False
    df["swing_low"] = False

    df["swing_price"] = None
    df["swing_type"] = None
    df["swing_index"] = None

    highs = df["high"].values
    lows = df["low"].values

    for i in range(left, len(df) - right):

        current_high = highs[i]
        current_low = lows[i]

        # -----------------------
        # Swing High
        # -----------------------

        if (
            current_high > max(highs[i-left:i])
            and current_high > max(highs[i+1:i+right+1])
        ):

            df.loc[df.index[i], "swing_high"] = True
            df.loc[df.index[i], "swing_price"] = current_high
            df.loc[df.index[i], "swing_type"] = "HIGH"
            df.loc[df.index[i], "swing_index"] = i

        # -----------------------
        # Swing Low
        # -----------------------

        elif (
            current_low < min(lows[i-left:i])
            and current_low < min(lows[i+1:i+right+1])
        ):

            df.loc[df.index[i], "swing_low"] = True
            df.loc[df.index[i], "swing_price"] = current_low
            df.loc[df.index[i], "swing_type"] = "LOW"
            df.loc[df.index[i], "swing_index"] = i

    return df
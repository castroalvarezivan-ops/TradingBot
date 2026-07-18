import pandas as pd


def detect_market_structure_v2(df):
    """
    Construye la estructura del mercado utilizando
    únicamente Swing Highs y Swing Lows.

    Devuelve:

        HH
        HL
        LH
        LL
        RANGE
    """

    df = df.copy()

    df["market_structure"] = "RANGE"

    last_high = None
    last_low = None

    for i in range(len(df)):

        # ======================
        # NUEVO SWING HIGH
        # ======================

        if df.loc[df.index[i], "swing_high"]:

            current = df.loc[df.index[i], "high"]

            if last_high is None:

                last_high = current

            else:

                if current > last_high:

                    df.loc[df.index[i], "market_structure"] = "HH"

                else:

                    df.loc[df.index[i], "market_structure"] = "LH"

                last_high = current

        # ======================
        # NUEVO SWING LOW
        # ======================

        elif df.loc[df.index[i], "swing_low"]:

            current = df.loc[df.index[i], "low"]

            if last_low is None:

                last_low = current

            else:

                if current > last_low:

                    df.loc[df.index[i], "market_structure"] = "HL"

                else:

                    df.loc[df.index[i], "market_structure"] = "LL"

                last_low = current

    return df
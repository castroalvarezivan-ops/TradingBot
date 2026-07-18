import pandas as pd


def detect_market_structure(df):
    """
    Construye la estructura del mercado utilizando los Swing High
    y Swing Low detectados previamente.

    Estados posibles:

        HH = Higher High
        HL = Higher Low
        LH = Lower High
        LL = Lower Low
        RANGE = Sin estructura definida

    Requiere que previamente existan:

        swing_high
        swing_low
    """

    df = df.copy()

    df["market_structure"] = "RANGE"

    last_swing_high = None
    last_swing_low = None

    for i in range(len(df)):

        # ----------------------------
        # SWING HIGH
        # ----------------------------

        if df.loc[df.index[i], "swing_high"]:

            current_high = df.loc[df.index[i], "high"]

            if last_swing_high is None:

                structure = "HH"

            else:

                if current_high > last_swing_high:
                    structure = "HH"
                else:
                    structure = "LH"

            df.loc[df.index[i], "market_structure"] = structure

            last_swing_high = current_high

        # ----------------------------
        # SWING LOW
        # ----------------------------

        elif df.loc[df.index[i], "swing_low"]:

            current_low = df.loc[df.index[i], "low"]

            if last_swing_low is None:

                structure = "LL"

            else:

                if current_low < last_swing_low:
                    structure = "LL"
                else:
                    structure = "HL"

            df.loc[df.index[i], "market_structure"] = structure

            last_swing_low = current_low

    return df
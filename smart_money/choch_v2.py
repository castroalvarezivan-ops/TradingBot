import pandas as pd


def detect_choch_v2(df):
    """
    Detecta Change Of Character (CHoCH)
    utilizando la estructura del mercado V2.

    Devuelve:

        bullish
        bearish
        None
    """

    df = df.copy()

    df["choch"] = None

    previous_structure = "RANGE"

    for i in range(len(df)):

        current = df.loc[df.index[i], "market_structure"]

        # ==========================
        # CHOCH ALCISTA
        # ==========================

        if previous_structure == "LL" and current == "HL":

            df.loc[df.index[i], "choch"] = "bullish"

        elif previous_structure == "LH" and current == "HH":

            df.loc[df.index[i], "choch"] = "bullish"

        # ==========================
        # CHOCH BAJISTA
        # ==========================

        elif previous_structure == "HH" and current == "LH":

            df.loc[df.index[i], "choch"] = "bearish"

        elif previous_structure == "HL" and current == "LL":

            df.loc[df.index[i], "choch"] = "bearish"

        if current != "RANGE":
            previous_structure = current

    return df
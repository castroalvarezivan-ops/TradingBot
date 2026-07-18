import pandas as pd


def detect_bos_v2(df):
    """
    Detecta Break Of Structure (BOS)
    utilizando la estructura del mercado V2.

    Devuelve:

        bullish
        bearish
        None
    """

    df = df.copy()

    df["bos"] = None

    previous_structure = "RANGE"

    for i in range(len(df)):

        current = df.loc[df.index[i], "market_structure"]

        # ==========================
        # BOS ALCISTA
        # ==========================

        if previous_structure == "HL" and current == "HH":

            df.loc[df.index[i], "bos"] = "bullish"

        # ==========================
        # BOS BAJISTA
        # ==========================

        elif previous_structure == "LH" and current == "LL":

            df.loc[df.index[i], "bos"] = "bearish"

        if current != "RANGE":
            previous_structure = current

    return df
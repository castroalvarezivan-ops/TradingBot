import pandas as pd


def detect_choch(df):
    """
    Detecta Change Of Character (CHoCH).

    Un CHoCH ocurre cuando el mercado cambia
    de una estructura alcista a bajista
    o viceversa.
    """

    df = df.copy()

    df["choch"] = None

    previous_structure = "RANGE"

    for i in range(len(df)):

        current_structure = df.loc[df.index[i], "market_structure"]

        # ======================
        # CHoCH ALCISTA
        # ======================

        if (
            previous_structure in ["LL", "LH"]
            and current_structure in ["HL", "HH"]
        ):

            df.loc[df.index[i], "choch"] = "bullish"

        # ======================
        # CHoCH BAJISTA
        # ======================

        elif (
            previous_structure in ["HH", "HL"]
            and current_structure in ["LH", "LL"]
        ):

            df.loc[df.index[i], "choch"] = "bearish"

        previous_structure = current_structure

    return df
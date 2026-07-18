import pandas as pd


def detect_bos(df):
    """
    Detecta Break Of Structure (BOS).

    Un BOS alcista ocurre cuando la estructura rompe
    hacia un nuevo HH.

    Un BOS bajista ocurre cuando la estructura rompe
    hacia un nuevo LL.
    """

    df = df.copy()

    df["bos"] = None

    previous_structure = "RANGE"

    for i in range(len(df)):

        current_structure = df.loc[df.index[i], "market_structure"]

        # ======================
        # BOS ALCISTA
        # ======================

        if (
            previous_structure in ["HL", "LH", "LL"]
            and current_structure == "HH"
        ):

            df.loc[df.index[i], "bos"] = "bullish"

        # ======================
        # BOS BAJISTA
        # ======================

        elif (
            previous_structure in ["HH", "HL", "LH"]
            and current_structure == "LL"
        ):

            df.loc[df.index[i], "bos"] = "bearish"

        previous_structure = current_structure

    return df
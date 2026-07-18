import pandas as pd


def detect_fair_value_gap(df):
    """
    Detecta Fair Value Gaps (FVG).

    Un FVG alcista ocurre cuando el mínimo de la vela
    actual está por encima del máximo de hace dos velas.

    Un FVG bajista ocurre cuando el máximo de la vela
    actual está por debajo del mínimo de hace dos velas.
    """

    df = df.copy()

    df["bullish_fvg"] = False
    df["bearish_fvg"] = False

    for i in range(2, len(df)):

        # Bullish FVG
        if df["low"].iloc[i] > df["high"].iloc[i - 2]:
            df.loc[df.index[i], "bullish_fvg"] = True

        # Bearish FVG
        elif df["high"].iloc[i] < df["low"].iloc[i - 2]:
            df.loc[df.index[i], "bearish_fvg"] = True

    return df
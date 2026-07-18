import pandas as pd


def detect_order_blocks(df):
    """
    Detecta posibles Order Blocks.

    Un Order Block alcista es una vela bajista
    seguida por una vela alcista fuerte.

    Un Order Block bajista es una vela alcista
    seguida por una vela bajista fuerte.
    """

    df = df.copy()

    df["bullish_ob"] = False
    df["bearish_ob"] = False

    for i in range(1, len(df)):

        previous = df.iloc[i - 1]
        current = df.iloc[i]

        # Bullish Order Block
        if (
            previous["close"] < previous["open"]
            and current["close"] > current["open"]
            and current["close"] > previous["high"]
        ):
            df.loc[df.index[i], "bullish_ob"] = True

        # Bearish Order Block
        elif (
            previous["close"] > previous["open"]
            and current["close"] < current["open"]
            and current["close"] < previous["low"]
        ):
            df.loc[df.index[i], "bearish_ob"] = True

    return df
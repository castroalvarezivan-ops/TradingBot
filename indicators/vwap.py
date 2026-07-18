import pandas as pd


def calculate_vwap(df):
    """
    Calcula el VWAP (Volume Weighted Average Price).
    """

    typical_price = (
        df["high"] +
        df["low"] +
        df["close"]
    ) / 3

    cumulative_tp_volume = (
        typical_price * df["volume"]
    ).cumsum()

    cumulative_volume = (
        df["volume"]
    ).cumsum()

    df["vwap"] = (
        cumulative_tp_volume /
        cumulative_volume
    )

    return df
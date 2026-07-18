import pandas as pd
import numpy as np


def calculate_adx(df, period=14):
    """
    Calcula el Average Directional Index (ADX).
    """

    high = df["high"]
    low = df["low"]
    close = df["close"]

    plus_dm = high.diff()
    minus_dm = -low.diff()

    plus_dm = np.where(
        (plus_dm > minus_dm) & (plus_dm > 0),
        plus_dm,
        0
    )

    minus_dm = np.where(
        (minus_dm > plus_dm) & (minus_dm > 0),
        minus_dm,
        0
    )

    tr1 = high - low
    tr2 = abs(high - close.shift())
    tr3 = abs(low - close.shift())

    tr = pd.concat(
        [
            tr1,
            tr2,
            tr3
        ],
        axis=1
    ).max(axis=1)

    atr = tr.rolling(period).mean()

    plus_di = 100 * (
        pd.Series(plus_dm).rolling(period).mean() / atr
    )

    minus_di = 100 * (
        pd.Series(minus_dm).rolling(period).mean() / atr
    )

    dx = (
        abs(plus_di - minus_di)
        /
        (plus_di + minus_di)
    ) * 100

    df["adx"] = dx.rolling(period).mean()

    return df
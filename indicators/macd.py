import pandas as pd


def calculate_macd(
    df,
    fast_period=12,
    slow_period=26,
    signal_period=9
):
    """
    Calcula el indicador MACD.
    """

    ema_fast = df['close'].ewm(
        span=fast_period,
        adjust=False
    ).mean()

    ema_slow = df['close'].ewm(
        span=slow_period,
        adjust=False
    ).mean()

    df['macd'] = ema_fast - ema_slow

    df['macd_signal'] = df['macd'].ewm(
        span=signal_period,
        adjust=False
    ).mean()

    df['macd_histogram'] = (
        df['macd'] - df['macd_signal']
    )

    return df
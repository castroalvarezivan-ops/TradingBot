import pandas as pd


def check_trend(df):
    """
    Evalúa la tendencia usando las EMAs.
    """

    latest = df.iloc[-1]

    if latest["ema_9"] > latest["ema_21"] > latest["ema_50"]:
        return "BULLISH"

    elif latest["ema_9"] < latest["ema_21"] < latest["ema_50"]:
        return "BEARISH"

    return "SIDEWAYS"


def analyze_multi_timeframe(
    df_4h,
    df_1h,
    df_15m,
    df_5m
):
    """
    Analiza la tendencia en múltiples temporalidades.
    """

    trend_4h = check_trend(df_4h)
    trend_1h = check_trend(df_1h)
    trend_15m = check_trend(df_15m)
    trend_5m = check_trend(df_5m)

    bullish = (
        trend_4h == "BULLISH"
        and trend_1h == "BULLISH"
        and trend_15m == "BULLISH"
    )

    bearish = (
        trend_4h == "BEARISH"
        and trend_1h == "BEARISH"
        and trend_15m == "BEARISH"
    )

    return {
        "4H": trend_4h,
        "1H": trend_1h,
        "15M": trend_15m,
        "5M": trend_5m,
        "bullish": bullish,
        "bearish": bearish
    }
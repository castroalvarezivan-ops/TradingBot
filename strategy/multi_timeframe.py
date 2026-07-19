# ==========================================
# TradingBot V2.9.1
# Archivo: strategy/multi_timeframe.py
# ==========================================

"""
Multi Timeframe Engine

Evalúa la tendencia institucional en múltiples
temporalidades utilizando las EMAs.

Este módulo NO toma decisiones.

Únicamente informa el estado de cada timeframe
para que el Decision Engine pueda utilizarlo.
"""


def check_trend(df):
    """
    Determina la tendencia usando EMAs.
    """

    if df is None or len(df) == 0:
        return "UNKNOWN"

    latest = df.iloc[-1]

    ema9 = latest["ema_9"]
    ema21 = latest["ema_21"]
    ema50 = latest["ema_50"]

    if ema9 > ema21 > ema50:
        return "BULLISH"

    elif ema9 < ema21 < ema50:
        return "BEARISH"

    return "SIDEWAYS"


def analyze_multi_timeframe(
    df_4h,
    df_1h,
    df_15m,
    df_5m,
):
    """
    Analiza la tendencia de todas las temporalidades.
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

    alignment = 0

    for trend in (
        trend_4h,
        trend_1h,
        trend_15m,
        trend_5m,
    ):
        if trend == "BULLISH":
            alignment += 25
        elif trend == "BEARISH":
            alignment += 25

    return {

        "4H": trend_4h,

        "1H": trend_1h,

        "15M": trend_15m,

        "5M": trend_5m,

        "bullish": bullish,

        "bearish": bearish,

        "alignment": alignment

    }
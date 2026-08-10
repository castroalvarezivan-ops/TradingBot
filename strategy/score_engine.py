# ==========================================
# TradingBot Executive V8
# strategy/score_engine.py
# ==========================================

"""
Score Engine Institucional

Calcula el Score IA (0-100)
utilizado por Decision Engine.
"""

MAX_SCORE = 100


def calculate_score(latest):

    score = 0
    reasons = []

    # =====================================
    # EMA
    # =====================================

    if latest["ema_9"] > latest["ema_21"] > latest["ema_50"]:
        score += 15
        reasons.append("EMAs Alcistas")

    elif latest["ema_9"] < latest["ema_21"] < latest["ema_50"]:
        score -= 15
        reasons.append("EMAs Bajistas")

    # =====================================
    # RSI
    # =====================================

    rsi = latest["rsi"]

    if 50 <= rsi <= 65:
        score += 10
        reasons.append("RSI Saludable")

    elif rsi < 30:
        score += 8
        reasons.append("Sobreventa")

    elif rsi > 75:
        score -= 8
        reasons.append("Sobrecompra")

    # =====================================
    # MACD
    # =====================================

    if latest["macd"] > latest["macd_signal"]:
        score += 10
        reasons.append("MACD Bullish")

    else:
        score -= 10
        reasons.append("MACD Bearish")

    # =====================================
    # ADX
    # =====================================

    adx = latest["adx"]

    if adx >= 30:
        score += 8
        reasons.append("ADX Alto")

    elif adx < 20:
        score -= 5
        reasons.append("Mercado Lateral")

    # =====================================
    # SUPERTREND
    # =====================================

    if latest["supertrend"]:
        score += 8
        reasons.append("Supertrend")

    else:
        score -= 8
        reasons.append("Supertrend Bajista")

    # =====================================
    # VOLUMEN
    # =====================================

    if latest["volume"] > latest["vol_sma"] * 1.5:
        score += 10
        reasons.append("Volumen Institucional")

    # =====================================
    # BOS
    # =====================================

    if latest["bos"] == "bullish":
        score += 10
        reasons.append("Bullish BOS")

    elif latest["bos"] == "bearish":
        score -= 10
        reasons.append("Bearish BOS")

    # =====================================
    # CHOCH
    # =====================================

    if latest["choch"] == "bullish":
        score += 10
        reasons.append("Bullish CHOCH")

    elif latest["choch"] == "bearish":
        score -= 10
        reasons.append("Bearish CHOCH")

    # =====================================
    # ORDER BLOCK
    # =====================================

    if latest["bullish_ob"]:
        score += 8
        reasons.append("Bullish OB")

    if latest["bearish_ob"]:
        score -= 8
        reasons.append("Bearish OB")

    # =====================================
    # FAIR VALUE GAP
    # =====================================

    if latest["bullish_fvg"]:
        score += 6
        reasons.append("Bullish FVG")

    if latest["bearish_fvg"]:
        score -= 6
        reasons.append("Bearish FVG")

    # =====================================
    # LIQUIDEZ
    # =====================================

    if latest["equal_high"]:
        score += 5
        reasons.append("Equal High")

    if latest["equal_low"]:
        score += 5
        reasons.append("Equal Low")

    # =====================================
    # NORMALIZACIÓN
    # =====================================

    score = max(min(score, MAX_SCORE), -MAX_SCORE)

    institutional_score = int((score + MAX_SCORE) / 2)

    return institutional_score, reasons


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    print("===================================")
    print(" SCORE ENGINE V8")
    print("===================================")
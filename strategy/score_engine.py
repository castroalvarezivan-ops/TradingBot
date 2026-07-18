def calculate_score(latest):
    """
    Calcula el score institucional.
    """

    score = 0
    reasons = []

    # ==========================
    # EMA
    # ==========================

    if latest["ema_9"] > latest["ema_21"] > latest["ema_50"]:
        score += 40
        reasons.append("EMAs Alcistas")

    elif latest["ema_9"] < latest["ema_21"] < latest["ema_50"]:
        score -= 40
        reasons.append("EMAs Bajistas")

    # ==========================
    # RSI
    # ==========================

    if 40 <= latest["rsi"] <= 65:
        score += 25
        reasons.append("RSI Saludable")

    elif latest["rsi"] < 30:
        score += 20
        reasons.append("RSI Sobreventa")

    elif latest["rsi"] > 75:
        score -= 20
        reasons.append("RSI Sobrecompra")

    # ==========================
    # MACD
    # ==========================

    if latest["macd"] > latest["macd_signal"]:
        score += 25
        reasons.append("MACD Alcista")
    else:
        score -= 25
        reasons.append("MACD Bajista")

    # ==========================
    # ADX
    # ==========================

    if latest["adx"] >= 30:
        score += 20
        reasons.append("ADX Tendencia Fuerte")

    elif latest["adx"] < 20:
        score -= 15
        reasons.append("ADX Mercado Lateral")

    # ==========================
    # SUPERTREND
    # ==========================

    if latest["supertrend"]:
        score += 20
        reasons.append("Supertrend Alcista")
    else:
        score -= 20
        reasons.append("Supertrend Bajista")

    # ==========================
    # VOLUMEN
    # ==========================

    if latest["volume"] > latest["vol_sma"] * 1.5:
        score += 35
        reasons.append("Volumen Institucional")

    # ==========================
    # BOS DIRECCIONAL
    # ==========================

    if latest["bos"] == "bullish":
        score += 25
        reasons.append("Bullish BOS")

    elif latest["bos"] == "bearish":
        score -= 25
        reasons.append("Bearish BOS")

    # ==========================
    # CHOCH DIRECCIONAL
    # ==========================

    if latest["choch"] == "bullish":
        score += 30
        reasons.append("Bullish CHoCH")

    elif latest["choch"] == "bearish":
        score -= 30
        reasons.append("Bearish CHoCH")

    # ==========================
    # LIQUIDEZ
    # ==========================

    if latest["equal_high"]:
        score += 10
        reasons.append("Equal High")

    if latest["equal_low"]:
        score += 10
        reasons.append("Equal Low")

    # ==========================
    # ORDER BLOCKS
    # ==========================

    if latest["bullish_ob"]:
        score += 25
        reasons.append("Bullish Order Block")

    if latest["bearish_ob"]:
        score -= 25
        reasons.append("Bearish Order Block")

    # ==========================
    # FAIR VALUE GAP
    # ==========================

    if latest["bullish_fvg"]:
        score += 20
        reasons.append("Bullish FVG")

    if latest["bearish_fvg"]:
        score -= 20
        reasons.append("Bearish FVG")

    return score, reasons
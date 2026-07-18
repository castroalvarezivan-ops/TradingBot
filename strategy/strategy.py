# V2.6.1 STABLE
# Archivo: strategy/strategy.py

import pandas as pd
import numpy as np

# ==========================
# INDICADORES
# ==========================
from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd
from indicators.atr import calculate_atr
from indicators.adx import calculate_adx
from indicators.vwap import calculate_vwap
from indicators.supertrend import calculate_supertrend

# ==========================
# SMART MONEY
# ==========================
from smart_money.swings import detect_swings
from smart_money.market_structure import detect_market_structure
from smart_money.bos import detect_bos
from smart_money.choch import detect_choch
from smart_money.swings_v2 import detect_swings_v2
from smart_money.market_structure_v2 import detect_market_structure_v2
from smart_money.bos_v2 import detect_bos_v2
from smart_money.choch_v2 import detect_choch_v2
from smart_money.liquidity import detect_liquidity
from smart_money.order_blocks import detect_order_blocks
from smart_money.fair_value_gap import detect_fair_value_gap
from config.config import USE_SMART_MONEY_V2

# ==========================
# DECISION ENGINE
# ==========================
from strategy.decision_engine import evaluate

def calculate_indicators(df):
    """
    Calcula TODOS los indicadores una sola vez.
    Optimizado para pre-procesamiento en Backtesting o escaneo en vivo.
    """
    if df is None or len(df) < 50:
        return None

    df = df.copy()

    # Indicadores Técnicos
    df = calculate_ema(df)
    df = calculate_rsi(df)
    df = calculate_macd(df)
    df = calculate_atr(df)
    df = calculate_adx(df)
    df = calculate_vwap(df)
    df = calculate_supertrend(df)

    # Smart Money
    if USE_SMART_MONEY_V2:
        df = detect_swings_v2(df)
        df = detect_market_structure_v2(df)
        df = detect_bos_v2(df)
        df = detect_choch_v2(df)
    else:
        df = detect_swings(df)
        df = detect_market_structure(df)
        df = detect_bos(df)
        df = detect_choch(df)

    df = detect_liquidity(df)
    df = detect_order_blocks(df)
    df = detect_fair_value_gap(df)

    # Volumen SMA
    df["vol_sma"] = df["volume"].rolling(window=20).mean()

    return df

def evaluate_market_condition(df):
    """
    Uso: Live Scanning.
    Calcula indicadores y evalúa inmediatamente.
    """
    df_processed = calculate_indicators(df)
    if df_processed is None:
        return "HOLD", 0, "Datos insuficientes"
    
    return evaluate(df_processed.iloc[-1])

def evaluate_market_condition_precalculated(latest):
    """
    Uso: Backtesting.
    Evalúa una fila que ya tiene indicadores calculados.
    """
    return evaluate(latest)
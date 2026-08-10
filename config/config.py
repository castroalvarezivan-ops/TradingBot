# ==========================================
# TradingBot V8
# config/config.py
# Configuración Global
# ==========================================

import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# BINANCE
# ==========================================

API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# ==========================================
# MERCADO
# ==========================================

SYMBOLS = [
    "BTC/USDT",
    "ETH/USDT",
    "SOL/USDT",
    "BNB/USDT",
    "ADA/USDT"
]

TIMEFRAME = "15m"

# ==========================================
# CAPITAL
# ==========================================

INITIAL_CAPITAL = 1000

# Riesgo por operación
RISK_PER_TRADE = 0.01

# Compatibilidad con Risk Engine
MAX_RISK_PER_TRADE = RISK_PER_TRADE

# ==========================================
# ATR
# ==========================================

ATR_SL_MULTIPLIER = 2.0
ATR_TP_MULTIPLIER = 4.0

# ==========================================
# TRADES
# ==========================================

MAX_OPEN_TRADES = 1

COMMISSION = 0.001
SLIPPAGE = 0.0005

# ==========================================
# SMART MONEY
# ==========================================

USE_SMART_MONEY_V2 = True

# ==========================================
# DECISION ENGINE
# ==========================================

BUY_THRESHOLD = 50
SELL_THRESHOLD = -50

# ==========================================
# CONFIDENCE ENGINE
# ==========================================

ENABLE_CONFIDENCE_ENGINE = True

# ==========================================
# DEBUG
# ==========================================

DEBUG_MODE = True
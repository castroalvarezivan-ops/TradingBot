import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# Parámetros globales del sistema
SYMBOLS = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT', 'ADA/USDT']
TIMEFRAME = '15m'

# ===========================================
# BACKTEST
# ===========================================

INITIAL_CAPITAL = 1000

RISK_PER_TRADE = 0.01

ATR_SL_MULTIPLIER = 2.0

ATR_TP_MULTIPLIER = 4.0

MAX_OPEN_TRADES = 1

COMMISSION = 0.001      # 0.1%

SLIPPAGE = 0.0005       # 0.05%

# =====================================
# SMART MONEY ENGINE
# =====================================

USE_SMART_MONEY_V2 = True

# ==========================================
# DECISION ENGINE
# ==========================================

BUY_THRESHOLD = 50
SELL_THRESHOLD = -50

# ==========================================
# DEBUG
# ==========================================

DEBUG_MODE = True

# ==========================================
# CONFIDENCE ENGINE
# ==========================================

ENABLE_CONFIDENCE_ENGINE = True
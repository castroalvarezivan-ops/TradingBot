import ccxt
import pandas as pd
from config.config import API_KEY, SECRET_KEY, TIMEFRAME, SYMBOLS


def get_exchange():
    """
    Inicializa la conexión con Binance.
    """
    return ccxt.binance({
        "apiKey": API_KEY,
        "secret": SECRET_KEY,
        "enableRateLimit": True,
        "options": {
            "defaultType": "spot"
        }
    })


# ==========================================
# Símbolos dinámicos
# ==========================================

def get_dynamic_symbols(limit=100):
    """
    Obtiene dinámicamente los pares con mayor
    volumen negociado en USDT.
    """

    try:

        exchange = get_exchange()

        tickers = exchange.fetch_tickers()

        usdt_tickers = {

            symbol: data

            for symbol, data in tickers.items()

            if symbol.endswith("/USDT")

            and data.get("quoteVolume") is not None

        }

        sorted_tickers = sorted(

            usdt_tickers.items(),

            key=lambda x: x[1]["quoteVolume"],

            reverse=True

        )

        top_symbols = [

            item[0]

            for item in sorted_tickers[:limit]

        ]

        return top_symbols

    except Exception as e:

        print(

            f"Error obteniendo símbolos dinámicos: {e}"

        )

        return SYMBOLS


# ==========================================
# Descargar velas
# ==========================================

def fetch_candles(

    symbol,

    timeframe=None,

    limit=1000

):
    """
    Descarga velas OHLCV.

    Compatible con:

    - Pipeline Engine
    - Backtesting Engine
    """

    try:

        exchange = get_exchange()

        if timeframe is None:

            timeframe = TIMEFRAME

        ohlcv = exchange.fetch_ohlcv(

            symbol,

            timeframe,

            limit=limit

        )

        df = pd.DataFrame(

            ohlcv,

            columns=[

                "timestamp",

                "open",

                "high",

                "low",

                "close",

                "volume"

            ]

        )

        df["timestamp"] = pd.to_datetime(

            df["timestamp"],

            unit="ms"

        )

        return df

    except Exception as e:

        print(

            f"Error descargando velas para {symbol}: {e}"

        )

        return None


# ==========================================
# Precio actual
# ==========================================

def get_current_price(symbol):
    """
    Obtiene el último precio del mercado.
    """

    try:

        exchange = get_exchange()

        ticker = exchange.fetch_ticker(symbol)

        return ticker["last"]

    except Exception as e:

        print(

            f"Error obteniendo precio de {symbol}: {e}"

        )

        return None


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    print("===================================")
    print(" SCANNER V5")
    print("===================================")

    print()

    symbols = get_dynamic_symbols(10)

    print("Top símbolos:")

    print(symbols)

    print()

    df = fetch_candles(

        "BTC/USDT",

        timeframe="15m",

        limit=5

    )

    print(df)

    print()

    print(

        "Precio:",

        get_current_price("BTC/USDT")

    )
import ccxt
import pandas as pd
from config.config import API_KEY, SECRET_KEY, TIMEFRAME, SYMBOLS

def get_exchange():
    """Inicializa la conexión con Binance."""
    return ccxt.binance({
        'apiKey': API_KEY,
        'secret': SECRET_KEY,
        'enableRateLimit': True,
        'options': {'defaultType': 'spot'}
    })

def get_dynamic_symbols(limit=100):
    """Obtiene dinámicamente los pares con mayor volumen en USDT en tiempo real."""
    try:
        exchange = get_exchange()
        tickers = exchange.fetch_tickers()
        
        # Filtramos solo los pares contra USDT que tengan volumen activo
        usdt_tickers = {
            symbol: data for symbol, data in tickers.items() 
            if symbol.endswith('/USDT') and data.get('quoteVolume') is not None
        }
        
        # Ordenamos de mayor a menor volumen (dinero real moviéndose)
        sorted_tickers = sorted(usdt_tickers.items(), key=lambda x: x[1]['quoteVolume'], reverse=True)
        
        # Extraemos los mejores 'limit' pares
        top_symbols = [item[0] for item in sorted_tickers[:limit]]
        return top_symbols
    except Exception as e:
        print(f"Error obteniendo volumenes dinámicos de Binance, usando lista base: {e}")
        return SYMBOLS

def fetch_candles(symbol):
    """Descarga el historial de velas (OHLCV) para un símbolo dado."""
    try:
        exchange = get_exchange()
        ohlcv = exchange.fetch_ohlcv(symbol, TIMEFRAME, limit=1000)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"Error en scanner para {symbol}: {e}")
        return None

def get_current_price(symbol):
    """Obtiene el precio actual de mercado para un símbolo."""
    try:
        exchange = get_exchange()
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        print(f"Error obteniendo precio de {symbol}: {e}")
        return None
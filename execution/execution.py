import ccxt
from config.config import API_KEY, SECRET_KEY

def get_exchange_client():
    """Inicializa el cliente de Binance para ejecución."""
    return ccxt.binance({
        'apiKey': API_KEY,
        'secret': SECRET_KEY,
        'enableRateLimit': True,
        'options': {'defaultType': 'spot'}
    })

def get_balance():
    """Obtiene el balance de USDT disponible y total en la cuenta."""
    try:
        exchange = get_exchange_client()
        balance = exchange.fetch_balance()
        free_usdt = balance['free'].get('USDT', 0.0)
        total_usdt = balance['total'].get('USDT', 0.0)
        return free_usdt, total_usdt
    except Exception as e:
        print(f"Error obteniendo balance: {e}")
        return 0.0, 0.0

def place_market_order(symbol, side, amount_usdt):
    """Ejecuta una orden a mercado en Binance Spot basada en USDT."""
    try:
        exchange = get_exchange_client()
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        
        # Calcula la cantidad exacta de la criptomoneda según el USDT destinado
        amount_coin = amount_usdt / price
        
        if side.upper() == 'BUY':
            order = exchange.create_market_buy_order(symbol, amount_coin)
            print(f"[EJECUCIÓN] COMPRA exitosa de {symbol} por {amount_usdt} USDT")
            return order
        elif side.upper() == 'SELL':
            order = exchange.create_market_sell_order(symbol, amount_coin)
            print(f"[EJECUCIÓN] VENTA exitosa de {symbol}")
            return order
    except Exception as e:
        print(f"[ERROR EJECUCIÓN] No se pudo procesar la orden para {symbol}: {e}")
        return None
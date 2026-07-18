import ccxt
import pandas as pd
import os

def download_data():
    # Inicializar exchange público
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    timeframe = '1h'
    limit = 500  # Descarga 500 horas de datos

    print(f"Descargando {limit} velas de {symbol}...")
    
    # Obtener datos
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    
    # Crear DataFrame
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    # Formatear fecha
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Guardar en database/data.csv
    if not os.path.exists('database'):
        os.makedirs('database')
        
    df.to_csv('database/data.csv', index=False)
    print(f"Éxito: Archivo guardado en database/data.csv con {len(df)} filas.")

if __name__ == "__main__":
    download_data()
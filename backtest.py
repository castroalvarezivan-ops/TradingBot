import pandas as pd
from backtesting.engine import run_backtest

def main():
    # 1. Cargar datos
    try:
        df = pd.read_csv("database/data.csv")
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'database/data.csv'")
        return

    # 2. Ejecutar el motor de backtesting
    # El engine ahora se encarga de todo: procesar, calcular y mostrar el reporte final
    print("Iniciando Backtest V2.6.1...")
    run_backtest(df)

if __name__ == "__main__":
    main()
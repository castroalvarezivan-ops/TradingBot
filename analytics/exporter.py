# ==========================================
# TradingBot V2.6.2
# Archivo: analytics/exporter.py
# ==========================================

import os
import pandas as pd
from datetime import datetime


def export_trades(trades, folder="reports/exports"):
    """
    Exporta el historial completo de operaciones a un archivo CSV.

    Parámetros:
        trades (list): Lista de diccionarios con las operaciones.
        folder (str): Carpeta donde se guardará el archivo.

    Retorna:
        str | None: Ruta del archivo generado o None si no hay operaciones.
    """

    if not trades:
        print("⚠ No existen operaciones para exportar.")
        return None

    # Crear carpeta automáticamente si no existe
    os.makedirs(folder, exist_ok=True)

    # Nombre único basado en fecha y hora
    filename = datetime.now().strftime(
        "trades_%Y%m%d_%H%M%S.csv"
    )

    filepath = os.path.join(folder, filename)

    # Convertir a DataFrame
    df = pd.DataFrame(trades)

    # Exportar CSV
    df.to_csv(
        filepath,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n========================================")
    print("✅ HISTORIAL EXPORTADO")
    print("========================================")
    print(filepath)
    print("========================================")

    return filepath
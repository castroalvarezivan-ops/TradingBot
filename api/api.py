from flask import Flask, render_template, jsonify, request

from config.config import SYMBOLS
from scanner.scanner import (
    get_dynamic_symbols,
    fetch_candles,
    get_current_price
)

from strategy.strategy import (
    calculate_indicators,
    evaluate_market_condition
)

from risk.risk import calculate_risk_parameters
from execution.execution import get_balance, place_market_order

print("***** ESTE ES MI API.PY *****")

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

bot_status = {
    "active_signals": []
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/balance', methods=['GET'])
def api_balance():

    free, total = get_balance()

    return jsonify({
        "free": free,
        "total": total
    })


@app.route('/api/scan', methods=['POST'])
def api_scan():

    print("\n***** API_SCAN EJECUTÁNDOSE *****")

    data = request.json or {}

    use_dynamic = data.get("dynamic", False)

    symbols_to_scan = (
        get_dynamic_symbols(50)
        if use_dynamic
        else SYMBOLS
    )

    print(f"Escaneando {len(symbols_to_scan)} símbolos...")

    signals = []

    for symbol in symbols_to_scan:

        print("\n" + "=" * 70)
        print(f"Analizando: {symbol}")

        # Obtener velas
        df = fetch_candles(symbol)

        if df is None:
            print("No se pudieron obtener velas.")
            continue

        print("Columnas originales:")
        print(df.columns.tolist())

        # Calcular indicadores
        df = calculate_indicators(df)

        if df is None:
            print("No se pudieron calcular indicadores.")
            continue

        print("Columnas con indicadores:")
        print(df.columns.tolist())

        # Evaluar estrategia
        action, score, reason = evaluate_market_condition(df)

        print(f"Acción : {action}")
        print(f"Score  : {score}")
        print(f"Razón  : {reason}")

        price = get_current_price(symbol)

        if action != "HOLD":

            latest = df.iloc[-1]

            print("----------- INDICADORES -----------")
            print(f"EMA 9        : {latest.get('ema_9')}")
            print(f"EMA 21       : {latest.get('ema_21')}")
            print(f"EMA 50       : {latest.get('ema_50')}")
            print(f"RSI          : {latest.get('rsi')}")
            print(f"MACD         : {latest.get('macd')}")
            print(f"MACD Signal  : {latest.get('macd_signal')}")
            print(f"ADX          : {latest.get('adx')}")
            print(f"ATR          : {latest.get('atr')}")
            print(f"Supertrend   : {latest.get('supertrend')}")
            print("----------------------------------")

            atr = latest["atr"]

            sl, tp = calculate_risk_parameters(
                price,
                atr,
                action
            )

            signals.append({

                "symbol": symbol,
                "action": action,
                "score": score,
                "reason": reason,
                "price": price,
                "stop_loss": sl,
                "take_profit": tp

            })

            print(f"✅ Señal agregada para {symbol}")

        else:
            print("⏸ Sin señal (HOLD)")

    print("\n" + "=" * 70)
    print(f"Escaneo finalizado. Señales encontradas: {len(signals)}")
    print("=" * 70)

    bot_status["active_signals"] = signals

    return jsonify({

        "status": "success",
        "signals": signals

    })


@app.route('/api/execute', methods=['POST'])
def api_execute():

    data = request.json or {}

    symbol = data.get("symbol")

    action = data.get("action")

    amount_usdt = float(data.get("amount", 15))

    if not symbol or not action:

        return jsonify({

            "status": "error",
            "message": "Faltan parámetros"

        }), 400

    order = place_market_order(

        symbol,
        action,
        amount_usdt

    )

    if order:

        return jsonify({

            "status": "success",
            "order": order

        })

    return jsonify({

        "status": "error",
        "message": "Error al ejecutar en Binance"

    }), 500


if __name__ == "__main__":

    print("=" * 50)
    print("🚀 INICIANDO SISTEMA DE TRADING INSTITUCIONAL 🚀")
    print("=" * 50)
    print("🌐 Servidor web activo en: http://127.0.0.1:5001")
    print("💡 Presiona CTRL+C para detener el bot en cualquier momento.")
    print("=" * 50)

    app.run(
        debug=True,
        port=5001
    )
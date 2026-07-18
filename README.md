# 🚀 TradingBot

Bot de Trading Institucional desarrollado en Python para Binance Spot.

El objetivo de este proyecto es construir un sistema profesional capaz de analizar el mercado, detectar oportunidades de alta probabilidad y ejecutar operaciones de forma segura mediante una arquitectura modular y escalable.

---

# Características actuales

- ✅ Dashboard Web con Flask.
- ✅ Consulta de balance en Binance.
- ✅ Escáner de mercado.
- ✅ Escaneo dinámico por volumen.
- ✅ Gestión de riesgo.
- ✅ Ejecución de órdenes Spot.
- ✅ Arquitectura modular.
- ✅ Indicadores separados por módulos.

---

# Arquitectura del proyecto

```
TradingBot
│
├── api
├── config
├── execution
├── indicators
├── risk
├── scanner
├── strategy
├── templates
├── static
├── main.py
├── .env
├── requirements.txt
├── README.md
└── CHANGELOG.md
```

---

# Tecnologías utilizadas

- Python 3
- Flask
- CCXT
- Pandas
- NumPy
- Binance API

---

# Instalación

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Configurar las claves de Binance en el archivo `.env`:

```
BINANCE_API_KEY=TU_API_KEY
BINANCE_SECRET_KEY=TU_SECRET_KEY
```

Ejecutar el proyecto:

```bash
python main.py
```

Abrir el navegador:

```
http://127.0.0.1:5001
```

---

# Estado del proyecto

🚧 Versión 2.0.0 (En desarrollo)

Actualmente se está migrando a una arquitectura modular para facilitar el crecimiento del proyecto y la incorporación de nuevas funcionalidades.

---

# Próximas funcionalidades

- RSI modular.
- MACD.
- ATR.
- ADX.
- VWAP.
- SuperTrend.
- Base de datos SQLite.
- Historial de operaciones.
- Sistema de Logs.
- Alertas por Telegram.
- Backtesting.
- Dashboard avanzado.
- Modo Automático.
- Inteligencia Artificial para filtrado de señales.

---

# Licencia

Proyecto de uso educativo y experimental.

El usuario es responsable del uso del bot y de cualquier operación realizada en mercados financieros.
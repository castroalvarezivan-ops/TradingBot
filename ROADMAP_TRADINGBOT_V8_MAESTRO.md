# TradingBot — Roadmap Maestro V8

**Fecha de actualización:** 2026-08-10  
**Base:** `TRADINGBOT_FULL_AUDIT.txt` + estado de trabajo reconstruido durante el desarrollo.

> Este documento sustituye la lectura literal del roadmap antiguo como fuente de estado. El objetivo es separar lo implementado, lo integrado parcialmente y lo pendiente.

---

## 0. Regla de estado

- 🟢 **IMPLEMENTADO + CONECTADO** — existe y participa en el flujo principal.
- 🟡 **IMPLEMENTADO + PARCIAL** — existe, pero la integración está incompleta.
- 🟠 **IMPLEMENTADO + NO CONECTADO** — existe código funcional, pero el flujo principal todavía no lo utiliza.
- 🔴 **PENDIENTE** — todavía falta construirlo o integrarlo.
- ⚠️ **AUDITAR** — existe, pero antes de marcarlo como terminado hay que comprobar su comportamiento extremo/integración.

---

# FASE 0 — Fundaciones y control del proyecto

### Estado: 🟢 / 🟡

- 🟢 Estructura modular del proyecto.
- 🟢 Configuración centralizada.
- 🟢 `.env` para credenciales.
- 🟢 Git / control de versiones.
- 🟢 Separación entre Core, Engines, Strategy, API, Dashboard, Backtesting y Paper Trading.
- 🟡 Documentación de versión y roadmap: existen, pero estaban desactualizados respecto a la evolución posterior.
- 🟡 El inventario contiene código histórico/duplicado que debe distinguirse del flujo oficial.

**Objetivo:** mantener una única arquitectura oficial y evitar seguir agregando módulos sin integración.

---

# FASE 1 — Market Engine

### Estado: 🟢 IMPLEMENTADO + CONECTADO

Responsabilidades:

- Descarga de OHLCV.
- Conexión con el mercado.
- Timeframe principal de 15m.
- Precio actual.
- Integración con el scanner/cliente de mercado.

Configuración actual auditada:

- BTC/USDT
- ETH/USDT
- SOL/USDT
- BNB/USDT
- ADA/USDT

**Pendiente:**
- ⚠️ Verificar normalización de símbolos entre `BTC/USDT` y posibles formatos internos.
- ⚠️ Validar manejo de errores, datos insuficientes y rate limits.
- ⚠️ Definir una única fuente oficial de datos para live, paper y backtesting.

---

# FASE 2 — Strategy Engine

### Estado: 🟢 IMPLEMENTADO + CONECTADO / ⚠️ AUDITAR

El Strategy Engine procesa el dataframe antes de la decisión.

Incluye la capa de indicadores y Smart Money.

Componentes identificados en el proyecto:

- EMA
- RSI
- MACD
- ATR
- ADX
- VWAP
- Supertrend
- Volume SMA
- Swings
- Market Structure
- BOS
- CHOCH
- Liquidity
- Order Blocks
- Fair Value Gap
- componentes Smart Money V2

Configuración:

- `USE_SMART_MONEY_V2 = True`

**Punto crítico:**
El Strategy Engine produce un dataframe procesado, pero el `PipelineEngine` toma ese dataframe y vuelve a entregar la última fila al Decision Engine. La relación entre cualquier decisión generada dentro de capas antiguas de Strategy y la decisión oficial del `DecisionEngine` debe quedar explícitamente definida.

**Objetivo:** una única fuente oficial de features; ningún indicador debe calcularse sin propósito dentro de la decisión.

---

# FASE 3 — Decision Engine

### Estado: 🟢 IMPLEMENTADO + CONECTADO / ⚠️ AUDITAR

Flujo actual:

```text
features de Strategy
        ↓
Score Engine
        ↓
Confidence Engine
        ↓
BUY / SELL / HOLD
```

Configuración:

- `BUY_THRESHOLD = 50`
- `SELL_THRESHOLD = -50`
- Confidence Engine activado.
- Circuit Breaker integrado.

El Decision Engine utiliza:

- Score Engine.
- Confidence Engine.
- Circuit Breaker.

**Pendiente:**
- ⚠️ Auditar pesos y reglas del Score Engine.
- ⚠️ Definir qué significa estadísticamente el score.
- ⚠️ Evitar interpretar `confidence` como probabilidad real de ganar hasta validarlo.
- 🔴 Reducir señales falsas mediante backtesting.
- 🔴 Evaluar umbrales dinámicos por régimen de mercado.

---

# FASE 4 — Risk Engine

### Estado: 🟠 IMPLEMENTADO + NO CONECTADO AL PIPELINE PRINCIPAL

El código del Risk Engine existe y contempla validaciones de riesgo.

Sin embargo, el `PipelineEngine` actual contiene:

```text
valid = True
reason_risk = "Pendiente integración"
```

Por lo tanto, esta fase **NO debe marcarse como terminada**.

**Objetivo prioritario:**

```text
Decision
   ↓
Risk Engine
   ↓
VALID / BLOCK
   ↓
Position Engine
```

Debe validar como mínimo:

- Riesgo por operación.
- Balance disponible.
- Drawdown.
- Máximo de operaciones.
- Tamaño de posición.
- Stop Loss.
- Take Profit.
- Fees.
- Slippage.

Configuración actual:

- Riesgo por operación: 1%.
- ATR SL: 2.0.
- ATR TP: 4.0.
- Máximo de operaciones abiertas: 1.
- Comisión: 0.1%.
- Slippage: 0.05%.

---

# FASE 5 — Portfolio Engine

### Estado: 🟢 IMPLEMENTADO + CONECTADO / ⚠️ AUDITAR

Responsabilidades:

- Balance/estado del portfolio.
- Comprobación de posiciones abiertas.
- Resumen de portfolio.

Actualmente el Pipeline consulta el portfolio antes de construir la posición.

**Pendiente:**
- Integrar definitivamente el estado de posiciones con Paper Trading.
- Garantizar que el límite de operaciones se aplique en una sola capa de autoridad.
- Validar consistencia entre balance del exchange y balance paper.

---

# FASE 6 — Position Engine

### Estado: 🟢 IMPLEMENTADO + CONECTADO

Construye la posición a partir de:

- Balance.
- Símbolo.
- Acción.
- Precio de entrada.
- ATR.

Calcula:

- Stop Loss.
- Take Profit.
- Riesgo monetario.
- Quantity.
- Risk percent.

Configuración actual:

```text
Riesgo = 1%
SL = ATR × 2
TP = ATR × 4
```

**Pendiente:**
- ⚠️ Validar mínimos/máximos y precision de Binance.
- ⚠️ Validar cantidad mínima por símbolo.
- ⚠️ Integrarlo después de Risk Engine, no antes.
- ⚠️ Añadir fees/slippage al sizing final.

---

# FASE 7 — Trade Manager / Paper Trading

### Estado: 🟡 IMPLEMENTADO + PARCIAL

El Pipeline ya:

1. actualiza trades cerrados;
2. construye una posición;
3. abre un paper trade;
4. guarda SL/TP.

Esto demuestra que Paper Trading ya participa en el flujo.

**Pendiente:**
- Paper wallet/balance totalmente consistente.
- Registro persistente de operaciones.
- Equity Curve.
- PnL real.
- Drawdown.
- Estadísticas derivadas de trades.
- Reconciliación de posiciones abiertas/cerradas.
- Tests de SL/TP y timeout.

---

# FASE 8 — Backtesting

### Estado: 🟢 IMPLEMENTADO / ⚠️ AUDITAR

Existe `BacktestingEngine` que conecta:

```text
Market
 ↓
Strategy
 ↓
Decision
 ↓
Simulator
 ↓
Metrics
 ↓
Report
```

El engine procesa decisiones sobre las filas del dataframe y luego simula trades.

**Pendiente:**
- Garantizar que Backtesting y Live/Paper utilicen exactamente la misma lógica de Strategy + Decision.
- Añadir fees y slippage de forma coherente.
- Evitar look-ahead bias.
- Validar resultados con múltiples pares y periodos.
- Walk Forward.
- Monte Carlo.
- Tests de robustez.

---

# FASE 9 — Analytics

### Estado: 🟡 IMPLEMENTADO + PARCIAL

Existen módulos para:

- Equity Curve.
- Drawdown.
- Expectancy.
- Performance.
- Statistics.
- Trade History.
- Reports.
- Exportación.

**Problema actual:**
El dashboard/API todavía utiliza valores temporales para winrate y drawdown.

Por tanto:

```text
WINRATE = 92%
DRAWDOWN = 3.2%
```

**NO deben considerarse métricas reales del sistema.**

**Objetivo:** conectar Analytics con el historial real de Paper Trading/Backtesting.

---

# FASE 10 — Resilience / Circuit Breaker

### Estado: 🟢 IMPLEMENTADO + CONECTADO

El Decision Engine consulta el Circuit Breaker antes de procesar una decisión.

Debe mantenerse como protección transversal.

**Pendiente:**
- Integrarlo también donde corresponda en Market/Risk/Execution.
- Definir qué errores abren el circuito.
- Añadir observabilidad y métricas.

---

# FASE 11 — API + Dashboard

### Estado: 🟢 / 🟡

API Flask V8 existente.

Flujo:

```text
Dashboard
   ↓
/api/scan
   ↓
PipelineEngine
   ↓
signals
   ↓
Dashboard
```

También existe endpoint de balance.

El dashboard V8 utiliza `index_v8.html`.

**Pendiente:**
- Conectar métricas reales.
- Mostrar estado real de Risk.
- Mostrar estado real de Paper Trading.
- Mostrar posiciones.
- Mostrar PnL.
- Mostrar equity curve.
- Mostrar drawdown real.
- Mostrar razones de bloqueo.
- Evitar métricas hardcodeadas.

---

# FASE 12 — Execution Engine

### Estado: 🟠 IMPLEMENTADO + NO CONECTADO AL PIPELINE

El Pipeline crea una respuesta:

```text
status = SIMULATION
message = Orden preparada
```

pero no ejecuta la orden mediante `ExecutionEngine` en ese paso.

Esto es correcto mientras se esté validando Paper Trading.

**NO activar Live Trading todavía.**

Antes de conectar ejecución real deben estar cerradas las fases:

```text
Risk
Portfolio
Position
Paper Trading
Analytics
Resilience
```

y debe existir una batería de pruebas.

---

# FASE 13 — Live Trading

### Estado: 🔴 PENDIENTE

Solo después de completar la validación Paper.

Requisitos mínimos:

- Risk Engine conectado.
- Position sizing validado.
- Balance real reconciliado.
- Precision de Binance validada.
- Fees/slippage incorporados.
- Stop Loss/Take Profit verificados.
- Protección de drawdown.
- Daily loss limit.
- Max trades/day.
- Circuit Breaker.
- Logs.
- Auditoría de errores.
- Kill switch.
- Pruebas en entorno controlado.

---

# FASE 14 — Machine Learning / IA

### Estado: 🔴 FUTURO

El proyecto contempla:

- Machine Learning.
- Optimización automática.
- Predicción de probabilidad.
- Confidence basado en IA.
- Optimización genética.
- Walk Forward.
- Monte Carlo.

**Regla:** no introducir ML para compensar una arquitectura o estrategia que todavía no haya sido validada estadísticamente.

Primero debemos tener un baseline estable.

---

# ORDEN OFICIAL DE TRABAJO

## Prioridad 1 — Integridad del pipeline

```text
Market
 ↓
Strategy
 ↓
Decision
 ↓
Portfolio
 ↓
Risk  ← CONECTAR
 ↓
Position
 ↓
Trade Manager
 ↓
Paper Trading
```

## Prioridad 2 — Métricas reales

```text
Paper Trades
 ↓
Trade History
 ↓
Analytics
 ↓
Winrate
Drawdown
Profit Factor
Expectancy
Equity Curve
```

## Prioridad 3 — Validación

```text
Backtesting
 ↓
Out-of-sample
 ↓
Walk Forward
 ↓
Monte Carlo
 ↓
Paper Trading prolongado
```

## Prioridad 4 — Ejecución

```text
Paper Trading estable
 ↓
Execution Engine
 ↓
Live Trading controlado
```

---

# BLOQUEOS ACTUALES

Antes de Live Trading:

- 🔴 Risk Engine debe integrarse realmente al Pipeline.
- 🔴 Paper Trading debe producir estadísticas reales.
- 🔴 Dashboard debe dejar de mostrar métricas hardcodeadas.
- 🔴 Position sizing debe pasar por Risk antes de abrir posición.
- ⚠️ Strategy/Decision debe tener una única definición oficial de señal.
- ⚠️ Backtesting debe compartir exactamente la misma lógica que Paper/Live.
- ⚠️ Execution debe permanecer en simulación hasta completar validación.
- ⚠️ Deben existir tests de integración del pipeline completo.

---

# ARQUITECTURA OFICIAL PROPUESTA

```text
                         BINANCE
                            │
                            ▼
                     ┌─────────────┐
                     │ MarketEngine│
                     └──────┬──────┘
                            ▼
                     ┌─────────────┐
                     │StrategyEngine│
                     └──────┬──────┘
                            ▼
                     ┌─────────────┐
                     │DecisionEngine│
                     └──────┬──────┘
                            ▼
                     ┌─────────────┐
                     │PortfolioEngine│
                     └──────┬──────┘
                            ▼
                       ┌────────┐
                       │  RISK  │
                       └────┬───┘
                            ▼
                     ┌─────────────┐
                     │PositionEngine│
                     └──────┬──────┘
                            ▼
                     ┌─────────────┐
                     │Trade Manager│
                     └──────┬──────┘
                            ▼
                     ┌─────────────┐
                     │Paper Trading│
                     └──────┬──────┘
                            ▼
                     ┌─────────────┐
                     │  Analytics  │
                     └──────┬──────┘
                            │
                   ┌────────┴────────┐
                   ▼                 ▼
              Dashboard          Reports

                  FUTURO
                     │
                     ▼
              ExecutionEngine
                     │
                     ▼
                LIVE BINANCE
```

---

# DEFINICIÓN DE "LISTO PARA LIVE"

El proyecto no se considerará listo para dinero real por tener muchas carpetas o una etiqueta V8.

Será "Live Ready" únicamente cuando:

- [ ] Risk integrado y probado.
- [ ] Position sizing probado.
- [ ] Paper wallet reconciliado.
- [ ] Historial de trades persistente.
- [ ] Métricas reales.
- [ ] Backtest reproducible.
- [ ] Out-of-sample validado.
- [ ] Walk Forward.
- [ ] Monte Carlo.
- [ ] Fees/slippage.
- [ ] Circuit Breaker.
- [ ] Kill switch.
- [ ] Límites de pérdida.
- [ ] Tests de integración.
- [ ] Logs/auditoría.
- [ ] Ejecución Binance probada en modo seguro.
- [ ] Paper Trading prolongado sin inconsistencias.

---

## REGLA DEL PROYECTO

**No añadir una nueva capa hasta demostrar que la capa anterior funciona.**

La prioridad ahora no es agregar más indicadores, IA o Smart Money.

La prioridad es convertir el sistema existente en un flujo coherente:

**SEÑAL → RIESGO → POSICIÓN → PAPER TRADE → MÉTRICAS → VALIDACIÓN.**

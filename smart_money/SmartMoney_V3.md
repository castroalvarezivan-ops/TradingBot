# SMART MONEY ENGINE V3

## Objetivo

Detectar estructuras institucionales de alta calidad para generar señales con mayor probabilidad de éxito.

---

## Flujo

Velas

↓

Swing Detection

↓

Market Structure

↓

Break Of Structure (BOS)

↓

Change Of Character (CHoCH)

↓

Liquidity

↓

Order Blocks

↓

Mitigation

↓

Fair Value Gap

↓

Premium / Discount

↓

Confluence

↓

Score Engine

---

## Módulos

### swings.py

Responsable de detectar:

- Swing High
- Swing Low
- Fuerza del swing

---

### market_structure.py

Construye:

HH

HL

LH

LL

---

### bos.py

Detecta rupturas reales de estructura.

---

### choch.py

Detecta cambios de tendencia.

---

### liquidity.py

Detecta:

Equal High

Equal Low

Liquidity Sweep

---

### order_blocks.py

Detecta:

Bullish OB

Bearish OB

Mitigated

Fresh

---

### mitigation.py

Detecta mitigaciones.

---

### fair_value_gap.py

Detecta:

Bullish FVG

Bearish FVG

Filled

Open

---

### premium_discount.py

Calcula:

Premium

Discount

Equilibrium

---

### confluence.py

Une toda la información y genera una estructura única para el Score Engine.
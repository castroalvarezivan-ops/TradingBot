# ==========================================
# TradingBot V2.6.3
# Archivo: analytics/statistics.py
# ==========================================

"""
Módulo de estadísticas del TradingBot.

Este archivo irá creciendo progresivamente durante la V2.6.3.

Actualmente calcula:

- Confidence promedio

Próximamente incorporará:

- Average Win
- Average Loss
- Expectancy
- Profit Factor monetario
- Recovery Factor
- Average Risk Reward
"""


def average_win(trades):
    """
    Placeholder.

    Será implementado cuando cada trade almacene
    el beneficio monetario (PnL).
    """

    return 0.0


def average_loss(trades):
    """
    Placeholder.

    Será implementado cuando cada trade almacene
    la pérdida monetaria (PnL).
    """

    return 0.0


def confidence_average(trades):
    """
    Calcula el Score promedio generado
    por el Decision Engine.
    """

    if not trades:
        return 0.0

    total_score = sum(
        trade["score"]
        for trade in trades
    )

    return round(
        total_score / len(trades),
        2
    )
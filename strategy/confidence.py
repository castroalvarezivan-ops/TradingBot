"""
Confidence Engine
V2.6.2

Convierte el Score institucional en un porcentaje
de confianza para la operación.
"""


def calculate_confidence(score):
    """
    Convierte un score en un porcentaje de confianza.

    Retorna:
        confidence (0-100)
        level (LOW / MEDIUM / HIGH / VERY HIGH)
    """

    # Limitar score entre -100 y 100
    score = max(min(score, 100), -100)

    confidence = abs(score)

    if confidence < 40:
        level = "LOW"

    elif confidence < 60:
        level = "MEDIUM"

    elif confidence < 80:
        level = "HIGH"

    else:
        level = "VERY HIGH"

    return confidence, level
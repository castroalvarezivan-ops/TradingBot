from datetime import datetime


def calculate_confidence(score):
    """
    Convierte el score en un porcentaje de confianza.
    """

    confidence = abs(score)

    if confidence > 100:
        confidence = 100

    return confidence


def risk_level(confidence):
    """
    Determina el nivel de riesgo.
    """

    if confidence >= 90:
        return "LOW"

    elif confidence >= 75:
        return "MEDIUM"

    return "HIGH"


def build_signal(action, score, reason):
    """
    Construye la señal institucional.
    """

    confidence = calculate_confidence(score)

    signal = {

        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "action": action,

        "score": score,

        "confidence": confidence,

        "risk_level": risk_level(confidence),

        "reason": reason

    }

    return signal
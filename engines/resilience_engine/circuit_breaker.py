# ==========================================
# TradingBot V2.8.1
# Archivo: engines/resilience_engine/circuit_breaker.py
# ==========================================

import logging
import time

logger = logging.getLogger("CircuitBreaker")


class CircuitBreaker:
    """
    Circuit Breaker institucional.

    Evita que un módulo continúe ejecutándose cuando
    ocurren demasiados errores consecutivos.
    """

    def __init__(
        self,
        failure_threshold=5,
        recovery_timeout=60
    ):

        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout

        self.failure_count = 0

        self.last_failure_time = None

        self.state = "CLOSED"

    # ==========================================
    # Consultar estado
    # ==========================================

    def can_proceed(self):
        """
        Retorna True si el sistema puede continuar.
        """

        if self.state == "CLOSED":
            return True

        if self.state == "OPEN":

            elapsed = time.time() - self.last_failure_time

            if elapsed >= self.recovery_timeout:

                logger.warning(
                    "Circuit Breaker -> HALF_OPEN"
                )

                self.state = "HALF_OPEN"

                return True

            return False

        if self.state == "HALF_OPEN":
            return True

        return False

    # ==========================================
    # Reportar éxito
    # ==========================================

    def report_success(self):

        if self.state == "HALF_OPEN":

            logger.info(
                "Circuit Breaker RESET"
            )

            self.reset()

    # ==========================================
    # Reportar fallo
    # ==========================================

    def report_failure(self):

        self.failure_count += 1

        self.last_failure_time = time.time()

        logger.error(
            f"Circuit Failure #{self.failure_count}"
        )

        if self.failure_count >= self.failure_threshold:

            self.state = "OPEN"

            logger.critical(
                "Circuit Breaker OPEN"
            )

    # ==========================================
    # Reiniciar
    # ==========================================

    def reset(self):

        self.failure_count = 0

        self.last_failure_time = None

        self.state = "CLOSED"

    # ==========================================
    # Estado
    # ==========================================

    def get_status(self):

        return {

            "state": self.state,

            "failures": self.failure_count,

            "threshold": self.failure_threshold,

            "timeout": self.recovery_timeout

        }


# ==========================================
# Instancia Global
# ==========================================

circuit_breaker = CircuitBreaker()
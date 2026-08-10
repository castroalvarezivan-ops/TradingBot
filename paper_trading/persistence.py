# ==========================================
# TradingBot V4.5
# Persistence Manager
# ==========================================

"""
Persistence Manager

Guarda y recupera automáticamente
el estado del Paper Trading.

Archivos utilizados:

- wallet.json
- positions.json
- history.json
"""

import json
from pathlib import Path


BASE_DIR = Path(__file__).parent

WALLET_FILE = BASE_DIR / "wallet.json"
POSITIONS_FILE = BASE_DIR / "positions.json"
HISTORY_FILE = BASE_DIR / "history.json"


class PersistenceManager:

    # ======================================

    @staticmethod
    def save_json(filepath, data):

        with open(filepath, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    # ======================================

    @staticmethod
    def load_json(filepath):

        if not filepath.exists():

            return None

        with open(filepath, "r", encoding="utf-8") as f:

            return json.load(f)

    # ======================================
    # Wallet
    # ======================================

    @classmethod
    def save_wallet(cls, wallet):

        cls.save_json(

            WALLET_FILE,

            wallet.summary()

        )

    @classmethod
    def load_wallet(cls):

        return cls.load_json(

            WALLET_FILE

        )

    # ======================================
    # Positions
    # ======================================

    @classmethod
    def save_positions(cls, positions):

        data = [

            p.summary()

            for p in positions

        ]

        cls.save_json(

            POSITIONS_FILE,

            data

        )

    @classmethod
    def load_positions(cls):

        return cls.load_json(

            POSITIONS_FILE

        )

    # ======================================
    # History
    # ======================================

    @classmethod
    def save_history(cls, history):

        cls.save_json(

            HISTORY_FILE,

            history

        )

    @classmethod
    def load_history(cls):

        return cls.load_json(

            HISTORY_FILE

        )
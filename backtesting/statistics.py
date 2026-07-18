from collections import Counter


def calculate_statistics(trades):
    """
    Calcula estadísticas completas del backtesting.
    """

    if len(trades) == 0:

        return {

            "total": 0,

            "buy": 0,

            "sell": 0,

            "hold": 0,

            "wins": 0,

            "losses": 0,

            "open": 0,

            "win_rate": 0,

            "average_score": 0

        }

    actions = [trade["action"] for trade in trades]

    counter = Counter(actions)

    average_score = sum(
        trade["score"] for trade in trades
    ) / len(trades)

    wins = sum(
        1 for trade in trades
        if trade.get("result") == "WIN"
    )

    losses = sum(
        1 for trade in trades
        if trade.get("result") == "LOSS"
    )

    open_trades = sum(
        1 for trade in trades
        if trade.get("result") == "OPEN"
    )

    closed = wins + losses

    if closed > 0:
        win_rate = (wins / closed) * 100
    else:
        win_rate = 0

    stats = {

        "total": len(trades),

        "buy": counter.get("BUY", 0),

        "sell": counter.get("SELL", 0),

        "hold": counter.get("HOLD", 0),

        "wins": wins,

        "losses": losses,

        "open": open_trades,

        "win_rate": round(win_rate, 2),

        "average_score": round(average_score, 2)

    }

    return stats
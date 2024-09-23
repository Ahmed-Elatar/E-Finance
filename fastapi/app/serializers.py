# --------------------  serializers-----------------------------


def TickerSerializer(Ticker :dict):
    return {
        "sender" :Ticker["sender"],
        "ticker": Ticker["symbol"],
        "status": Ticker["status"],

    }

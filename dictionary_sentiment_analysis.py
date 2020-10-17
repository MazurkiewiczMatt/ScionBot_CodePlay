bull_words = ["moon", "rocket", "tendies", "call", "print", "bull", "long", "gain", "rise", "fed", "increase", "green",
              "profit", "buy"]

bear_words = ["put", "scam", "bubble", "drill", "bear", "short", "rope", "loss", "hell", "black", "red", "sell"]


def dictionary_sentiment_check(string: str) -> float:
    """Returns bullish attitude in range (0, 1). (1-return) is the formula for bearish attitude."""
    bullishness = 0
    bearishness = 0
    string = string.lower()
    for word in bull_words:
        if word in string:
            bullishness += 1
    for word in bear_words:
        if word in string:
            bearishness += 1
    total_words = bullishness + bearishness
    return bullishness / total_words

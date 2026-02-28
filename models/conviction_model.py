from data.market_data import sentiment_score

def conviction(signal):

    sentiment = sentiment_score()

    return signal * sentiment

def generate_signal(token_data):

    score = (
        token_data["volume"] * 0.4 +
        token_data["wallets"] * 0.3 +
        token_data["liquidity"] * 0.3
    )

    return score

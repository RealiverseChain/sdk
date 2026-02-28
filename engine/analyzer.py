from data.solana_collector import collect_tokens
from models.signal_model import generate_signal
from models.conviction_model import conviction


def analyze():

    tokens = collect_tokens()

    results = []

    for token in tokens:

        signal = generate_signal(token)

        score = conviction(signal)

        results.append({

            "token": token["token"],

            "score": score

        })

    return results

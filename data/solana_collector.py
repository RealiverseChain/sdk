import random

def collect_tokens():

    tokens = [
        "BONK",
        "WIF",
        "JUP",
        "PYTH",
        "RAY",
        "ORCA"
    ]

    data = []

    for token in tokens:

        data.append({

            "token": token,

            "volume": random.randint(1000,100000),

            "wallets": random.randint(50,500),

            "liquidity": random.randint(10000,200000)

        })

    return data

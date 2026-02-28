from engine.aggregator import aggregate
from models.ranking_model import rank
from config.settings import MAX_RESULTS


def top_convictions():

    results = aggregate()

    ranked = rank(results)

    return ranked[:MAX_RESULTS]

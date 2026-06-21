from difflib import SequenceMatcher

def compute_reward(a, b):
    return SequenceMatcher(None, a, b).ratio()

memory_store = []

def store_feedback(draft, edited, score):
    memory_store.append({
        "draft": draft,
        "edited": edited,
        "score": score
    })

def get_recent_feedback(n=3):
    return memory_store[-n:]

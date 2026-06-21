def detect_conflict(values):

    unique = list(set(values))

    if len(unique) > 1:
        return {
            "conflict": True,
            "values": unique
        }

    return {"conflict": False}

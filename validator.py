def validate(value):

    if not value or value in ["NOT_FOUND", "FAILED"]:
        return "MISSING - FLAGGED"

    return value

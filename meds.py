def compare_meds(admission, discharge):

    added = list(set(discharge) - set(admission))
    removed = list(set(admission) - set(discharge))

    flagged = []

    for med in added:
        flagged.append(f"{med} ADDED - reason not documented")

    for med in removed:
        flagged.append(f"{med} REMOVED - reason not documented")

    return {
        "added": added,
        "removed": removed,
        "flags": flagged
    }

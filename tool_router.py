def decide_tool(state, action):

    if "extract" in action:
        return "extractor"

    if state["med_admission"] and state["med_discharge"]:
        return "meds"

    if len(state["diagnosis"]) > 1:
        return "conflict"

    if "MISSING" in str(state):
        return "escalation"

    return "extractor"

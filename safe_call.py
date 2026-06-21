def drug_interaction_tool(meds):

    if "aspirin" in meds and "warfarin" in meds:
        return "WARNING: aspirin + warfarin interaction"

    return "No interaction"

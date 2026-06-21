from src.agent.state import init_state
from src.tools.extractor import extract_section
from src.tools.meds import compare_meds
from src.tools.validator import validate
from src.tools.conflict import detect_conflict
from src.tools.safe_call import safe_tool_call
from src.tools.tool_router import decide_tool
from src.tools.escalation import escalation_tool

from src.rag.chunker import chunk_text
from src.rag.embedder import embed_chunks
from src.rag.vector_store import create_index
from src.rag.retriever import retrieve

MAX_STEPS = 10

def run_agent(doc_text):

    # RAG setup
    chunks = chunk_text(doc_text)
    embeddings = embed_chunks(chunks)
    index = create_index(embeddings)

    state = init_state()
    trace = []

    for step in range(MAX_STEPS):

        # Planning
        if not state["demographics"]:
            action = "extract_demographics"
        elif not state["admission_date"]:
            action = "extract_admission_date"
        elif not state["discharge_date"]:
            action = "extract_discharge_date"
        elif not state["diagnosis"]:
            action = "extract_diagnosis"
        elif not state["med_admission"]:
            action = "extract_admission_meds"
        elif not state["med_discharge"]:
            action = "extract_discharge_meds"
        else:
            action = "generate_summary"

        # Retrieval
        query = action.replace("extract_", "")
        context = " ".join(retrieve(query, chunks, index))

        # Tool decision
        tool = decide_tool(state, action)

        # Execution with safety
        if tool == "extractor":
            result = safe_tool_call(extract_section, context, query)

        elif tool == "meds":
            result = compare_meds(state["med_admission"], state["med_discharge"])

        elif tool == "conflict":
            result = detect_conflict(state["diagnosis"])

        elif tool == "escalation":
            result = escalation_tool("Critical issue detected")

        else:
            result = "UNKNOWN"

        result = validate(result)

        # Update state
        if "demographics" in action:
            state["demographics"] = result
        elif "diagnosis" in action:
            state["diagnosis"].append(result)
        elif "admission_meds" in action:
            state["med_admission"] = result.split(",")
        elif "discharge_meds" in action:
            state["med_discharge"] = result.split(",")

        # Trace
        trace.append({
            "step": step,
            "action": action,
            "tool": tool,
            "result": result
        })

        if action == "generate_summary":
            break

    state["summary"] = generate_summary(state)

    return state, trace


def generate_summary(state):

    return f"""
    --- DISCHARGE SUMMARY DRAFT ---

    Patient: {state['demographics']}
    Diagnosis: {state['diagnosis']}

    Admission Meds: {state['med_admission']}
    Discharge Meds: {state['med_discharge']}

    Conflicts: {state['conflicts']}
    Missing: {state['missing']}

    NOTE: Draft only. Requires clinician review.
    """

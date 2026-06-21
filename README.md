#  MediAgent-RAG: Agentic Clinical AI System

An intelligent AI system that generates clinical discharge summaries from medical PDFs using **RAG (Retrieval-Augmented Generation)**, **agent-based decision making**, and a **feedback-driven learning loop**.

---

##  Features

*  PDF Ingestion using PyMuPDF
*  RAG Pipeline (Chunking + Embeddings + FAISS)
*  Agent-based workflow with state tracking
*  Dynamic tool selection (Extractor, Meds, Conflict, Validator)
*  Medication reconciliation
*  Conflict detection
*  Failure handling with retry logic
*  Learning loop with memory + reward
*  No hallucination (strict NOT_FOUND policy)

---

##  Architecture

The system follows a modular pipeline:

1. **PDF Parser** → Extracts raw text
2. **RAG Pipeline** → Retrieves relevant context
3. **Agent Controller** → Plans actions using state
4. **Tool System** → Executes domain-specific tasks
5. **Safety Layer** → Handles failures robustly
6. **Learning Loop** → Improves using feedback

---

##  Workflow

1. Input medical PDF
2. Extract text
3. Split into chunks
4. Convert into embeddings
5. Store in FAISS vector DB
6. Retrieve relevant context
7. Agent decides next action
8. Tool executes task
9. State updates
10. Generate discharge summary
11. Learning loop improves system

---

##  Project Structure

```
src/
├── parser/
├── rag/
├── agent/
├── tools/
├── learning/
demo.py
```

---

##  How to Run

```bash
pip install -r requirements.txt
python demo.py
```

---

##  How It Works (Interview Explanation)

This project implements an **agentic AI system** that:

* Uses **RAG** to retrieve grounded information
* Maintains a **state-based workflow**
* Dynamically selects tools based on context
* Ensures reliability using **validation and retries**
* Learns from feedback using **memory and reward signals**
##  Key Highlights

* Combines **LLMs + RAG + Agents + Learning**
* Designed for **real-world healthcare automation**
* Focus on **accuracy, safety, and explainability**


##  Disclaimer

This system generates draft clinical summaries and must be reviewed by a qualified healthcare professional.


##  Author

Harsh Kumar Gaurav
AI/ML Data Science



##  If you like this project

Give it a star and share!

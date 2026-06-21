from src.rag.embedder import model

def retrieve(query, chunks, index, k=3):
    query_vec = model.encode([query])
    _, indices = index.search(query_vec, k)
    return [chunks[i] for i in indices[0]]

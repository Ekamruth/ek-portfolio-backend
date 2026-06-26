from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_PATH = Path(__file__).parent.parent / "knowledge" / "chroma"
_embedding_model = None

def _get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return _embedding_model

def retrieve_relevant_docs(query, top_k=5):
    vector_store = Chroma(collection_name="knowledge_base", persist_directory=str(CHROMA_PATH), embedding_function=_get_embedding_model())
    
    # Retrieve relevant documents based on the query
    relevant_docs = vector_store.similarity_search(query, k=top_k)
    
    return relevant_docs
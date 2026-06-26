import shutil
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

base_path = Path(__file__).parent.parent / "knowledge"
CHROMA_PATH = base_path / "chroma"

def ingest_documents():
    if CHROMA_PATH.exists():
        shutil.rmtree(CHROMA_PATH)
        print("Cleared existing ChromaDB")

    documents = []
    for file in Path(base_path).glob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            documents.append(Document(page_content=content, metadata={"source": str(file)}))

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = text_splitter.split_documents(documents)
    print(f"Number of split documents: {len(split_docs)}")

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = Chroma.from_documents(
        documents=split_docs,
        embedding=embedding_model,
        persist_directory=str(CHROMA_PATH),
        collection_name="knowledge_base"
    )

    print("ChromaDB rebuilt successfully")
    return vector_store
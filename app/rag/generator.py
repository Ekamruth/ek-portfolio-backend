from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from app.rag.retriever import retrieve_relevant_docs
from app.prompt import SYSTEM_PROMPT
from app.config import settings

llm = ChatOpenAI(
    model=settings.openrouter_model,
    base_url=settings.openrouter_base_url,
    api_key=settings.openrouter_api_key,
    temperature=0,
)

def generate_response(query: str, history: list[dict] | None = None):
    relevant_docs = retrieve_relevant_docs(query)
    context = "\n\n".join([f"Source: {doc.metadata['source']}\nContent: {doc.page_content}" for doc in relevant_docs])

    messages = [SystemMessage(content=f"{SYSTEM_PROMPT}\n\nContext:\n{context}")]

    for msg in (history or []):
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))

    messages.append(HumanMessage(content=query))

    return llm.invoke(messages)

def generate_response_stream(query: str, history: list[dict] | None = None):
    relevant_docs = retrieve_relevant_docs(query)
    context = "\n\n".join([f"Source: {doc.metadata['source']}\nContent: {doc.page_content}" for doc in relevant_docs])

    messages = [SystemMessage(content=f"{SYSTEM_PROMPT}\n\nContext:\n{context}")]

    for msg in (history or []):
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))

    messages.append(HumanMessage(content=query))

    return llm.stream(messages)

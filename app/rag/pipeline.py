"""RAG pipeline orchestration."""

from .retriever import Retriever


def answer_question(question: str, retriever: Retriever) -> str:
    """Build a context-aware answer scaffold from retrieved documents."""
    documents = retriever.retrieve(question)
    if not documents:
        return "No relevant context found."
    return "\n\n".join(document.text for document in documents)

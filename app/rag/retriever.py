"""Retrieval interfaces."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievedDocument:
    """A document fragment returned by retrieval."""

    text: str
    score: float = 0.0


class Retriever:
    """Minimal in-memory retriever scaffold."""

    def __init__(self, documents: list[str] | None = None) -> None:
        self.documents = documents or []

    def retrieve(self, query: str, top_k: int = 3) -> list[RetrievedDocument]:
        """Return fragments containing query terms, preserving insertion order."""
        if top_k <= 0:
            return []
        query_terms = set(query.lower().split())
        matches = [
            RetrievedDocument(text=document, score=1.0)
            for document in self.documents
            if query_terms.intersection(document.lower().split())
        ]
        return matches[:top_k]

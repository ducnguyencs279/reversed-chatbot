"""Embedding interfaces."""

from typing import Protocol


class Embedder(Protocol):
    """Interface implemented by embedding providers."""

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one vector per input text."""
        ...

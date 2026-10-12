"""Document chunking utilities."""


def chunk_text(text: str, chunk_size: int = 500) -> list[str]:
    """Split text into non-empty chunks of approximately ``chunk_size`` characters."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size) if text[i : i + chunk_size]]

"""Document loading utilities."""

from pathlib import Path


def load_text(path: str | Path) -> str:
    """Load a UTF-8 text document."""
    return Path(path).read_text(encoding="utf-8")

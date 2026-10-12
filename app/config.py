"""Application configuration."""

from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    data_dir: Path = Path(os.getenv("DATA_DIR", "data/sample"))
    model_name: str = os.getenv("MODEL_NAME", "")


settings = Settings()

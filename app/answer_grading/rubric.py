"""Rubric definitions for answer grading."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Rubric:
    """Simple grading rubric."""

    max_score: float = 10.0

"""Answer grading interface."""

from .rubric import Rubric


def grade_answer(answer: str, reference: str, rubric: Rubric | None = None) -> float:
    """Return a simple token-overlap score as a scaffold."""
    rubric = rubric or Rubric()
    answer_terms = set(answer.lower().split())
    reference_terms = set(reference.lower().split())
    if not reference_terms:
        return 0.0
    return rubric.max_score * len(answer_terms & reference_terms) / len(reference_terms)

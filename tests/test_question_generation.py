from app.question_generation.generator import generate_questions


def test_generate_questions():
    assert len(generate_questions("context", count=2)) == 2

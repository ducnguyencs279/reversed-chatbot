from app.answer_grading.grader import grade_answer


def test_grade_answer():
    assert grade_answer("python language", "python language") == 10.0

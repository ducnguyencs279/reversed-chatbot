from app.rag.chunker import chunk_text
from app.rag.pipeline import answer_question
from app.rag.retriever import Retriever


def test_chunk_text():
    assert chunk_text("abcdef", 2) == ["ab", "cd", "ef"]


def test_answer_question_uses_retrieved_context():
    assert answer_question("python", Retriever(["Python is useful"])) == "Python is useful"

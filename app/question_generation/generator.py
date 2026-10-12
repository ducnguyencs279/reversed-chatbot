def generate_questions(context: str, count: int = 1) -> list[str]:
    if count < 0:
        raise ValueError("count must not be negative")
    if not context.strip():
        return []
    return [f"What is the main idea of the following content? ({index + 1})" for index in range(count)]

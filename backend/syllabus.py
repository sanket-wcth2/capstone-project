CLASS_11_KEYWORDS = [
    "sets", "function", "trigonometry", "sin", "cos", "tan",
    "complex", "quadratic",
    "permutation", "combination",
    "binomial", "sequence", "series",
    "straight line", "conic",
    "limit", "derivative", "differentiate",
    "probability", "statistics"
]

CLASS_12_KEYWORDS = [
    "relation", "function", "inverse",
    "continuity", "differentiability",
    "integration", "integral", "integrate", "dx",
    "differential equation",
    "vector", "3d", "three dimensional",
    "matrix", "determinant", "inverse matrix",
    "linear programming",
    "probability"
]


def is_supported_for_class(question: str, student_class: int) -> bool:
    q = question.lower()

    if student_class == 11:
        return any(k in q for k in CLASS_11_KEYWORDS)

    if student_class == 12:
        return any(k in q for k in CLASS_12_KEYWORDS)

    return False

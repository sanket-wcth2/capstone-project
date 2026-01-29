CLASS_11_TOPICS = [
    "sets", "functions", "trigonometry", "complex",
    "quadratic", "permutation", "combination",
    "binomial", "sequence", "series",
    "straight line", "conic",
    "limit", "derivative", "probability", "statistics"
]

CLASS_12_TOPICS = [
    "relation", "function", "inverse trigonometric",
    "continuity", "differentiability",
    "application of derivative",
    "integration", "integral",
    "differential equation",
    "vector", "3d", "three dimensional",
    "linear programming",
    "probability"
]

# 🔹 ACTION / OPERATION KEYWORDS (VERY IMPORTANT)
ACTION_KEYWORDS = [
    # Calculus actions
    "integrate", "integration", "integral", "dx",
    "differentiate", "derivative", "dy/dx",
    "limit",

    # Matrices & determinants
    "matrix", "matrices", "determinant", "inverse",

    # Vectors
    "vector", "magnitude",

    # Trigonometry usage
    "sin", "cos", "tan", "prove",

    # Algebra indicators
    "x^", "x²", "x**"
]

ALL_KEYWORDS = CLASS_11_TOPICS + CLASS_12_TOPICS + ACTION_KEYWORDS


def is_supported(question: str) -> bool:
    q = question.lower()
    return any(keyword in q for keyword in ALL_KEYWORDS)

def detect_topic(question: str) -> str:
    q = question.lower()

    if "integrate" in q or "∫" in q:
        return "integration"
    if "derivative" in q or "differentiate" in q or "dy/dx" in q:
        return "derivative"
    if "limit" in q:
        return "limit"
    if "determinant" in q:
        return "determinant"
    if "inverse" in q and "matrix" in q:
        return "inverse_matrix"
    if "vector" in q or "magnitude" in q:
        return "vector"
    if "probability" in q:
        return "probability"
    if "prove" in q and ("sin" in q or "cos" in q):
        return "trigonometry"

    return "general"

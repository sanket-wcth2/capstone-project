def get_prompt(topic: str, question: str) -> str:
    base = """
You are an experienced CBSE/HSC Mathematics teacher for Class 11 and 12.
Follow NCERT/HSC board exam format.
Do not skip steps.
Use clear mathematical notation.
Write answers exactly as expected in board exams.
"""

    templates = {
        "integration": base + """
FORMAT:
Given:
∫ [expression] dx

Solution:
Integrating term by term,

∫ [term 1] dx = [result]
∫ [term 2] dx = [result]
∫ [term 3] dx = [result]

Final Answer:
∫ [expression] dx = [combined result] + C
""",

        "derivative": base + """
FORMAT:
Given:
y = [expression]

Solution:
Differentiating both sides with respect to x,

dy/dx = [differentiate term-wise]

Final Answer:
dy/dx = [result]
""",

        "limit": base + """
FORMAT:
Given:
lim (x → a) f(x)

Solution:
Since the given function is continuous at x = a,
substitute x = a.

Final Answer:
[value]
""",

        "determinant": base + """
FORMAT:
Given:
Matrix A (2 × 2)

If the matrix is given in the form [[a,b],[c,d]],
first rewrite it as:

| a  b |
| c  d |

Solution:
Determinant of matrix A is

|A| = ad − bc

Final Answer:
|A| = [value]
""",

        "inverse_matrix": base + """
FORMAT:
Given:
Matrix A

Solution:
First find |A|.

If |A| ≠ 0, then the inverse of A is given by

A⁻¹ = (1/|A|) | d  −b |
               | −c  a |

Final Answer:
A⁻¹ = [matrix]
""",

        "vector": base + """
FORMAT:
Given:
Vector a = xi + yj + zk

Solution:
Magnitude of vector a is

|a| = √(x² + y² + z²)

Final Answer:
|a| = [value]
""",

        "probability": base + """
FORMAT:
Given:
Total number of outcomes = n
Number of favourable outcomes = m

Solution:
Probability = m / n

Final Answer:
Probability = m/n
""",

        "trigonometry": base + """
FORMAT:
Given:
LHS

Solution:
Simplify LHS step by step,

LHS = [expression]
= RHS

Final Answer:
LHS = RHS
Hence proved.
""",

        "general": base
    }

    return templates.get(topic, base) + "\nQuestion:\n" + question

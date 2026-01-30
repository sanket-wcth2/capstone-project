from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from ai_solver import solve_math

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()

    question = data.get("question", "").strip()
    student_class = data.get("class")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    if not student_class:
        return jsonify({"error": "Class not specified"}), 400

    solution = solve_math(question, student_class)

    return jsonify({
        "solution": solution
    })


if __name__ == "__main__":
    app.run(debug=True)

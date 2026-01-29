from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from ai_solver import solve_math

load_dotenv()

app = Flask(__name__)

# ✅ ENABLE CORS FOR FRONTEND
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/solve", methods=["POST"])
def solve():
    try:
        data = request.get_json()
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"error": "Question is required"}), 400

        solution = solve_math(question)

        return jsonify({"solution": solution})

    except Exception as e:
        # 🔴 This helps us see real backend errors
        print("ERROR:", e)
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)

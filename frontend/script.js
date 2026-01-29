async function solveMath() {
    const question = document.getElementById("question").value;
    // Detect topic from question (frontend)
let topic = "General";

const q = question.toLowerCase();

if (q.includes("integrate") || q.includes("∫") || q.includes("dx")) {
    topic = "Integration (Class 12)";
} else if (q.includes("derivative") || q.includes("differentiate") || q.includes("dy/dx")) {
    topic = "Derivative (Class 11/12)";
} else if (q.includes("limit")) {
    topic = "Limits (Class 11)";
} else if (q.includes("determinant")) {
    topic = "Matrix – Determinant";
} else if (q.includes("inverse") && q.includes("matrix")) {
    topic = "Matrix – Inverse";
} else if (q.includes("vector")) {
    topic = "Vectors (Class 12)";
} else if (q.includes("probability")) {
    topic = "Probability";
}

    const output = document.getElementById("output");

    if (!question.trim()) {
        output.innerHTML = "<span class='error'>Please enter a question.</span>";
        return;
    }

    output.innerHTML = "Solving...";

    try {
        const response = await fetch("http://127.0.0.1:5000/solve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        let text = data.solution || data.error;

        // 🔹 FRONTEND CLEANING RULES

        // Remove C1, C2, C3 → replace with C
        text = text.replace(/C\d+/g, "C");

        // Remove repeated explanation clutter
        text = text.replace(/where C =.*$/gm, "");

        // Highlight Final Answer
        text = text.replace(
            /Final Answer:/gi,
            "<br><strong class='final'>Final Answer:</strong>"
        );

        // Preserve line breaks
        text = text.replace(/\n/g, "<br>");
        
        // Show topic badge
        const badge = document.getElementById("topic-badge");
        badge.innerText = topic;
        badge.style.display = "inline-block";

        output.innerHTML = text;

    } catch (error) {
        output.innerHTML = "<span class='error'>Error connecting to server.</span>";
        console.error(error);
    }
}

async function solveMath(studentClass) {
    const question = document.getElementById("question").value;
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
            body: JSON.stringify({
                question: question,
                class: studentClass
            })
        });

        const data = await response.json();
        let text = data.solution;

        if (!text) {
            throw new Error("Empty response");
        }

        // ---------- SPLIT STEPS & FINAL ANSWER ----------
        let stepsText = text;
        let finalLatex = "";

        if (text.includes("FINAL_ANSWER_LATEX:")) {
            const parts = text.split("FINAL_ANSWER_LATEX:");
            stepsText = parts[0].trim();
            finalLatex = parts[1].trim();
        }

        // ---------- BUILD COMBINED OUTPUT ----------
        let html = `<div class="solution-card">`;

        html += `<div class="solution-steps">${stepsText.replace(/\n/g, "<br>")}</div>`;

        if (finalLatex) {
            html += `
                <hr>
                <div class="solution-final">
                    <strong>Final Answer:</strong><br>
                    \\(${finalLatex}\\)
                </div>
            `;
        }

        html += `</div>`;

        output.innerHTML = html;

        if (window.MathJax) {
            MathJax.typesetPromise();
        }

    } catch (error) {
        output.innerHTML = "<span class='error'>Unable to get solution.</span>";
        console.error(error);
    }
}

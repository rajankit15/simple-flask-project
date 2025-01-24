// Move focus to the next input
function moveNext(current, nextId) {
    if (current.value.length === 1) {
        document.getElementById(nextId)?.focus();
    }
}

// Combine code before form submission
function combineCode() {
    const inputs = document.querySelectorAll(".code-inputs input");
    const fullCode = Array.from(inputs).map(input => input.value).join("");
    document.getElementById("fullCode").value = fullCode;
}

// Handle backspace navigation
document.addEventListener("keydown", function (event) {
    if (event.key === "Backspace") {
        let inputs = document.querySelectorAll(".code-inputs input");
        inputs.forEach((input, index) => {
            input.addEventListener("keydown", function (e) {
                if (e.key === "Backspace" && input.value === "") {
                    let prev = inputs[index - 1];
                    if (prev) {
                        prev.focus();
                        prev.value = "";
                    }
                }
            });
        });
    }
});

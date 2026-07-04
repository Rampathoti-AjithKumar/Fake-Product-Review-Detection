async function predictReview() {

    const review = document.getElementById("review").value.trim();

    const loading = document.getElementById("loading");
    const result = document.getElementById("result");

    if (review === "") {
        alert("Please enter a product review.");
        return;
    }

    loading.style.display = "block";
    result.style.display = "none";

    try {

        const response = await fetch("http://localhost:8080/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                review: review
            })
        });

        const data = await response.json();

        loading.style.display = "none";
        result.style.display = "block";

        const color = data.prediction === "Genuine"
            ? "#22c55e"
            : "#ef4444";

        result.innerHTML = `
            <h2>Prediction Result</h2>

            <p style="font-size:22px;font-weight:bold;color:${color};">
                ${data.prediction === "Genuine" ? "✅ Genuine Review" : "❌ Fake Review"}
            </p>

            <br>

            <p style="font-size:18px;">
                Confidence : <b>${data.confidence}%</b>
            </p>

            <div class="progress">
                <div class="progress-bar" id="progressBar"></div>
            </div>
        `;

        setTimeout(() => {
            document.getElementById("progressBar").style.width =
                data.confidence + "%";
        }, 100);

    } catch (error) {

        loading.style.display = "none";

        result.style.display = "block";

        result.innerHTML = `
            <h2 style="color:#ef4444;">
                Unable to connect to the server.
            </h2>
        `;

        console.error(error);
    }
}

function clearReview() {

    document.getElementById("review").value = "";

    document.getElementById("result").style.display = "none";

    document.getElementById("loading").style.display = "none";
}
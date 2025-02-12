let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    if (!textToAnalyze.trim()) {
        document.getElementById("system_response").innerHTML = "Invalid text! Please try again!";
        return;
    }
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        } else if (this.readyState == 4 && this.status == 400) {
            let errorResponse = JSON.parse(xhttp.responseText); 
            document.getElementById("system_response").innerHTML = errorResponse.message; 
        }
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};

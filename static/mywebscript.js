let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let responseJson = JSON.parse(xhttp.responseText); // Convert to JSON
            let emotions = responseJson.emotions; // Extract only emotions

            // Construct the response string in the required format
            let responseText = `For the given statement, the system response is 'anger': ${emotions.anger}, 'disgust': ${emotions.disgust}, 'fear': ${emotions.fear}, 'joy': ${emotions.joy} and 'sadness': ${emotions.sadness}. The dominant emotion is ${emotions.dominant_emotion}.`;

            document.getElementById("system_response").innerText = responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}

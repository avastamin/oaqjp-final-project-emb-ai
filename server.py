from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the index.html page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detection_api():
    """
    API endpoint to analyze emotions from text.

    Expects JSON input:
    {
        "textToAnalyze": "your text here"
    }

    Returns:
    JSON response containing emotion scores and the dominant emotion.
    """
    if request.method == 'GET':
        text_to_analyze = request.args.get("textToAnalyze", "")
    else:
        data = request.get_json()
        text_to_analyze = data.get("textToAnalyze", "")

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    # Call emotion detector function
    emotions = emotion_detector(text_to_analyze)

    # Format the response for display
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}, "
        f"and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    if response["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    return jsonify({"response": response_text, "emotions": emotions})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


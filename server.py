"""
This module is responsible for running the Flask application, which handles text input
for emotion detection and returns the analysis results. It uses the emotion_detector 
function to process text and respond with emotion analysis.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page with the form for text analysis.

    Returns:
        str: The rendered HTML page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Handles the emotion detection request. It accepts the text as a GET request and processes it.

    Args:
        None

    Returns:
        Response: JSON response containing emotion detection result or error message.
    """
    statement = request.args.get('textToAnalyze', '').strip()

    # Check if the statement is empty
    if not statement:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Call the emotion_detector function with the provided statement
    result = emotion_detector(statement)

    # If dominant_emotion is None, return an error message
    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

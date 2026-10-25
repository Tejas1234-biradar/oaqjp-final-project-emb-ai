"""Emotion Detection Web Server.

This module defines a Flask-based web server for performing emotion
detection on user-provided text using the Watson NLP EmotionPredict API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_detector():
    """Analyze the user-provided text for emotions and return the result."""
    text_to_detect = request.args.get("textToAnalyze")

    if not text_to_detect or not text_to_detect.strip():
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_detect)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Initiate the rendering of the main application page over Flask."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

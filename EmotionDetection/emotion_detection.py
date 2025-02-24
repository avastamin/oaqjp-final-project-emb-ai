import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotional tone of the given text using the Watson NLP EmotionPredict API.
    
    Parameters:
        text_to_analyze (str): The text to be analyzed for emotions.
    
    Returns:
        dict: A dictionary containing scores for anger, disgust, fear, joy, sadness, 
              and the dominant emotion with the highest score.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        response_data = response.json()  # Convert response text into dictionary
        
        # Handle error responses
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        response.raise_for_status()
        data = response.json()

        # Extract emotion scores
        emotions = data.get("emotion_predictions", [{}])[0]
        scores = {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': max(emotions, key=emotions.get) if emotions else None
        }
        return scores

    
        # Extract required emotions and their scores
        emotions = response_data.get("emotionPredictions", [{}])[0].get("emotion", {})
        anger = emotions.get("anger", 0.0)
        disgust = emotions.get("disgust", 0.0)
        fear = emotions.get("fear", 0.0)
        joy = emotions.get("joy", 0.0)
        sadness = emotions.get("sadness", 0.0)
        
        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get, default="unknown")
        
        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


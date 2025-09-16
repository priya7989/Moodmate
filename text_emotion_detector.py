from transformers import pipeline

def dynamic_emotion_detection():
    # Load pretrained BERT emotion detection model
    emotion_classifier = pipeline("text-classification", model="boltuix/bert-emotion")

    print("Enter text (type 'exit' to quit):")
    while True:
        text_input = input("> ")
        if text_input.lower() == "exit":
            break
        # Predict emotion
        result = emotion_classifier(text_input)[0]
        print(f"Emotion: {result['label']}, Confidence: {result['score']:.2%}")

if __name__ == "__main__":
    dynamic_emotion_detection()

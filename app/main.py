import sys
import joblib

model = joblib.load("app/sentiment_model.pkl")

def predict_sentiment(text):
    prediction = model.predict([text])[0]
    return "Positive" if prediction == 1 else "Negative"

# Case 1: User passed input as command-line argument
if len(sys.argv) > 1:
    input_text = " ".join(sys.argv[1:])
    sentiment = predict_sentiment(input_text)
    print(f"Sentiment: {sentiment}")

# Case 2: No CLI argument, prompt interactively
else:
    while True:
        input_text = input("Enter text to analyze (or type 'exit' to quit): ")
        if input_text.lower() == "exit":
            break
        sentiment = predict_sentiment(input_text)
        print(f"Sentiment: {sentiment}")

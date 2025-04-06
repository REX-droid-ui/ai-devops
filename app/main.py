import pickle

with open('app/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('app/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_sentiment(text):
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    return "Positive" if prediction[0] == 1 else "Negative"

if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    result = predict_sentiment(text)
    print(f"Sentiment: {result}")

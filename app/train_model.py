import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import joblib
import os

df = pd.read_csv("app/IMDB Dataset.csv")

df["sentiment"] = df["sentiment"].map({"positive": 1, "negative": 0})

X_train, X_test, y_train, y_test = train_test_split(df["review"], df["sentiment"], test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=10000)),
    ('clf', LogisticRegression(max_iter=300))
])

pipeline.fit(X_train, y_train)

os.makedirs("app", exist_ok=True)

joblib.dump(pipeline, "app/sentiment_pipeline.pkl")

print("✅ Trained pipeline saved as app/sentiment_pipeline.pkl")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Sample training data
texts = ["I love this!", "This is amazing", "I hate this", "This is terrible"]
labels = [1, 1, 0, 0]  # 1 = positive, 0 = negative

# Fit vectorizer and model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
model = LogisticRegression()
model.fit(X, labels)

# Save inside app/ directory
with open("app/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ vectorizer.pkl and model.pkl saved inside app/")

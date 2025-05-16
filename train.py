# train_and_save.py
import pickle
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

X = [
    "I love this product", "This is amazing", "Happy and satisfied",
    "Terrible experience", "I hate it", "Worst purchase ever"
]
y = [1, 1, 1, 0, 0, 0]  # 1 = POSITIVE, 0 = NEGATIVE

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression()),
])

model.fit(X, y)

with open("sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)
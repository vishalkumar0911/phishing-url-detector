import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load dataset
print("📁 Loading CSV...")
df = pd.read_csv('phishing_data.csv')

# Optional: Sample a subset
df = df.sample(1000, random_state=42)

print("✅ CSV Loaded!")
X = df['URL']
y = df['label']

# Vectorize
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Save
joblib.dump(model, 'ml_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
print("✅ Model and vectorizer saved.")

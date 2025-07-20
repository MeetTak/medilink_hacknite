import pandas as pd
import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load your dataset
df = pd.read_csv("final.csv")  # Replace with your actual CSV path

# Clean side effects text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['cleaned_side_effects'] = df['side_effects'].apply(clean_text)

# Encode target labels
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['medical_condition'])

# Text vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['cleaned_side_effects'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model artifacts
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(label_encoder, 'encoder.pkl')

# Save medical_condition → rating + reviews mapping for future lookup
lookup_df = df[['medical_condition', 'rating', 'no_of_reviews']].drop_duplicates()
lookup_df.to_csv('lookup_table.csv', index=False)

print("✅ Model, vectorizer, encoder, and lookup table saved.")

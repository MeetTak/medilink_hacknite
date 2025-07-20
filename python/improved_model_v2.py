import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import re

print("🚀 Creating an improved drug prediction model v2...")

# Load the dataset
print("📊 Loading dataset...")
df = pd.read_csv('drugs_side_effects_drugs_com.csv')
print(f"✅ Dataset loaded successfully! Shape: {df.shape}")

# Basic data exploration
print("📋 First few drug names:", df['drug_name'].head().tolist())
print("📋 Sample side effects:", df['side_effects'].iloc[0][:100] + "...")

# Clean the data
print("🧹 Cleaning and preparing data...")

def clean_text(text):
    """Clean side effects text"""
    if pd.isna(text):
        return ""
    text = str(text).lower()
    # Remove special characters but keep spaces
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

# Filter and clean data
df_clean = df[['drug_name', 'side_effects']].copy()
df_clean = df_clean.dropna()
print(f"✅ After removing missing values: {len(df_clean)} rows")

# Clean the text data
df_clean['side_effects_clean'] = df_clean['side_effects'].apply(clean_text)
df_clean['drug_name_clean'] = df_clean['drug_name'].apply(lambda x: str(x).strip().lower())

# Remove entries with very short side effects (likely incomplete data)
df_clean = df_clean[df_clean['side_effects_clean'].str.len() >= 20]
print(f"✅ After removing short side effects: {len(df_clean)} rows")

# Check drug distribution
print("📊 Total unique drugs:", df_clean['drug_name_clean'].nunique())
print("📊 Drug frequency distribution:")
drug_counts = df_clean['drug_name_clean'].value_counts()
print(drug_counts.head(15))

# Instead of filtering by frequency, let's sample more drugs
# Take top drugs that appear at least once and have good side effect descriptions
unique_drugs = df_clean['drug_name_clean'].unique()
print(f"✅ Working with {len(unique_drugs)} unique drugs")

# For better training, let's create a balanced dataset
# Take up to 10 samples per drug if available
balanced_data = []
for drug in unique_drugs[:200]:  # Top 200 drugs to avoid overfitting
    drug_data = df_clean[df_clean['drug_name_clean'] == drug]
    # Take up to 10 samples per drug
    sample_size = min(10, len(drug_data))
    sampled = drug_data.sample(n=sample_size, random_state=42)
    balanced_data.append(sampled)

df_balanced = pd.concat(balanced_data, ignore_index=True)
print(f"🎯 Balanced dataset: {len(df_balanced)} samples, {df_balanced['drug_name_clean'].nunique()} unique drugs")

# Final dataset
X = df_balanced['side_effects_clean']
y = df_balanced['drug_name_clean']

print(f"🔀 Final dataset: {len(X)} samples, {len(y.unique())} unique drugs")

# Split the data
print("🔀 Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"📈 Training set: {len(X_train)} samples")
print(f"📉 Test set: {len(X_test)} samples")

# Create TF-IDF vectorizer
print("🔧 Creating TF-IDF vectorizer...")
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words='english',
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.8
)

# Fit and transform training data
print("📊 Vectorizing text data...")
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print(f"✅ Feature matrix shape: {X_train_tfidf.shape}")

# Train the model
print("🤖 Training Multinomial Naive Bayes model...")
model = MultinomialNB(alpha=0.1)
model.fit(X_train_tfidf, y_train)

# Make predictions
print("🔮 Making predictions...")
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model accuracy: {accuracy:.4f}")

# Print classification report for top classes
print("\n📊 Classification Report (top 10 classes):")
unique_classes = y_test.value_counts().head(10).index
mask = y_test.isin(unique_classes)
print(classification_report(y_test[mask], 
                          pd.Series(y_pred)[mask.values], 
                          labels=unique_classes,
                          target_names=unique_classes))

# Test with some example symptoms
print("\n🧪 Testing with example symptoms:")
test_symptoms = [
    "skin rash itching redness swelling",
    "nausea vomiting stomach pain diarrhea",
    "headache dizziness drowsiness fatigue",
    "dry mouth constipation blurred vision",
    "chest pain difficulty breathing shortness of breath"
]

for symptom in test_symptoms:
    symptom_tfidf = vectorizer.transform([symptom])
    predicted_drug = model.predict(symptom_tfidf)[0]
    prediction_proba = model.predict_proba(symptom_tfidf)[0]
    max_prob = max(prediction_proba)
    
    print(f"Symptoms: '{symptom}'")
    print(f"Predicted drug: {predicted_drug} (confidence: {max_prob:.4f})")
    print()

# Save the improved model
print("💾 Saving the improved model...")
model_data = {
    'model': model,
    'vectorizer': vectorizer,
    'accuracy': accuracy,
    'classes': model.classes_
}

with open('drug_prediction_model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

print("✅ Improved model saved successfully!")
print(f"📊 Final model stats:")
print(f"   - Training samples: {len(X_train)}")
print(f"   - Test accuracy: {accuracy:.4f}")
print(f"   - Number of drugs: {len(model.classes_)}")
print(f"   - Feature dimensions: {X_train_tfidf.shape[1]}")

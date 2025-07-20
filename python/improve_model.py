#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import re

print("🚀 Creating a new and improved drug prediction model...")

# Load the correct dataset
print("📊 Loading dataset...")
try:
    df = pd.read_csv('drugs_side_effects_drugs_com.csv')
    print(f"✅ Dataset loaded successfully! Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    exit(1)

# Check the data structure
print(f"📋 First few drug names: {df['drug_name'].head().tolist()}")
print(f"📋 Sample side effects: {df['side_effects'].iloc[0][:100]}...")

# Clean and prepare the data
print("🧹 Cleaning and preparing data...")

# Remove rows with missing side effects or drug names
df_clean = df.dropna(subset=['drug_name', 'side_effects'])
print(f"✅ After removing missing values: {df_clean.shape[0]} rows")

# Clean side effects text
def clean_text(text):
    if pd.isna(text):
        return ""
    # Convert to string and lowercase
    text = str(text).lower()
    # Remove special characters and extra spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df_clean['side_effects_clean'] = df_clean['side_effects'].apply(clean_text)
df_clean['drug_name_clean'] = df_clean['drug_name'].apply(lambda x: str(x).strip())

# Remove empty or very short side effects
df_clean = df_clean[df_clean['side_effects_clean'].str.len() > 10]
print(f"✅ After removing short side effects: {df_clean.shape[0]} rows")

# Get unique drugs and their counts
drug_counts = df_clean['drug_name_clean'].value_counts()
print(f"📊 Total unique drugs: {len(drug_counts)}")
print(f"📊 Top 10 drugs by frequency:")
print(drug_counts.head(10))

# Keep drugs that appear at least 2 times to have enough training data
min_drug_frequency = 2
drugs_to_keep = drug_counts[drug_counts >= min_drug_frequency].index
df_filtered = df_clean[df_clean['drug_name_clean'].isin(drugs_to_keep)]
print(f"✅ After filtering (min {min_drug_frequency} occurrences): {df_filtered.shape[0]} rows")
print(f"✅ Number of unique drugs: {df_filtered['drug_name_clean'].nunique()}")

# Prepare features and labels
X = df_filtered['side_effects_clean'].values
y = df_filtered['drug_name_clean'].values

print(f"🎯 Final dataset: {len(X)} samples, {len(np.unique(y))} unique drugs")

# Split the data
print("🔀 Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"📚 Training set: {len(X_train)} samples")
print(f"🧪 Test set: {len(X_test)} samples")

# Create TF-IDF vectorizer with better parameters
print("🔤 Creating TF-IDF vectorizer...")
vectorizer = TfidfVectorizer(
    max_features=5000,  # Increased vocabulary
    ngram_range=(1, 2),  # Include bigrams
    min_df=2,  # Word must appear in at least 2 documents
    max_df=0.95,  # Ignore words that appear in more than 95% of documents
    stop_words='english',
    lowercase=True
)

# Fit and transform the training data
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print(f"✅ TF-IDF shape: {X_train_tfidf.shape}")
print(f"✅ Vocabulary size: {len(vectorizer.vocabulary_)}")

# Train the model
print("🤖 Training Naive Bayes model...")
nb_model = MultinomialNB(alpha=0.1)  # Lower smoothing parameter
nb_model.fit(X_train_tfidf, y_train)

# Make predictions
print("🔮 Making predictions...")
y_pred = nb_model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Model Accuracy: {accuracy:.3f} ({accuracy*100:.1f}%)")

# Test with sample inputs
print("\n🧪 Testing model with sample symptoms...")
test_symptoms = [
    "headache and nausea",
    "fever and cough", 
    "stomach pain and diarrhea",
    "skin rash and itching",
    "dizziness and fatigue",
    "muscle pain and weakness"
]

for symptom in test_symptoms:
    symptom_clean = clean_text(symptom)
    symptom_tfidf = vectorizer.transform([symptom_clean])
    
    # Get prediction
    prediction = nb_model.predict(symptom_tfidf)[0]
    
    # Get probabilities
    proba = nb_model.predict_proba(symptom_tfidf)
    confidence = np.max(proba) * 100
    
    # Get top 3 predictions
    top_indices = np.argsort(proba[0])[-3:][::-1]
    top_drugs = [nb_model.classes_[i] for i in top_indices]
    top_confidences = [proba[0][i] * 100 for i in top_indices]
    
    print(f"\n📝 Symptom: '{symptom}'")
    print(f"💊 Predicted drug: {prediction} ({confidence:.1f}%)")
    print(f"🏆 Top 3: {', '.join([f'{drug} ({conf:.1f}%)' for drug, conf in zip(top_drugs, top_confidences)])}")

# Save the improved model
print("\n💾 Saving the improved model...")
model_data = {
    'model': nb_model,
    'vectorizer': vectorizer,
    'accuracy': accuracy,
    'drug_count': len(np.unique(y)),
    'sample_count': len(X)
}

with open('drug_prediction_model_improved.pkl', 'wb') as file:
    pickle.dump(model_data, file)

print("✅ Improved model saved as 'drug_prediction_model_improved.pkl'")

# Create a backup of the old model and replace it
import os
if os.path.exists('drug_prediction_model.pkl'):
    os.rename('drug_prediction_model.pkl', 'drug_prediction_model_old.pkl')
    print("📋 Old model backed up as 'drug_prediction_model_old.pkl'")

os.rename('drug_prediction_model_improved.pkl', 'drug_prediction_model.pkl')
print("🔄 New model is now active!")

print("\n🎉 Model improvement complete!")
print(f"📊 Final Statistics:")
print(f"   • Accuracy: {accuracy:.3f} ({accuracy*100:.1f}%)")
print(f"   • Unique drugs: {len(np.unique(y))}")
print(f"   • Training samples: {len(X)}")
print(f"   • Vocabulary size: {len(vectorizer.vocabulary_)}")

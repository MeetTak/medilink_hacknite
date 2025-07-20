#!/usr/bin/env python3

import pickle
import numpy as np

print("Testing model predictions in detail...")

# Load the model
with open("drug_prediction_model.pkl", 'rb') as file:
    loaded_data = pickle.load(file)
    model = loaded_data['model']
    vectorizer = loaded_data['vectorizer']

print(f"Model classes count: {len(model.classes_)}")
print(f"First 10 classes: {model.classes_[:10]}")
print(f"Vectorizer vocabulary size: {len(vectorizer.vocabulary_)}")

# Test different symptoms
test_symptoms = [
    "headache and nausea",
    "fever and cough", 
    "stomach pain",
    "back pain",
    "sore throat",
    "dizziness",
    "rash",
    "fatigue"
]

print("\n" + "="*50)
print("TESTING DIFFERENT SYMPTOMS:")
print("="*50)

for symptom in test_symptoms:
    print(f"\nTesting: '{symptom}'")
    
    # Transform the input
    symptom_tfidf = vectorizer.transform([symptom])
    print(f"TF-IDF vector shape: {symptom_tfidf.shape}")
    print(f"TF-IDF non-zero elements: {symptom_tfidf.nnz}")
    
    # Get prediction
    prediction = model.predict(symptom_tfidf)
    print(f"Prediction: {prediction[0]}")
    
    # Get probabilities
    if hasattr(model, 'predict_proba'):
        proba = model.predict_proba(symptom_tfidf)
        max_prob = np.max(proba)
        print(f"Max probability: {max_prob:.6f}")
        
        # Get top 5 predictions
        top_indices = np.argsort(proba[0])[-5:][::-1]
        print("Top 5 predictions:")
        for i, idx in enumerate(top_indices):
            drug = model.classes_[idx]
            confidence = proba[0][idx]
            print(f"  {i+1}. {drug}: {confidence:.6f} ({confidence*100:.3f}%)")

print("\n" + "="*50)
print("CHECKING MODEL TRAINING QUALITY:")
print("="*50)

# Check if all predictions are the same
all_predictions = []
for symptom in test_symptoms:
    symptom_tfidf = vectorizer.transform([symptom])
    pred = model.predict(symptom_tfidf)[0]
    all_predictions.append(pred)

unique_predictions = set(all_predictions)
print(f"Unique predictions for {len(test_symptoms)} different symptoms: {len(unique_predictions)}")
print(f"All predictions: {all_predictions}")

if len(unique_predictions) == 1:
    print("⚠️  WARNING: Model is predicting the same drug for all symptoms!")
    print("   This suggests the model is poorly trained or overfitted.")
else:
    print("✅ Model is making different predictions for different symptoms.")

# Check vocabulary relevance
print(f"\nSample vocabulary words: {list(vectorizer.vocabulary_.keys())[:20]}")

# Check feature importance for the most common prediction
most_common_pred = all_predictions[0]
print(f"\nMost common prediction: {most_common_pred}")

# Test with very specific medical terms
medical_terms = [
    "acetaminophen side effects",
    "ibuprofen adverse reactions", 
    "aspirin contraindications",
    "paracetamol toxicity"
]

print(f"\nTesting with specific medical terms:")
for term in medical_terms:
    symptom_tfidf = vectorizer.transform([term])
    prediction = model.predict(symptom_tfidf)
    proba = model.predict_proba(symptom_tfidf)
    max_prob = np.max(proba)
    print(f"'{term}' -> {prediction[0]} ({max_prob*100:.3f}%)")

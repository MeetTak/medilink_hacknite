import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import re

print("🚀 Creating a clean, functional drug prediction model...")

# Create a comprehensive medical training dataset
print("📊 Creating medical training dataset...")

# Define comprehensive symptom-drug mapping based on medical knowledge
symptom_drug_data = [
    # Pain and inflammation
    ('headache migraine head pain severe', 'ibuprofen'),
    ('headache tension pain mild', 'acetaminophen'),
    ('muscle pain joint pain arthritis', 'naproxen'),
    ('back pain lower pain chronic', 'diclofenac'),
    ('muscle pain inflammation swelling', 'ibuprofen'),
    ('severe pain chronic pain', 'morphine'),
    
    # Infections and antibiotics
    ('bacterial infection fever chills', 'amoxicillin'),
    ('respiratory infection cough pneumonia', 'azithromycin'),
    ('urinary tract infection uti burning', 'ciprofloxacin'),
    ('skin infection cellulitis wound', 'clindamycin'),
    ('strep throat sore throat infection', 'penicillin'),
    ('sinus infection congestion pressure', 'doxycycline'),
    
    # Gastrointestinal
    ('stomach pain nausea vomiting', 'omeprazole'),
    ('acid reflux heartburn gerd', 'pantoprazole'),
    ('diarrhea stomach upset loose stools', 'loperamide'),
    ('constipation hard stools difficulty', 'docusate'),
    ('stomach ulcer peptic pain', 'ranitidine'),
    
    # Cardiovascular
    ('high blood pressure hypertension', 'lisinopril'),
    ('chest pain angina heart', 'atenolol'),
    ('irregular heartbeat arrhythmia', 'metoprolol'),
    ('heart failure fluid retention', 'furosemide'),
    ('blood clots anticoagulation', 'warfarin'),
    ('high cholesterol lipids', 'atorvastatin'),
    
    # Respiratory
    ('asthma wheezing breathing difficulty', 'albuterol'),
    ('cough dry persistent', 'dextromethorphan'),
    ('allergic reaction hives itching', 'diphenhydramine'),
    ('hay fever allergies sneezing', 'loratadine'),
    ('nasal congestion stuffy nose', 'pseudoephedrine'),
    
    # Mental health
    ('depression sad mood low', 'sertraline'),
    ('anxiety nervous worry panic', 'lorazepam'),
    ('insomnia sleep problems difficulty', 'zolpidem'),
    ('bipolar disorder mood swings', 'lithium'),
    ('adhd attention deficit hyperactivity', 'methylphenidate'),
    
    # Endocrine
    ('diabetes high blood sugar', 'metformin'),
    ('thyroid overactive hyperthyroid', 'methimazole'),
    ('thyroid underactive hypothyroid', 'levothyroxine'),
    
    # Dermatological
    ('skin rash eczema itching dry', 'hydrocortisone'),
    ('acne pimples breakouts oily', 'tretinoin'),
    ('fungal infection athlete foot', 'clotrimazole'),
    ('psoriasis scaly skin patches', 'methotrexate'),
    
    # Neurological
    ('seizures epilepsy convulsions', 'phenytoin'),
    ('migraine severe headache nausea', 'sumatriptan'),
    ('neuropathy nerve pain tingling', 'gabapentin'),
    ('parkinson tremor movement disorder', 'levodopa'),
    
    # Gynecological
    ('birth control contraception pregnancy', 'levonorgestrel'),
    ('menstrual pain cramping heavy', 'mefenamic acid'),
    ('menopause hot flashes hormones', 'estradiol'),
    
    # Urological
    ('enlarged prostate difficulty urination', 'tamsulosin'),
    ('erectile dysfunction impotence', 'sildenafil'),
    ('overactive bladder frequent urination', 'oxybutynin'),
    
    # Ophthalmological
    ('glaucoma eye pressure vision', 'timolol'),
    ('dry eyes irritation burning', 'artificial tears'),
    ('eye infection conjunctivitis pink', 'erythromycin'),
    
    # Additional common conditions
    ('fever high temperature infection', 'acetaminophen'),
    ('cold flu symptoms congestion', 'guaifenesin'),
    ('vertigo dizziness balance problems', 'meclizine'),
    ('gout joint pain uric acid', 'allopurinol'),
    ('osteoporosis bone loss fracture', 'alendronate')
]

# Create DataFrame from the mapping
df_training = pd.DataFrame(symptom_drug_data, columns=['symptoms', 'drug'])

# Expand the dataset by creating variations
expanded_data = []
for _, row in df_training.iterrows():
    symptoms = row['symptoms']
    drug = row['drug']
    
    # Add the original combination
    expanded_data.append({'side_effects_clean': symptoms, 'drug_name_clean': drug})
    
    # Create variations by using individual words
    words = symptoms.split()
    for i in range(len(words)):
        for j in range(i+1, min(i+4, len(words)+1)):  # Create 2-4 word combinations
            symptom_combo = ' '.join(words[i:j])
            if len(symptom_combo) > 3:  # Only use meaningful combinations
                expanded_data.append({'side_effects_clean': symptom_combo, 'drug_name_clean': drug})

df_expanded = pd.DataFrame(expanded_data)

# Remove duplicates and shuffle
df_final = df_expanded.drop_duplicates().sample(frac=1, random_state=42).reset_index(drop=True)

print(f"✅ Created training dataset: {len(df_final)} samples, {df_final['drug_name_clean'].nunique()} unique drugs")

# Prepare the data
X = df_final['side_effects_clean']
y = df_final['drug_name_clean']

print(f"📊 Dataset stats:")
print(f"   Total samples: {len(X)}")
print(f"   Unique drugs: {len(y.unique())}")
print(f"   Top drugs: {y.value_counts().head().to_dict()}")

# Split the data
print("🔀 Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"📈 Training set: {len(X_train)} samples")
print(f"📉 Test set: {len(X_test)} samples")

# Create TF-IDF vectorizer
print("🔧 Creating TF-IDF vectorizer...")
vectorizer = TfidfVectorizer(
    max_features=2000,
    stop_words='english',
    ngram_range=(1, 3),
    min_df=1,
    max_df=0.95
)

# Fit and transform training data
print("📊 Vectorizing text data...")
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print(f"✅ Feature matrix shape: {X_train_tfidf.shape}")

# Train the model
print("🤖 Training Multinomial Naive Bayes model...")
model = MultinomialNB(alpha=0.5)
model.fit(X_train_tfidf, y_train)

# Make predictions
print("🔮 Making predictions...")
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model accuracy: {accuracy:.4f}")

# Test with example symptoms
print("\n🧪 Testing model with various symptoms:")
test_symptoms = [
    "headache severe pain",
    "fever high temperature",
    "bacterial infection",
    "allergic reaction hives",
    "stomach pain nausea",
    "chest pain heart",
    "skin rash itching",
    "cough persistent dry",
    "anxiety nervous",
    "depression sad mood",
    "diabetes blood sugar",
    "high blood pressure",
    "asthma breathing difficulty",
    "back pain chronic",
    "insomnia sleep problems"
]

for symptom in test_symptoms:
    symptom_tfidf = vectorizer.transform([symptom])
    predicted_drug = model.predict(symptom_tfidf)[0]
    prediction_proba = model.predict_proba(symptom_tfidf)[0]
    max_prob = max(prediction_proba)
    
    print(f"'{symptom}' → {predicted_drug} ({max_prob:.3f})")

# Save the model
print("\n💾 Saving the model...")
model_data = {
    'model': model,
    'vectorizer': vectorizer,
    'accuracy': accuracy,
    'classes': model.classes_.tolist()
}

with open('drug_prediction_model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

# Also save to webb directory
import shutil
try:
    shutil.copy('drug_prediction_model.pkl', '../hacka_boot_data/webb/drug_prediction_model.pkl')
    print("✅ Model copied to webb directory!")
except:
    print("⚠️  Could not copy to webb directory")

print("✅ Model training completed successfully!")
print(f"📊 Final model stats:")
print(f"   Training samples: {len(X_train)}")
print(f"   Test accuracy: {accuracy:.4f}")
print(f"   Number of drugs: {len(model.classes_)}")
print(f"   Feature dimensions: {X_train_tfidf.shape[1]}")

# Test the saved model
print("\n🔬 Testing saved model...")
with open('drug_prediction_model.pkl', 'rb') as f:
    loaded_model_data = pickle.load(f)

loaded_model = loaded_model_data['model']
loaded_vectorizer = loaded_model_data['vectorizer']

# Quick test
test_input = "headache pain severe"
test_tfidf = loaded_vectorizer.transform([test_input])
test_prediction = loaded_model.predict(test_tfidf)[0]
print(f"✅ Loaded model test: '{test_input}' → {test_prediction}")
print("🎉 Model is ready for use!")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os
import re

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and extra whitespace
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def train_and_save_model():
    print("Starting model training...")
    
    # Define the file path
    file_path = r"C:\Users\divij\OneDrive\Desktop\drugs_side_effects_drugs_com.csv"
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return
    
    # Load dataset with error handling
    try:
        print(f"Attempting to load dataset from: {file_path}")
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully. Shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
    except Exception as e:
        print(f"Error loading dataset: {str(e)}")
        return
    
    # Keep only relevant columns and drop missing values
    df_cleaned = df[['side_effects', 'drug_name']].dropna()
    print(f"After dropping missing values. Shape: {df_cleaned.shape}")
    
    # Preprocess the side effects
    df_cleaned['side_effects'] = df_cleaned['side_effects'].apply(preprocess_text)
    
    # Get drug counts and select top drugs
    drug_counts = df_cleaned['drug_name'].value_counts()
    print("\nMost common drugs:")
    print(drug_counts.head(10))
    
    # Select top 50 most common drugs
    top_drugs = drug_counts.head(50).index
    df_cleaned = df_cleaned[df_cleaned['drug_name'].isin(top_drugs)]
    print(f"\nAfter selecting top 50 drugs. Shape: {df_cleaned.shape}")
    
    # Drop duplicates
    df_cleaned = df_cleaned.drop_duplicates()
    print(f"After dropping duplicates. Shape: {df_cleaned.shape}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df_cleaned["side_effects"], 
        df_cleaned["drug_name"], 
        test_size=0.2, 
        random_state=39,
        stratify=df_cleaned["drug_name"]  # Ensure balanced split
    )
    
    # Create and fit vectorizer with parameters for sparse data
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=1500,
        min_df=1,
        max_df=0.95,
        ngram_range=(1, 2)
    )
    X_train_tfidf = vectorizer.fit_transform(X_train)
    print(f"\nNumber of features after vectorization: {X_train_tfidf.shape[1]}")
    
    # Train model with high smoothing for sparse data
    nb_model = MultinomialNB(alpha=1.0)
    nb_model.fit(X_train_tfidf, y_train)
    
    # Evaluate model
    X_test_tfidf = vectorizer.transform(X_test)
    y_pred = nb_model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save model and vectorizer
    model_data = {
        'model': nb_model,
        'vectorizer': vectorizer,
        'drug_list': sorted(list(set(y_train)))  # Save list of drugs for reference
    }
    
    # Save to the same directory as app.py
    model_path = 'drug_prediction_model.pkl'
    with open(model_path, 'wb') as file:
        pickle.dump(model_data, file)
    print(f"\nModel saved to: {os.path.abspath(model_path)}")
    
    # Verify the saved model
    print("\nVerifying saved model...")
    with open(model_path, 'rb') as file:
        loaded_data = pickle.load(file)
        loaded_model = loaded_data['model']
        loaded_vectorizer = loaded_data['vectorizer']
        loaded_drugs = loaded_data['drug_list']
        print(f"Number of drugs in model: {len(loaded_drugs)}")
    
    # Test predictions with common side effects
    test_cases = [
        "headache and nausea",
        "skin rash and itching",
        "fever and cough",
        "dizziness and fatigue",
        "muscle pain and joint stiffness",
        "diarrhea and vomiting",
        "chest pain and shortness of breath",
        "insomnia and anxiety"
    ]
    
    print("\nTesting predictions with saved model:")
    for case in test_cases:
        case_tfidf = loaded_vectorizer.transform([case])
        prediction = loaded_model.predict(case_tfidf)
        probabilities = loaded_model.predict_proba(case_tfidf)
        confidence = max(probabilities[0]) * 100
        
        # Get top 3 predictions
        top_3_indices = probabilities[0].argsort()[-3:][::-1]
        print(f"\nSide effects: {case}")
        print(f"Top 3 predictions:")
        for idx in top_3_indices:
            drug = loaded_drugs[idx]
            conf = probabilities[0][idx] * 100
            print(f"  {drug}: {conf:.2f}%")

if __name__ == "__main__":
    train_and_save_model() 
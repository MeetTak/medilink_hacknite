import streamlit as st
import joblib
import pandas as pd
import re

# Load saved model and encoders
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
encoder = joblib.load("encoder.pkl")
lookup_df = pd.read_csv("lookup_table.csv")

# Text cleaner
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Title
st.title("🩺 Medical Condition Predictor from Side Effects")

# Input from user
user_input = st.text_area("Enter Side Effects:", height=200)

# Predict button
if st.button("Predict Condition"):
    if user_input.strip() == "":
        st.warning("Please enter some side effects.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        pred = model.predict(vectorized)
        pred_label = encoder.inverse_transform(pred)[0]

        st.success(f"🔍 Predicted Medical Condition: **{pred_label}**")

        # Show rating and reviews
        match = lookup_df[lookup_df['medical_condition'] == pred_label]
        if not match.empty:
            rating = match['rating'].values[0]
            reviews = match['no_of_reviews'].values[0]
            st.info(f"⭐ Rating: {rating}/10\n💬 Reviews: {reviews}")
        else:
            st.info("No rating or review data available.")

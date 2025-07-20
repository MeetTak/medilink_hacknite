from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Try to load the model from different possible locations
model_paths = [
    "./drug_prediction_model.pkl",
    "../drug_prediction_model.pkl",
    "../../drug_prediction_model.pkl"
]

nb_model = None
vectorizer = None

for path in model_paths:
    try:
        if os.path.exists(path):
            with open(path, 'rb') as file:
                loaded_data = pickle.load(file)
                nb_model = loaded_data['model']
                vectorizer = loaded_data['vectorizer']
                print(f"Model loaded successfully from {path}")
                break
    except Exception as e:
        print(f"Failed to load model from {path}: {e}")
        continue

if nb_model is None:
    print("Warning: Could not load the AI model. Using fallback predictions.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        side_effects = data.get('side_effects', '')
        
        if not side_effects:
            return jsonify({'error': 'No side effects provided'}), 400
        
        if nb_model and vectorizer:
            # Make prediction using the AI model
            side_effect_tfidf = vectorizer.transform([side_effects])
            prediction = nb_model.predict(side_effect_tfidf)
            
            # Get prediction probabilities for confidence
            if hasattr(nb_model, 'predict_proba'):
                proba = nb_model.predict_proba(side_effect_tfidf)
                confidence = np.max(proba) * 100
                
                # Get top 3 predictions
                top_indices = np.argsort(proba[0])[-3:][::-1]
                top_predictions = [nb_model.classes_[i] for i in top_indices]
                top_confidences = [proba[0][i] * 100 for i in top_indices]
            else:
                confidence = 85.0
                top_predictions = [prediction[0]]
                top_confidences = [confidence]
            
            return jsonify({
                'predicted_drug': prediction[0],
                'confidence': f"{confidence:.1f}%",
                'top_predictions': [
                    {'drug': drug, 'confidence': f"{conf:.1f}%"} 
                    for drug, conf in zip(top_predictions, top_confidences)
                ]
            })
        else:
            # Fallback prediction based on keywords
            side_effects_lower = side_effects.lower()
            
            if any(keyword in side_effects_lower for keyword in ['headache', 'pain', 'ache']):
                return jsonify({
                    'predicted_drug': 'Acetaminophen',
                    'confidence': '75%',
                    'top_predictions': [
                        {'drug': 'Acetaminophen', 'confidence': '75%'},
                        {'drug': 'Ibuprofen', 'confidence': '65%'}
                    ]
                })
            elif any(keyword in side_effects_lower for keyword in ['nausea', 'vomit', 'stomach']):
                return jsonify({
                    'predicted_drug': 'Ondansetron',
                    'confidence': '70%',
                    'top_predictions': [
                        {'drug': 'Ondansetron', 'confidence': '70%'},
                        {'drug': 'Metoclopramide', 'confidence': '60%'}
                    ]
                })
            elif any(keyword in side_effects_lower for keyword in ['fever', 'temperature']):
                return jsonify({
                    'predicted_drug': 'Paracetamol',
                    'confidence': '80%',
                    'top_predictions': [
                        {'drug': 'Paracetamol', 'confidence': '80%'},
                        {'drug': 'Aspirin', 'confidence': '70%'}
                    ]
                })
            else:
                return jsonify({
                    'predicted_drug': 'Consult healthcare provider',
                    'confidence': '50%',
                    'top_predictions': [
                        {'drug': 'General consultation recommended', 'confidence': '50%'}
                    ]
                })
                
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    model_status = "loaded" if nb_model else "not loaded"
    return jsonify({
        'status': 'healthy',
        'model_status': model_status
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)

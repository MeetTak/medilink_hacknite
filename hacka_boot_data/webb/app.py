from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)

# Load the model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), 'drug_prediction_model.pkl')
try:
    with open(model_path, 'rb') as file:
        loaded_data = pickle.load(file)
        nb_model = loaded_data['model']
        vectorizer = loaded_data['vectorizer']
        print(f"✅ Model loaded successfully from {model_path}")
        print(f"📊 Model has {len(loaded_data['classes'])} drug classes")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    nb_model = None
    vectorizer = None

@app.route('/predict', methods=['POST'])
def predict():
    if nb_model is None or vectorizer is None:
        return jsonify({'error': 'Model not loaded properly'}), 500
    
    data = request.json
    side_effects = data.get('side_effects', '')
    
    if not side_effects:
        return jsonify({'error': 'No side effects provided'}), 400
    
    try:
        # Clean the input
        side_effects_clean = side_effects.lower().strip()
        
        # Make prediction
        side_effect_tfidf = vectorizer.transform([side_effects_clean])
        prediction = nb_model.predict(side_effect_tfidf)
        prediction_proba = nb_model.predict_proba(side_effect_tfidf)
        confidence = max(prediction_proba[0])
        
        return jsonify({
            'predicted_drug': prediction[0],
            'confidence': float(confidence),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

if __name__ == '__main__':
    print("🚀 Starting Flask AI Server...")
    print("📡 Server will run on http://localhost:8051")
    app.run(debug=True, host='0.0.0.0', port=8051)
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load the model and vectorizer
with open(r"D:\Downloads\drug_prediction_model (1).pkl", 'rb') as file:
    loaded_data = pickle.load(file)
    nb_model = loaded_data['model']
    vectorizer = loaded_data['vectorizer']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    side_effects = data.get('side_effects', '')
    
    if not side_effects:
        return jsonify({'error': 'No side effects provided'}), 400
    
    # Make prediction
    side_effect_tfidf = vectorizer.transform([side_effects])
    prediction = nb_model.predict(side_effect_tfidf)
    
    return jsonify({'predicted_drug': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
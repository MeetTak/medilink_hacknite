#!/usr/bin/env python3

import pickle
import sys

print("Checking model file...")

try:
    with open("drug_prediction_model.pkl", 'rb') as file:
        loaded_data = pickle.load(file)
        print("Model file loaded successfully!")
        print("Keys in model data:", list(loaded_data.keys()) if isinstance(loaded_data, dict) else "Not a dictionary")
        
        if isinstance(loaded_data, dict):
            for key, value in loaded_data.items():
                print(f"{key}: {type(value)}")
        else:
            print(f"Model type: {type(loaded_data)}")
            
except Exception as e:
    print(f"Error loading model: {e}")
    print(f"Python path: {sys.path}")
    
print("\nInstalled packages:")
try:
    import sklearn
    print(f"sklearn version: {sklearn.__version__}")
except ImportError as e:
    print(f"sklearn import error: {e}")
    
try:
    import scikit_learn
    print("scikit_learn imported successfully")
except ImportError as e:
    print(f"scikit_learn import error: {e}")

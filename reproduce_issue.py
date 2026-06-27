
import os
from tensorflow.keras.models import load_model

filepath = 'model2.h5'
print(f"Attempting to load {filepath}...")

if not os.path.exists(filepath):
    print(f"File {filepath} does not exist.")
else:
    print(f"File size: {os.path.getsize(filepath)} bytes")
    try:
        model = load_model(filepath)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Failed to load model: {e}")

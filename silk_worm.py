import numpy as np
import os
import tensorflow as tf

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# NOTE: The filename 'modellll.h5' seems unusual. Please double-check if this is the correct name for your silkworm model file.
# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, 'modellll.h5')
try:
    model = load_model(filepath)
    print("Silkworm model loaded successfully.")
except OSError:
    print(f"Error: Model file not found at '{filepath}'.")
    print("Please ensure the model file exists in the correct directory.")
    # This will prevent the app from crashing if the model is missing.
    model = None

SILKWORM_CLASSES = {
    0: ("Silkworm - Flacheria Disease", 'silkworm_Flacheria.html'),
    1: ("Silkworm - Grasseria Disease", 'silkworm_Grasseria.html'),
    2: ("Silkworm - Muscardin Disease", 'silkworm_muscardin.html'),
    3: ("Silkworm - Pabrin Disease", 'silkworm_pabrin.html'),
    4: ("Silkworm - healthy", 'un_disease.html')
}

def pred_silkworm_diseases(image_path):
  if model is None:
      print("Model is not loaded. Cannot perform prediction.")
      return "Model not loaded", "error.html"

  test_image = load_img(image_path, target_size=(128, 128))
  print("Got Image for prediction")
  test_image = img_to_array(test_image)/255.0
  test_image = np.expand_dims(test_image, axis=0)
  result = model.predict(test_image)
  print('Raw result = ', result)
  pred_index = np.argmax(result)
  print("Prediction index:", pred_index)

  # The 'healthy' class is part of the model, so we rely on its prediction.
  return SILKWORM_CLASSES.get(pred_index, ("Unknown prediction", "error.html"))

import tensorflow as tf
import cv2
import numpy as np
import os
import json

def predict_disease(model_path, image_path, class_indices_path):
    """Predict the disease of a given leaf image."""
    model = tf.keras.models.load_model(model_path)

    # Load correct class labels from saved file
    with open(class_indices_path, 'r') as f:
        class_indices = json.load(f)
    
    # Reverse mapping: {0: 'class_name'}
    class_labels = {v: k for k, v in class_indices.items()}

    # Check if image exists
    if not os.path.exists(image_path):
        print(f"❌ Error: The file '{image_path}' was not found.")
        return None

    # Read and preprocess the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Error: Unable to read '{image_path}'. Check the file format.")
        return None

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (64, 64))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)

    predicted_label = class_labels.get(predicted_class, "Unknown")
    return predicted_label, confidence

if __name__ == "__main__":
    image_path = 'src/sample_leaf.jpg'  # You can change this
    model_path = 'models/plant_disease_model.h5'
    class_indices_path = 'models/class_indices.json'

    result = predict_disease(model_path, image_path, class_indices_path)

    if result:
        predicted_label, confidence = result
        print(f"✅ Predicted Disease: {predicted_label} ({confidence*100:.2f}% confidence)")

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import json

def evaluate_model(model_path, test_dir):
    """Evaluate the trained model using test dataset."""
    model = tf.keras.models.load_model(model_path)

    # Load class indices for consistency
    with open('models/class_indices.json') as f:
        saved_class_indices = json.load(f)
    print("✅ Loaded Class Indices:", saved_class_indices)

    # Sort classes based on index to maintain correct order
    class_order = [k for k, v in sorted(saved_class_indices.items(), key=lambda item: item[1])]

    test_datagen = ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(64, 64),
        batch_size=8,
        class_mode='categorical',
        shuffle=False,  # Important: don't shuffle for evaluation
        classes=class_order  # Ensures correct mapping
    )

    # Print new check
    print("✅ Test generator class indices (post override):", test_generator.class_indices)

    loss, accuracy = model.evaluate(test_generator)
    print(f"🎯 Test Accuracy: {accuracy:.2f}")
    return accuracy

if __name__ == "__main__":
    evaluate_model('models/best_model.h5', 'dataset/val')

import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_and_preprocess_image(image_path, target_size=(64, 64)):
    """Load an image, resize it, and normalize pixel values."""
    img = cv2.imread(image_path)
    img = cv2.resize(img, target_size)
    img = img / 255.0  # Normalize pixel values
    return img

def augment_data(train_dir, target_size=(64, 64), batch_size=32, subset='training'):
    """Perform data augmentation on training images with optional dataset split."""
    datagen = ImageDataGenerator(
        validation_split=0.2,  # 80% training, 20% validation
        rotation_range=30,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    return datagen.flow_from_directory(
        train_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset=subset,  # 'training' or 'validation'
        shuffle=True
    )

if __name__ == "__main__":
    print("Preprocessing module ready!")

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from sklearn.utils.class_weight import compute_class_weight
import numpy as np
import json
import os
from preprocessing import augment_data

def build_model(input_shape=(64, 64, 3), num_classes=17):
    model = Sequential([
        Conv2D(64, (3, 3), activation='relu', input_shape=input_shape),
        BatchNormalization(),
        MaxPooling2D((2, 2)),

        Conv2D(128, (3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),

        Conv2D(256, (3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),

        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.6),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def get_class_weights(train_data):
    labels = train_data.classes
    class_weights = compute_class_weight(class_weight='balanced', classes=np.unique(labels), y=labels)
    return dict(enumerate(class_weights))

if __name__ == "__main__":
    # Load datasets
    train_data = augment_data('dataset/train', subset='training')
    val_data = augment_data('dataset/train', subset='validation')

    # Save class indices for consistency
    os.makedirs("models", exist_ok=True)
    with open("models/class_indices.json", "w") as f:
        json.dump(train_data.class_indices, f)
    print("✅ Class indices saved to models/class_indices.json")

    # Build and compile model
    model = build_model(num_classes=len(train_data.class_indices))

    # Compute class weights
    class_weights = get_class_weights(train_data)
    print("⚖️ Computed Class Weights:", class_weights)

    # Callbacks for training
    callbacks = [
        EarlyStopping(monitor='val_accuracy', patience=4, restore_best_weights=True, verbose=1),
        ReduceLROnPlateau(monitor='val_accuracy', factor=0.5, patience=2, min_lr=1e-6, verbose=1),
        ModelCheckpoint('models/best_model.h5', monitor='val_accuracy', save_best_only=True, verbose=1)
    ]

    # Train the model
    model.fit(
        train_data,
        validation_data=val_data,
        epochs=25,
        class_weight=class_weights,
        callbacks=callbacks
    )

    # Save final model (last state of training)
    model.save('models/plant_disease_model.h5')
    print("✅ Model training completed and saved!")

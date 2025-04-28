import os

model_path = 'models/plant_disease_model.h5'

if os.path.exists(model_path):
    print("Model file found!")
else:
    print("Model file NOT found!")

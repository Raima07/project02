import os

print(" Step 1: Running Data Preprocessing...")
os.system("python src/preprocessing.py")

print("\n Step 2: Training the Model...")
os.system("python src/train_model.py")

print("\n Step 3: Evaluating the Model...")
os.system("python src/evaluate_model.py")

print("\n Step 4: Making a Prediction...")
os.system("python src/predict.py")

print("\n All steps completed successfully!")

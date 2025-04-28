import os

train_dir = "dataset/train"
val_dir = "dataset/val"

def check_dataset(path, dataset_name):
    if os.path.exists(path) and len(os.listdir(path)) > 0:
        print(f"✅ {dataset_name} dataset found! Ready for training.")
        print(f"📂 Classes found in {dataset_name}:", os.listdir(path))
    else:
        print(f"❌ {dataset_name} dataset is missing or empty. Check the folder structure.")

check_dataset(train_dir, "Train")
check_dataset(val_dir, "Validation")

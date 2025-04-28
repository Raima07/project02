import os
from collections import Counter

def count_images_per_class(base_dir):
    class_counts = {}
    for class_name in os.listdir(base_dir):
        class_path = os.path.join(base_dir, class_name)
        if os.path.isdir(class_path):
            num_images = len([f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))])
            class_counts[class_name] = num_images
    return class_counts

if __name__ == "__main__":
    train_counts = count_images_per_class('dataset/train')
    val_counts = count_images_per_class('dataset/val')

    print("Train class distribution:")
    print(train_counts)

    print("\nValidation class distribution:")
    print(val_counts)

# 🌿 Plant Disease Detection

## 📌 Project Overview
This project is a **Plant Disease Detection System** that uses **Convolutional Neural Networks (CNNs)** to classify plant leaf images and detect diseases. The model is trained using **TensorFlow and Keras** and can predict the disease of a given plant leaf image.

## 📂 Project Structure
```
plant_disease_detection/
│── dataset/                  # Folder to store images (if applicable)
│── models/                   # To save trained models
│── src/                      # Source code files
│   │── data_preprocessing.py  # Handles dataset loading & preprocessing
│   │── model.py               # Defines and trains the CNN model
│   │── train.py               # Runs the training process
│   │── evaluate.py            # Evaluates the model performance
│   │── predict.py             # Loads the model and predicts diseases
│── app.py                     # Main file for running predictions
│── requirements.txt           # Lists dependencies
│── README.md                  # Project documentation
```

## 🛠️ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/plant-disease-detection.git
   cd plant-disease-detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Dataset**
   - Place images in the `dataset/` folder.
   - Organize images into subfolders, where each subfolder represents a different plant disease.

4. **Train the Model**
   ```bash
   python src/train.py
   ```

5. **Evaluate Performance**
   ```bash
   python src/evaluate.py
   ```

6. **Test Prediction on a Single Image**
   ```bash
   python src/predict.py --image test_leaf.jpg
   ```

7. **Run the Web App**
   ```bash
   streamlit run app.py
   ```

## 🔬 How It Works
- **Data Preprocessing** (`data_preprocessing.py`): Loads and augments images.
- **Model Definition** (`model.py`): Defines a CNN for plant disease classification.
- **Training** (`train.py`): Trains the model and saves it.
- **Evaluation** (`evaluate.py`): Plots accuracy and loss.
- **Prediction** (`predict.py`): Uses the trained model to classify plant diseases.
- **Web App** (`app.py`): Provides a simple UI to upload an image and get predictions.

## 🚀 Future Improvements
- Fine-tune the CNN for better accuracy.
- Use a larger dataset.
- Deploy the model using **Flask/FastAPI**.
- Add a mobile-friendly UI.

## 🤝 Contributing
Feel free to submit issues, feature requests, or pull requests to improve this project.

## 📜 License
This project is open-source and available under the **MIT License**.

---

💡 *Built with passion for AI and agriculture!* 🌱


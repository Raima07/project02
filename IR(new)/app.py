from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from src.predict import predict_disease

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

MODEL_PATH = 'models/best_model.h5'
CLASS_INDICES_PATH = 'models/class_indices.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    try:
        predicted_label, confidence = predict_disease(MODEL_PATH, file_path, CLASS_INDICES_PATH)
        return jsonify({
            'prediction': predicted_label,
            'confidence': float(confidence)  # ✅ Convert to native Python float
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

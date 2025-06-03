# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
from werkzeug.utils import secure_filename

# Import prediction function from predict.py
from backend.predict import predict_image
# from predict import predict_image # for local test

app = Flask(__name__)
#CORS(app, origins=["http://localhost:5173", "https://ai-image-classifier-3skv.onrender.com"])
#CORS(app, resources={r"/predict": {"origins": "https://scstylescope.vercel.app/"}})
CORS(app, supports_credentials=True, resources={
    r"/predict": {
        "origins": [
            "http://localhost:5173",
            "https://scstylescope.vercel.app"
        ]
    }
})

# Define upload directory for incoming files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Base directory (backend/)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

logging.basicConfig(level=logging.INFO)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file provided.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'Filename is empty.'}), 400

    filename = secure_filename(file.filename)
    save_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(save_path)

    try:
        prediction = predict_image(save_path)
        app.logger.info(f"Predicted: {prediction}")
        return jsonify({'status': 'success', 'result': prediction})
    except Exception as e:
        app.logger.error(f"Prediction failed: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        if os.path.exists(save_path):
            os.remove(save_path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port, debug=False)
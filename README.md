# AI Image Classifier Project (Backend)

## ✅ Overview

This project is an AI-powered image classifier for identifying clothing styles using a fine-tuned ResNet18 model.
The backend is built with **Flask** and **PyTorch**.

---

## ✅ Features

- 🧠 **AI-Powered Predictions** – Upload an image and get instant predictions for clothing categories.
- 📊 **Confidence Visualization** – View a breakdown of model confidence via an intuitive chart.
- 🎨 **Modern Frontend** – Stylish UI with responsive design and smooth animations.
- 🗂️ **Drag & Drop Upload** – Easily upload images by dragging or selecting from your files.
- 🌍 **Accessible via Web** – No installation required, use it directly in your browser.

---

## ✅ Project Structure

ai-image-classifier/
├── backend/
│ ├── app.py # Flask API server
│ ├── predict.py # Image prediction logic (ResNet18)
│ ├── train.py # Model fine-tuning script
│ ├── dataloader.py # Data loader for training
│ └── model/
│ └── resnet18_finetuned.pt # Trained model weights
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── UploadArea.jsx # Upload UI with drag & drop
│ │ │ └── ResultBox.jsx # Result display with chart
│ │ ├── pages/
│ │ │ └── Home.jsx # Main page layout
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ └── index.css
│ ├── index.html
│ └── package.json
└── data/
  └── clothing-dataset-small-master/
  ├── train/
  ├── validation/
  └── test/

---

## ✅ Project Structure

- **Architecture**: ResNet18 (from PyTorch, pretrained on ImageNet)
- **Classes**: 10 (e.g., shirt, pants, skirt, etc.)
- **Fine-tuning**:
  - 5 epochs
  - Learning rate: 0.0001 (Adam optimizer)
  - Dataset: ~2000+ clothing images
- **Performance**:
  - ~99% confidence on test samples
  - 95+% accuracy

---

## ✅ How to Use

### 🌐 Web App

1️⃣ Upload an image (via drag & drop or file selector).  
2️⃣ Click **Predict** to get results.  
3️⃣ View the predicted label, confidence score, and chart breakdown.

### 🛠️ Backend API

- **Endpoint**: `POST /predict`
- **Request**: 
  - Form-Data (key: `file`, value: image file)
- **Response Example**:

```json
{
  "label": "shirt",
  "confidence": 0.9821,
  "topk": [
    {"label": "shirt", "confidence": 0.9821},
    {"label": "t-shirt", "confidence": 0.0103},
    {"label": "jacket", "confidence": 0.0076}
  ]
}
```
---

## ✅ Tech Stack

* 🌐 Backend: Python 3.11, Flask, PyTorch, TorchVision, PIL
* 🎨 Frontend: React.js, Tailwind CSS, framer-motion
* 📊 Visualization: Chart.js (via react-chartjs-2)
* 🌎 Deployment: Render (Recommended)

## 🎯 Project Goal
  Create an intuitive, stylish web app for fashion enthusiasts and developers to explore AI-powered clothing predictions.

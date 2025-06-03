# AI Image Classifier Project

Domain: https://scstylescope.vercel.app/

## ✅ Overview

This project is an AI-powered image classifier for identifying clothing styles using a fine-tuned ResNet18 model. The backend is built with **Flask** and **PyTorch**, and the frontend with **React**.

---

## ✅ Features

* 🧠 **AI-Powered Predictions** – Upload an image and get instant predictions for clothing categories.
* 📊 **Confidence Visualization** – View a breakdown of model confidence via an intuitive chart.
* 🎨 **Modern Frontend** – Stylish UI with responsive design and smooth animations.
* 🗂️ **Drag & Drop Upload** – Easily upload images by dragging or selecting from your files.
* 🌍 **Accessible via Web** – No installation required, use it directly in your browser.
* 🚀 **Full Deployment** – Frontend hosted on Vercel, backend deployed on Render via Docker.

---

## ✅ Project Structure

```
ai-image-classifier/
├── backend/
│   ├── app.py               # Flask API server
│   ├── predict.py           # Image prediction logic (ResNet18)
│   ├── train.py             # Model fine-tuning script
│   ├── dataloader.py        # Data loader for training
│   ├── model/
│   │   └── resnet18_finetuned.pt  # Trained model weights
│
├── frontend/
│   ├── package.json         # Frontend dependencies
│   ├── src/
│   │   ├── components/
│   │   │   ├── UploadArea.jsx     # Upload UI (drag & drop + button)
│   │   │   └── ResultBox.jsx      # Result display with chart
│   │   ├── pages/
│   │   │   └── Home.jsx           # Main page layout
│   │   ├── App.jsx               # Entry point
│   │   ├── index.css             # Global styles
│   │   └── main.jsx              # React app root
│   ├── public/
│       └── index.html            # HTML template
│
├── .gitignore
├── Dockerfile
├── render.yaml
├── .dockerignore
└── README.md
```

---

## ✅ Model Overview

* **Architecture**: ResNet18 (from PyTorch, pretrained on ImageNet)
* **Classes**: 10 (e.g., shirt, pants, skirt, etc.)
* **Fine-tuning**:

  * 5 epochs
  * Learning rate: 0.0001 (Adam optimizer)
  * Dataset: \~2000+ clothing images
* **Performance**:

  * \~99% confidence on test samples
  * 95+% accuracy

---

## ✅ How to Use

### 🌐 Web App

1. Upload an image (via drag & drop or file selector).
2. Click **Predict** to get results.
3. View the predicted label, confidence score, and chart breakdown.

### 🛠️ Backend API

* **Endpoint**: `POST /predict`
* **Request**:

  * Form-Data (key: `file`, value: image file)
* **Response Example**:

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
* 🚀 Deployment: Render (Docker) + Vercel

---

## ✅ Dataset

This project uses the **Clothing Dataset (Small)** by Alexey Grigorev.
Original dataset repository: [alexeygrigorev/clothing-dataset-small](https://github.com/alexeygrigorev/clothing-dataset-small).

* The dataset contains \~2000 images of clothing items across 10 categories (e.g., shirt, pants, skirt, etc.).
* Used for training, validation, and testing of the model.
* **License**: CC0 1.0 Universal (Public Domain Dedication).

---

## ✅ Development Notes

* Multiple ResNet variants and CNN baselines were tested. A fine-tuned ResNet18 yielded the best results.
* Frontend design was carefully structured with responsiveness and ease-of-use in mind.
* Docker was introduced to stabilize backend deployment across systems. It added complexity and large disk use, but ensured environment consistency.
* CORS and file path issues required significant debugging when moving from local development to deployment.

---

## 🎯 Project Goal

Build an intuitive and attractive web app that makes AI-based image classification easily accessible to anyone interested in fashion tech or ML demos.
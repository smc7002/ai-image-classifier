# predict.py

import torch
from torchvision import transforms, models
from PIL import Image
import torch.nn.functional as F
import torch.nn as nn
import os

# 1️⃣ Transform
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# 2️⃣ Load Fine-tuned ResNet18
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(pretrained=False)
num_classes = 10  # Number of classes (adjust if needed)
model.fc = nn.Linear(model.fc.in_features, num_classes)

# Absolute model path for Render (and local)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model', 'resnet18_finetuned.pt')

try:
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    model.to(device)
except Exception as e:
    print(f"⚠️ Model loading failed: {e}")

# 3️⃣ Predict Function
def predict_image(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        image_tensor = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(image_tensor)
            probabilities = F.softmax(outputs, dim=1)

            confidence, predicted = torch.max(probabilities, 1)
            topk_probs, topk_indices = torch.topk(probabilities, 3)  # Top-3

        idx_to_class = [
            'dress', 'hat', 'longsleeve', 'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt'
        ]

        topk_results = []
        for i in range(3):
            label = idx_to_class[topk_indices[0][i].item()]
            conf = round(topk_probs[0][i].item(), 4)
            topk_results.append({"label": label, "confidence": conf})

        return {
            "main_prediction": {
                "label": idx_to_class[predicted.item()],
                "confidence": round(confidence.item(), 4)
            },
            "topk": topk_results
        }

    except Exception as e:
        print(f"⚠️ Prediction failed: {e}")
        return {"error": str(e)}

import torch
import torch.nn as nn
import torch.optim as optim
from dataloader import train_loader, val_loader
import torchvision.models as models
import os

# 1️⃣ Load Pretrained ResNet18
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(pretrained=True)

# 2️⃣ Replace final layer for your classes
num_classes = len(train_loader.dataset.classes)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)

# 3️⃣ Loss & Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001)  # Fine-tuning이니까 작은 LR

# 4️⃣ Training Loop
epochs = 5
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

    acc = correct / total
    print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss:.4f}, Train Accuracy: {acc:.4f}")

# 5️⃣ Save model
os.makedirs("backend/model", exist_ok=True)
torch.save(model.state_dict(), "backend/model/resnet18_finetuned.pt")
print("✅ Saved fine-tuned model: backend/model/resnet18_finetuned.pt")

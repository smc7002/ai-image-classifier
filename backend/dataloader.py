# backend/app.py

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. Defining image transformation (augmentation + normalization)
transform = transforms.Compose([
    transforms.RandomResizedCrop(128, scale=(0.8, 1.0)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
])

# 2. Loading Dataset
train_dataset = datasets.ImageFolder('../data/clothing-dataset-small-master/train', transform=transform)
val_dataset = datasets.ImageFolder('../data/clothing-dataset-small-master/validation', transform=transform)

# 3. Creating DataLoader
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)

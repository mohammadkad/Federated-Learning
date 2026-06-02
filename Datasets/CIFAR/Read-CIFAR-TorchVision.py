# Mohammad Kadkhodaei Elyaderani
# 1405-03-12, 2026/06/02

'''
The CIFAR-10 dataset consists of 60,000 color images, each of size 32×32 pixels.
Training set: 50,000 images
Test set: 10,000 images
Channels: 3 (RGB)
Total file size on disk: ~163 MB (compressed)
'''

'''
The CIFAR-10 and CIFAR-100 datasets are labeled subsets of the 80 million tiny images dataset. CIFAR-10 and CIFAR-100 were created by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.
https://docs.pytorch.org/vision/0.8/datasets.html#cifar
https://www.cs.toronto.edu/~kriz/
https://www.cs.toronto.edu/~kriz/cifar.html
'''

from torchvision import datasets
import torchvision.transforms as transforms

# Define transform (convert to tensor and normalize)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # Normalize to [-1, 1]
])

# Download and load training set
train_dataset = datasets.CIFAR10(
    root='./data',          # storage directory
    train=True,             # training set (50,000 images)
    download=True,          # download if not present
    transform=transform     # apply transforms
)

# Download and load test set
test_dataset = datasets.CIFAR10(
    root='./data',
    train=False,            # test set (10,000 images)
    download=True,
    transform=transform
)

# Check sizes
print(f"Training set size: {len(train_dataset)}")  # 50000
print(f"Test set size: {len(test_dataset)}")       # 10000
print(f"Image shape: {train_dataset[0][0].shape}") # torch.Size([3, 32, 32])

# Class names
classes = train_dataset.classes
print(f"Classes: {classes}")
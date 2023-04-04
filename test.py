import cv2
import numpy as np
import torch
import einops

# Create a sample PyTorch tensor
tensor = torch.zeros(1, 256, 512, 3)

tensor = einops.rearrange(tensor, "1 w h ch -> h w ch")
print(tensor.shape)

# Convert the numpy array to an OpenCV image
image = cv2.cvtColor(tensor.detach().cpu().numpy(), cv2.COLOR_RGB2BGR)
print(image.shape)
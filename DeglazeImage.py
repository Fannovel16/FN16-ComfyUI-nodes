import numpy as np
import cv2
from cv2.ximgproc import guidedFilter
import torch

def img_np_to_tensor(img_np):
    return torch.from_numpy(img_np / 255.0)[None,]
def img_tensor_to_np(img_tensor):
    img_tensor = img_tensor.clone()
    img_tensor = img_tensor * 255.0
    return img_tensor.squeeze(0).numpy().astype(np.float32)
    #Thanks ChatGPT

#https://github.com/lllyasviel/AdverseCleaner/blob/main/clean.py
def deglaze_np_img(np_img):
    y = np_img.copy()
    for _ in range(64):
        y = cv2.bilateralFilter(y, 5, 8, 8)
    for _ in range(4):
        y = guidedFilter(np_img, y, 4, 16)
    return y

class DeglazeImage:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE", ) } }

    CATEGORY = "image"

    RETURN_TYPES = ("IMAGE", )
    FUNCTION = "deglaze_image"
    def deglaze_image(self, image):
        return (img_np_to_tensor(deglaze_np_img(img_tensor_to_np(image))),)

NODE_CLASS_MAPPINGS = {
    "DeglazeImage": DeglazeImage
}
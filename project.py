
from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import random

def calculate_psnr(img1, img2, max_value=255):
    """"Calculating peak signal-to-noise ratio (PSNR) between two images."""
    mse = np.mean((np.array(img1, dtype=np.float32) - np.array(img2, dtype=np.float32)) ** 2)
    print(mse)
    if mse == 0:
        return 100
    return 20 * np.log10(max_value / (np.sqrt(mse)))

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
imgFilt = np.zeros((img.shape[0],img.shape[1]), np.uint8)
noise =  np.zeros((img.shape[0],img.shape[1]), np.uint8)

for i in range(img.shape[0]):
  for j in range(img.shape[1]):
    newValue = img[i][j] + random.gauss(0, 64)

    if(newValue < 0):
      newValue = 0
    elif(newValue > 255):
      newValue = 255

    imgFilt[i][j] = newValue

print(calculate_psnr(img, imgFilt))

cv2_imshow(img)
cv2_imshow(imgFilt)


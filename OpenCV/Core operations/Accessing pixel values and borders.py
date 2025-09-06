import numpy as np
import cv2 as cv

img = cv.imread("Test Image.png")
assert img is not None, "Could not read the image."

# Accessing pixel values
px = img[100, 100]  # Access pixel at (100, 100)
print(f"Pixel value at (100, 100): {px}")

# Changing pixel value
img[100, 100] = [255, 255, 255]  # Set pixel to white
print(f"Changed pixel value at (100, 100) to: {img[100, 100]}")

# Image rows, columns, and channels
print(f"Image shape: {img.shape}")  # (height, width, channels)

print(img.size) # Total number of pixels

print(img.dtype)  # Data type of the image

# Accessing a specific area
testArea = img[1000:1300, 1000:1300]  # Access a sub-area of the image

img[2500:2800, 2500:2800] = testArea  # Copy the sub-area to another location  

img[:,:, 0] = 0  # Set all blue channel values to 0

border = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_CONSTANT, value=[0, 0, 255])  # Add a red border  

cv.namedWindow("Modified Image", cv.WINDOW_NORMAL)
cv.resizeWindow("Modified Image", 600, 400)

cv.imshow("Modified Image", border)  # Display the modified image
cv.waitKey(0)
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color

# Load the image using matplotlib
img = io.imread('C:/Users/Tippireddy/Videos/Personal Docs/py/Object data/apple.jpg')

# If the image has 4 channels (RGBA), remove the alpha channel
if img.shape[2] == 4:
    img = img[:, :, :3]

# Convert the image to HSV color space using skimage
hsv_img = color.rgb2hsv(img)

# Get the H, S, and V components
hue = hsv_img[:, :, 0].flatten()
saturation = hsv_img[:, :, 1].flatten()
value = hsv_img[:, :, 2].flatten()

# Create a scatter plot of Hue vs. Saturation (H vs. S)
plt.scatter(hue, saturation, c=value, cmap='hsv', s=1)
plt.xlabel('Hue')
plt.ylabel('Saturation')
plt.title('Scatter Plot of Apple Colors in HSV Space')
plt.show()

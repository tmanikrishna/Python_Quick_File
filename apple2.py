import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from skimage import io, color

# Load the image using matplotlib
img = io.imread('C:/Users/Tippireddy/Videos/Personal Docs/py/Object data/apple.jpg')

# If the image has 4 channels (RGBA), remove the alpha channel
if img.shape[2] == 4:
    img = img[:, :, :3]

# Convert the image to HSV color space using skimage
hsv_img = color.rgb2hsv(img)

# Define the color ranges for red, green, and yellow apples in HSV
# Red Apples
lower_red1 = np.array([0, 0.2, 0.2])
upper_red1 = np.array([0.05, 1, 1])
lower_red2 = np.array([0.95, 0.2, 0.2])
upper_red2 = np.array([1, 1, 1])

# Green Apples
lower_green = np.array([0.1, 0.2, 0.2])
upper_green = np.array([0.3, 1, 1])

# Yellow Apples
lower_yellow = np.array([0.1, 0.4, 0.4])
upper_yellow = np.array([0.2, 1, 1])

# Create masks for each color range
mask_red1 = np.all(hsv_img >= lower_red1, axis=-1) & np.all(hsv_img <= upper_red1, axis=-1)
mask_red2 = np.all(hsv_img >= lower_red2, axis=-1) & np.all(hsv_img <= upper_red2, axis=-1)
mask_red = mask_red1 | mask_red2

mask_green = np.all(hsv_img >= lower_green, axis=-1) & np.all(hsv_img <= upper_green, axis=-1)
mask_yellow = np.all(hsv_img >= lower_yellow, axis=-1) & np.all(hsv_img <= upper_yellow, axis=-1)

# Combine the masks for all apple colors
mask_combined = mask_red | mask_green | mask_yellow

# Find contours (connected components) in the combined mask
from skimage.measure import label, regionprops

labeled_img = label(mask_combined)
regions = regionprops(labeled_img)

# Plot the original image
fig, ax = plt.subplots()
ax.imshow(img)

# Draw bounding boxes and center points for each detected region
for region in regions:
    # Get the bounding box coordinates
    minr, minc, maxr, maxc = region.bbox
    center = region.centroid

    # Create a rectangle for the bounding box
    rect = patches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                             linewidth=2, edgecolor='green', facecolor='none')
    ax.add_patch(rect)

    # Create a red dot for the center point
    ax.plot(center[1], center[0], 'ro', markersize=5)

# Show the image with the bounding boxes and center points
plt.show()

import cv2 as cv
import matplotlib.pyplot as plt

# Load the image
img = cv.imread("C:/Users/Tippireddy/Desktop/1.png")

# Convert BGR to RGB for matplotlib
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Show image using matplotlib
plt.imshow(img_rgb)
plt.axis('off')  # Hide the axis
plt.show()

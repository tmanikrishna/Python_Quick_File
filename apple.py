import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'C:/Users/Tippireddy/Videos/Personal Docs/py/Object data/basket.png'  # Replace with the path to your image
img = cv.imread(image_path)

if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()

# Convert the image to HSV color space
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)




# Define the color range for detection (apple is typically red)
lower_red = np.array([0, 120, 70])  # Lower bound for red color in HSV space
upper_red = np.array([10, 255, 255])  # Upper bound for red color in HSV space

# Create a mask to detect red areas (apple in this case)
mask = cv.inRange(hsv_img, lower_red, upper_red)

# Find contours in the mask
contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Process the contours to find the apple's position
for contour in contours:
    area = cv.contourArea(contour)
    if area > 500:  # Ignore small contours to avoid noise (adjust as needed)
        # Get the bounding box for the contour
        x, y, w, h = cv.boundingRect(contour)

        # Calculate the center of the bounding box
        center_x = x + w // 2
        center_y = y + h // 2

        # Draw the bounding box and center point on the image
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green bounding box
        cv.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)  # Red center point

        # Print the coordinates of the apple's center
        print(f"Apple center coordinates: X = {center_x}, Y = {center_y}")

# Convert the image from BGR (OpenCV format) to RGB (matplotlib format)
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Show the image using matplotlib
plt.imshow(img_rgb)
plt.axis('off')  # Hide axis
plt.show()




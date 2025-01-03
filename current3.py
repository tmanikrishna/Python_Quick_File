import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'C:/Users/Tippireddy/Desktop/1.png'  # Change this to the path of your image
img = cv.imread(image_path)

if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()

# Convert the image to HSV color space
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Define the color range for detection (example: red color)
lower_color = np.array([0, 120, 70])   # Lower bound for red
upper_color = np.array([10, 255, 255])  # Upper bound for red

# Create a mask to detect the color
mask = cv.inRange(hsv_img, lower_color, upper_color)

# Find contours in the mask
contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Process the contours
for contour in contours:
    area = cv.contourArea(contour)
    if area > 500:  # Ignore small contours to avoid noise (adjust this threshold as needed)
        # Get the bounding box of the contour
        x, y, w, h = cv.boundingRect(contour)

        # Calculate the center of the bounding box
        center_x = x + w // 2
        center_y = y + h // 2

        # Draw the bounding box and center point on the image
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green bounding box
        cv.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)  # Red center point

        # Print the coordinates of the center
        print(f"Object center coordinates: X = {center_x}, Y = {center_y}")

# Show the original image with detected object
cv.imshow('Detected Object', img)

# Wait for a key press and close the window
cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv

# Open the default webcam (camera index 0)
cap = cv.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    # Capture a single frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame from webcam.")
    else:
        # Display the captured frame
        cv.imshow("Webcam Image", frame)
        cv.waitKey(0)  # Wait for a keypress to close the window

    # Release the webcam resource
    cap.release()
    cv.destroyAllWindows()

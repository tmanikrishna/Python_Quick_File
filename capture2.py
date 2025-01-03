import cv2 as cv

# Try opening the USB webcam; replace 0 with the correct index (1, 2, etc.)
cap = cv.VideoCapture(5)  # Assuming 1 is the index for your USB webcam

if not cap.isOpened():
    print("Error: Could not open the USB webcam.")
else:
    print("USB webcam successfully opened. Press 'Esc' to exit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from the USB webcam.")
            break

        cv.imshow("USB Webcam Feed", frame)

        # Press 'Esc' key to exit
        if cv.waitKey(1) & 0xFF == 27:
            print("Exiting webcam feed.")
            break

    cap.release()
    cv.destroyAllWindows()

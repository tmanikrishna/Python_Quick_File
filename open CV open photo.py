# Simple Programme to Opean a Picture

import cv2 as cv
img = cv.imread("C:/Users/Tippireddy/Desktop/1.png") 

#cv.imshow("Display window", img)
#k = cv.waitKey(0) # Wait for a keystroke in the window

if img is None:
    print("Error: Image not found or path is incorrect.")
else:
    cv.imshow("Display window", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture(0)
cap.release()
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

cv.namedWindow("Frame")

def nothing(x):
    pass

cv.createTrackbar("Colour", "Frame", 0, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Get the current position of the trackbar
    colour = cv.getTrackbarPos("Colour", "Frame")
    cv.rectangle(frame, (50, 50, 200, 200), (colour, 0, 0), 2)

    cv.imshow("Frame", frame)

    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

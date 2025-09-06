import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture(0)
cap.release()
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

circles = []

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        circles.append((x, y))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    for circle in circles:
        cv.circle(frame, circle, 50, (0, 255, 0), 2)

    cv.imshow("Frame", frame)
    cv.setMouseCallback("Frame", draw_circle, frame)

    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

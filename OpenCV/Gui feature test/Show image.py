import cv2 as cv
import sys
 
img = cv.imread(cv.samples.findFile("Test Image.png"))
 
if img is None:
    sys.exit("Could not read the image.")
 
cv.namedWindow("Display window", cv.WINDOW_NORMAL)
cv.resizeWindow("Display window", 600, 400)

cv.imshow("Display window", img)
key = cv.waitKey(0)
 
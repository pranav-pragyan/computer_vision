import cv2 as cv
import numpy as np


def cross():
    pass


# blank image
img = np.zeros((300, 520, 3), np.uint8)
cv.namedWindow("Color Picker")

# create a switch (ON/OFF)
msg = "0:OFF\n1:ON"
# (msg, window_name, range_start, range_end, function)
cv.createTrackbar(msg, "Color Picker", 0, 1, cross)

# creating trackbars for R,G,B for a colors
cv.createTrackbar("R", "Color Picker", 0, 255, cross)
cv.createTrackbar("G", "Color Picker", 0, 255, cross)
cv.createTrackbar("B", "Color Picker", 0, 255, cross)


while True:
    cv.imshow("Color Picker", img)
    if cv.waitKey(1) == ord("q"):
        break

    # get the position of the trackbar.
    s = cv.getTrackbarPos(msg, "Color Picker")
    r = cv.getTrackbarPos("R", "Color Picker")
    g = cv.getTrackbarPos("G", "Color Picker")
    b = cv.getTrackbarPos("B", "Color Picker")

    # if switch is off then make all pixels zero
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()

#!/usr/bin/env python
import cv

cv.NamedWindow("camera", 1)
capture = cv.CreateCameraCapture(0)

while True:
    # Creates the frame
    img = cv.QueryFrame(capture)

    # http://opencv.willowgarage.com/documentation/python/drawing_functions.html#rectangle
    cv.Rectangle(img, (200, 150), (300, 250), (0, 0, 255), 1, 0)

    # http://opencv.willowgarage.com/documentation/python/drawing_functions.html#circle
    cv.Circle(img, (100, 100), 40, (255, 0, 0), thickness=1, lineType=8, shift=0)

    # Shows the image
    cv.ShowImage("camera", img)

    # Waits for the esc key to exit
    k = cv.WaitKey(7) % 0x100
    if k == 27:  # esc
        break

#!/usr/bin/env python
import cv

cv.NamedWindow("camera", 1)
capture = cv.CreateCameraCapture(0)

# Detect the width
width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))

# Detect the height
height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))

# Creates the result image
result = cv.CreateImage((width, height), cv.IPL_DEPTH_8U, 3)

while True:
    # Creates the frame
    img = cv.QueryFrame(capture)

    # http://opencv.willowgarage.com/documentation/python/drawing_functions.html#rectangle
    cv.Rectangle(img, (200, 150), (300, 250), (0, 0, 255), 1, 0)

    # http://opencv.willowgarage.com/documentation/python/drawing_functions.html#circle
    cv.Circle(img, (100, 100), 40, (255, 0, 0), thickness=1, lineType=8, shift=0)

    # Effets:
    # http://opencv.willowgarage.com/documentation/python/imgproc_image_filtering.html#smooth
    cv.Smooth(img, result, cv.CV_GAUSSIAN, 9, 9)

    # Shows the image
    cv.ShowImage("camera", result)

    # Waits for the esc key to exit
    k = cv.WaitKey(7) % 0x100
    if k == 27:  # esc
        break

#!/usr/bin/env python
import cv

cv.NamedWindow("camera", 1)
capture = cv.CreateCameraCapture(0)

while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)

    k = cv.WaitKey(7) % 0x100
    if k == 27:  # esc
        break

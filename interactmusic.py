#!/usr/bin/env python
import cv
import pygame

cv.NamedWindow("camera", 1)
capture = cv.CreateCameraCapture(0)

# Detect the width
# width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))

# Detect the height
# height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))

# Creates the result image
# result = cv.CreateImage((width, height), cv.IPL_DEPTH_8U, 3)

# frame = cv.QueryFrame(capture)
# temp = cv.CloneImage(frame)
# cv.Smooth(temp, temp, cv.CV_BLUR, 5, 5)

haarcascade = cv.Load("/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml")

pygame.init()
music = pygame.mixer.Sound('guitarra.ogg')


while True:
    # Creates the frame
    img = cv.QueryFrame(capture)

    # http://opencv.willowgarage.com/documentation/python/core_operations_on_arrays.html?highlight=absdiff#absdiff
    # cv.AbsDiff(img, temp, img)

    # http://opencv.willowgarage.com/documentation/python/drawing_functions.html#rectangle
    # cv.Rectangle(img, (200, 150), (300, 250), (0, 0, 255), 1, 0)

    # http://opencv.willowgarage.com/documentation/python/drawing_functions.html#circle
    # cv.Circle(img, (100, 100), 40, (255, 0, 0), thickness=1, lineType=8, shift=0)

    # Effets:

    # http://opencv.willowgarage.com/documentation/python/imgproc_image_filtering.html#smooth
    # cv.Smooth(img, result, cv.CV_GAUSSIAN, 9, 9)

    # http://opencv.willowgarage.com/documentation/python/imgproc_image_filtering.html#dilate
    # cv.Dilate(img, result, None, 5)

    # http://opencv.willowgarage.com/documentation/python/imgproc_image_filtering.html#erode
    # cv.Erode(img, result, None, 1)

    # http://opencv.willowgarage.com/documentation/python/objdetect_cascade_classification.html?highlight=haarcascades
    detected = cv.HaarDetectObjects(img, haarcascade, cv.CreateMemStorage(), 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (0, 0))
    if detected:
        music.play()

        for (x, y, w, h), n in detected:
            cv.Rectangle(img, (x, y), (x+w, y+h), 255)

    # Shows the image
    cv.ShowImage("camera", img)
    # cv.ShowImage("temp", temp)
    # cv.ShowImage("diff", img)

    # Waits for the esc key to exit
    k = cv.WaitKey(7) % 0x100
    if k == 27:  # esc
        break

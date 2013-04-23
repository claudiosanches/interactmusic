#!/usr/bin/env python
import cv
import pygame

cv.NamedWindow("camera", 1)
capture = cv.CreateCameraCapture(0)

haarcascade = cv.Load("/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml")

pygame.init()
music = pygame.mixer.Sound('guitarra.ogg')

while True:
    # Creates the frame
    img = cv.QueryFrame(capture)

    # http://opencv.willowgarage.com/documentation/python/objdetect_cascade_classification.html?highlight=haarcascades
    detected = cv.HaarDetectObjects(img, haarcascade, cv.CreateMemStorage(), 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (0, 0))
    if detected:
        music.play()

        for (x, y, w, h), n in detected:
            cv.Rectangle(img, (x, y), (x+w, y+h), 255)

    # Shows the image
    cv.ShowImage("camera", img)

    # Waits for the esc key to exit
    k = cv.WaitKey(7) % 0x100
    if k == 27:  # esc
        break

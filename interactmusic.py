#!/usr/bin/env python
import cv
import pygame


class InteractMusic:
    def __init__(self):
        self.name = "InteractMusic"
        pygame.mixer.init()
        self.capture = cv.CaptureFromCAM(0)
        cv.NamedWindow(self.name, 1)
        self.hc = cv.Load("haarcascades/haarcascade_frontalface_default.xml")

        # audio tracks
        self.audio1 = pygame.mixer.Sound('guitarra.ogg')
        self.audio2 = pygame.mixer.Sound('bateria.ogg')

    def is_intersect(self, ax, ay, aw, ah, bx, by, bw, bh):
        return ax < bw and aw > bx and ay < bh and ah > by

    def run(self):
        while True:
            webcam = cv.QueryFrame(self.capture)
            face = cv.HaarDetectObjects(webcam, self.hc, cv.CreateMemStorage(), 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (0, 0))

            for ((x, y, w, h), k) in face:
                # First rectangle
                rec1x = 200
                rec1y = 150
                rec1w = rec1x + 100
                rec1h = rec1y + 100
                cv.Rectangle(webcam, (rec1x, rec1y), (rec1w, rec1h), (0, 0, 255), 1, 0)

                # Second rectangle
                rec2x = 100
                rec2y = 250
                rec2w = rec2x + 100
                rec2h = rec2y + 100
                cv.Rectangle(webcam, (rec2x, rec2y), (rec2w, rec2h), (0, 0, 255), 1, 0)

                # Trace faces
                camX = int(x)
                camY = int(y)
                camW = camX + w
                camH = camY + h
                cv.Rectangle(webcam, (camX, camY), (camW, camH), (255, 0, 0), 1, 0)
                cv.ShowImage(self.name, webcam)

                # Test the first rectangle and play the audio
                if (self.is_intersect(rec1x, rec1y, rec1w, rec1h, camX, camY, camW, camH)):
                    # Checks if the channel is busy
                    if not self.audio1.get_busy():
                        self.audio1.play()

                if (self.is_intersect(rec2x, rec2y, rec2w, rec2h, camX, camY, camW, camH)):
                    # Checks if the channel is busy
                    if not self.audio1.get_busy():
                        self.audio1.play()

            # Waits for the esc key to exit
            c = cv.WaitKey(7) % 0x100
            if c == 27 or c == 10:
                break

if __name__ == "__main__":
    run = InteractMusic()
    run.run()

#!/usr/bin/env python
import cv
import pygame


class InteractMusic:
    def __init__(self):
        self.name = "InteractMusic"
        pygame.mixer.init(frequency=44100, size=-16, channels=4)
        self.capture = cv.CaptureFromCAM(0)
        cv.NamedWindow(self.name, 1)
        self.hc = cv.Load("haarcascades/haarcascade_frontalface_default.xml")

        # audio tracks
        self.audio1 = pygame.mixer.Sound('media/eletric5.ogg')
        self.audio2 = pygame.mixer.Sound('media/eletric7.ogg')
        self.audio3 = pygame.mixer.Sound('media/eletric4.ogg')  # base

        # audio channels
        self.channel1 = pygame.mixer.Channel(1)
        self.channel2 = pygame.mixer.Channel(2)
        self.channel3 = pygame.mixer.Channel(3)

    def is_intersect(self, ax, ay, aw, ah, bx, by, bw, bh):
        return ax < bw and aw > bx and ay < bh and ah > by

    def run(self):
        while True:
            webcam = cv.QueryFrame(self.capture)
            face = cv.HaarDetectObjects(webcam, self.hc, cv.CreateMemStorage(), 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (0, 0))
            if not self.channel3.get_busy():
                self.channel3.play(self.audio3)

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
                    if not self.channel1.get_busy():
                        self.channel1.play(self.audio1)

                if (self.is_intersect(rec2x, rec2y, rec2w, rec2h, camX, camY, camW, camH)):
                    # Checks if the channel is busy
                    if not self.channel2.get_busy():
                        self.channel2.play(self.audio2)

            # Waits for the esc key to exit
            c = cv.WaitKey(7) % 0x100
            if c == 27 or c == 10:
                break

if __name__ == "__main__":
    run = InteractMusic()
    run.run()

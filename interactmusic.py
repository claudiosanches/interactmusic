#!/usr/bin/env python
import cv
import pygame


class InteractMusic:
    def __init__(self):
        self.name = "InteractMusic"
        pygame.mixer.init(frequency=44100, size=-16, channels=8)
        self.capture = cv.CaptureFromCAM(0)
        cv.NamedWindow(self.name, 1)
        self.hc = cv.Load("haarcascades/haarcascade_frontalface_default.xml")

        # audio tracks
        self.audio0 = pygame.mixer.Sound('media/base.ogg')
        self.audio1 = pygame.mixer.Sound('media/song01.ogg')
        self.audio2 = pygame.mixer.Sound('media/song02.ogg')
        self.audio3 = pygame.mixer.Sound('media/song03.ogg')
        self.audio4 = pygame.mixer.Sound('media/song04.ogg')
        self.audio5 = pygame.mixer.Sound('media/song05.ogg')
        self.audio6 = pygame.mixer.Sound('media/song06.ogg')

        # audio channels
        self.channel0 = pygame.mixer.Channel(1)
        self.channel1 = pygame.mixer.Channel(2)
        self.channel2 = pygame.mixer.Channel(3)
        self.channel3 = pygame.mixer.Channel(4)
        self.channel4 = pygame.mixer.Channel(5)
        self.channel5 = pygame.mixer.Channel(6)
        self.channel6 = pygame.mixer.Channel(7)

    def is_intersect(self, ax, ay, aw, ah, bx, by, bw, bh):
        return ax < bw and aw > bx and ay < bh and ah > by

    def run(self):
        while True:
            webcam = cv.QueryFrame(self.capture)
            face = cv.HaarDetectObjects(webcam, self.hc, cv.CreateMemStorage(), 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (0, 0))
            if not self.channel0.get_busy():
                self.channel0.play(self.audio0)

            for ((x, y, w, h), k) in face:
                # First rectangle
                rec1x = 200
                rec1y = 150
                rec1w = rec1x + 50
                rec1h = rec1y + 50
                cv.Rectangle(webcam, (rec1x, rec1y), (rec1w, rec1h), (0, 0, 255), 1, 0)

                # Second rectangle
                rec2x = 400
                rec2y = 50
                rec2w = rec2x + 50
                rec2h = rec2y + 50
                cv.Rectangle(webcam, (rec2x, rec2y), (rec2w, rec2h), (0, 0, 255), 1, 0)

                # Third rectangle
                rec3x = 100
                rec3y = 100
                rec3w = rec3x + 50
                rec3h = rec3y + 50
                cv.Rectangle(webcam, (rec3x, rec3y), (rec3w, rec3h), (0, 0, 255), 1, 0)

                # Fourth rectangle
                rec4x = 400
                rec4y = 400
                rec4w = rec4x + 50
                rec4h = rec4y + 50
                cv.Rectangle(webcam, (rec4x, rec4y), (rec4w, rec4h), (0, 0, 255), 1, 0)

                # Fifth rectangle
                rec5x = 500
                rec5y = 150
                rec5w = rec5x + 50
                rec5h = rec5y + 50
                cv.Rectangle(webcam, (rec5x, rec5y), (rec5w, rec5h), (0, 0, 255), 1, 0)

                # Sixth rectangle
                rec6x = 50
                rec6y = 400
                rec6w = rec6x + 50
                rec6h = rec6y + 50
                cv.Rectangle(webcam, (rec6x, rec6y), (rec6w, rec6h), (0, 0, 255), 1, 0)

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

                if (self.is_intersect(rec3x, rec3y, rec3w, rec3h, camX, camY, camW, camH)):
                    # Checks if the channel is busy
                    if not self.channel3.get_busy():
                        self.channel3.play(self.audio3)

                if (self.is_intersect(rec4x, rec4y, rec4w, rec4h, camX, camY, camW, camH)):
                    # Checks if the channel is busy
                    if not self.channel4.get_busy():
                        self.channel4.play(self.audio4)

                if (self.is_intersect(rec5x, rec5y, rec5w, rec5h, camX, camY, camW, camH)):
                    # Checks if the channel is busy
                    if not self.channel5.get_busy():
                        self.channel5.play(self.audio5)

                if (self.is_intersect(rec6x, rec6y, rec6w, rec6h, camX, camY, camW, camH)):
                    # Checks if the channel is busy
                    if not self.channel6.get_busy():
                        self.channel6.play(self.audio6)

            # Waits for the esc key to exit
            c = cv.WaitKey(7) % 0x100
            if c == 27 or c == 10:
                break

if __name__ == "__main__":
    run = InteractMusic()
    run.run()

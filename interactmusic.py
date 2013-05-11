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

    def run(self):
        while True:
            webcam = cv.QueryFrame(self.capture)
            face = cv.HaarDetectObjects(webcam, self.hc, cv.CreateMemStorage(), 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (0, 0))

            for ((x, y, w, h), k) in face:
                # Trace faces
                cv.Rectangle(webcam, (int(x), int(y)), (int(x) + int(w), int(y) + int(h)), (255, 0, 0), 1, 0)
                cv.ShowImage(self.name, webcam)

                # Test the first rectangle and play the audio
                if x > 100:
                    # Checks if the channel is busy
                    if not self.audio1.get_busy():
                        self.audio1.play()

                if x < 450:
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

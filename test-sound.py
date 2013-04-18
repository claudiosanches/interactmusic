#!/usr/bin/env python
# http://www.pygame.org/docs/ref/mixer.html
import pygame

pygame.init()
music = pygame.mixer.Sound('guitarra.ogg')
clock = pygame.time.Clock()
music.play()

while True:
    clock.tick(5)

pygame.quit()

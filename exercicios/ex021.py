import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021b.mp3')
pygame.mixer.music.play()
pygame.event.wait()

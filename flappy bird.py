import pygame

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("flappy bird")

pygame.quit()
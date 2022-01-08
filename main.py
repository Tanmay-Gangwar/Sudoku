import pygame
import create
import front_screen
import board
import games
from data import *
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == '__main__':
    run = 1
    while run != 0:
        if run == 1: run = front_screen.main(screen)
        if run == 2: run = create.main(screen)
        if run == 3: run = games.main(screen)

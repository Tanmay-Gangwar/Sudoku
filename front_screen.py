import pygame
from data import *
pygame.init()

def display_screen(screen, x, y, click) -> None:
    screen.fill((255, 255, 255))
    screen.blit(title_image.image, (0, 0))
    if index_11.x <= x <= index_11.x + index_11.width and index_11.y <= y <= index_11.y + index_11.height: 
        screen.blit(index_12.image, (index_12.x, index_12.y))
        if click: return 2
    else: screen.blit(index_11.image, (index_11.x, index_11.y))
    if index_21.x <= x <= index_21.x + index_21.width and index_21.y <= y <= index_21.y + index_21.height: 
        screen.blit(index_22.image, (index_22.x, index_22.y))
        if click: return 3
    else: screen.blit(index_21.image, (index_21.x, index_21.y))
    pygame.display.update()

def main(screen):
    x = 0
    y = 0
    click = False
    while True:
        to_return = display_screen(screen, x ,y, click)
        if to_return: return to_return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
import pygame
from board_manager import Board_manager
from Image import Image
from board import Board
pygame.init()

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600
BOX_WIDTH = SCREEN_WIDTH // 9

title_image = Image('Title.jpg')
board_manager = Board_manager('boards.obj')
board_manager.load()

large_font = pygame.font.Font('freesansbold.ttf', 20)
small_font = pygame.font.Font('freesansbold.ttf', 14)

back_image_1 = Image('back_1.jpg')
back_image_1.y = SCREEN_HEIGHT - back_image_1.height
back_image_2 = Image('back_2.jpg')
back_image_2.y = back_image_1.y

tick_image_1 = Image('tick_2.jpg')
tick_image_1.x = SCREEN_WIDTH - tick_image_1.width
tick_image_1.y = SCREEN_HEIGHT - tick_image_1.height
tick_image_2 = Image('tick_1.jpg')
tick_image_2.x = tick_image_1.x
tick_image_2.y = tick_image_1.y

index_11 = Image('Index_11.png')
index_11.y = (50 * SCREEN_HEIGHT) // 100
index_12 = Image('Index_12.png')
index_12.y = index_11.y
index_21 = Image('Index_21.png')
index_21.y = (60 * SCREEN_HEIGHT) // 100
index_22 = Image('Index_22.png')
index_22.y = index_21.y

for img in [index_11, index_12, index_21, index_22]:
    img.x = SCREEN_WIDTH // 2 - img.width // 2
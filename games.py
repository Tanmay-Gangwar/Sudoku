import pygame
import time
from data import *
import game
pygame.init()

NUM_COLS = 4
GAP = SCREEN_WIDTH // (NUM_COLS * 7)
SPACE_LEFT = SCREEN_WIDTH - (NUM_COLS + 1) * GAP
WIDTH = SPACE_LEFT // NUM_COLS
HIGHLIGHT_ROW = 0
HIGHLIGHT_COL = 0

def draw_board(screen, board, cnt):
    ROW = cnt // NUM_COLS
    COL = cnt % NUM_COLS
    x = GAP + COL * (WIDTH + GAP)
    y = GAP + ROW * (WIDTH + GAP)
    BOX_WIDTH = WIDTH // 9
    for i in range(0, WIDTH, BOX_WIDTH):
        pygame.draw.line(screen, (0, 0, 0), (x + i, y), (x + i, y + 9 * BOX_WIDTH))
        pygame.draw.line(screen, (0, 0, 0), (x, y + i), (x + 9 * BOX_WIDTH, y + i))
    for i in range(0, WIDTH, 3 * BOX_WIDTH):
        pygame.draw.line(screen, (0, 0, 0), (x + i, y), (x + i, y + 9 * BOX_WIDTH), 2)
        pygame.draw.line(screen, (0, 0, 0), (x, y + i), (x + 9 * BOX_WIDTH, y + i), 2)
    
    for i in range(9):
        for j in range(9):
            if board.board[i][j][0] != 0:
                text = str(board.board[i][j][0])
                text = little_font.render(text, True, (0, 0, 0))
                screen.blit(text, (x + j * BOX_WIDTH + BOX_WIDTH // 2 - text.get_width() // 2, y + i * BOX_WIDTH + BOX_WIDTH // 2 - text.get_height() // 2))


def display_screen(screen, boards, click, x, y):
    global HIGHLIGHT_COL, HIGHLIGHT_ROW
    # print(len(boards))
    selected = False
    screen.fill((255, 255, 255))
    if HIGHLIGHT_ROW * NUM_COLS + HIGHLIGHT_COL < len(boards):
        pygame.draw.rect(screen, (255, 255, 0), (GAP // 2 + HIGHLIGHT_COL * (WIDTH + GAP), GAP // 2 + HIGHLIGHT_ROW * (WIDTH + GAP), WIDTH + GAP, WIDTH + GAP))
    for i in range(len(boards)):
        draw_board(screen, boards[i], i)
    if back_image_1.x <= x <= back_image_1.x + back_image_1.width and back_image_1.y <= y <= back_image_1.y + back_image_1.height:
        screen.blit(back_image_2.image, (back_image_2.x, back_image_2.y))
        if click:
            return 1
    else: screen.blit(back_image_1.image, (back_image_1.x, back_image_1.y))
    if tick_image_1.x <= x <= tick_image_1.x + tick_image_1.width and tick_image_1.y <= y <= tick_image_1.y + tick_image_1.height:
        screen.blit(tick_image_2.image, (tick_image_2.x, tick_image_2.y))
        if click and HIGHLIGHT_ROW * NUM_COLS + HIGHLIGHT_COL < len(boards):
            return game.main(screen, boards[HIGHLIGHT_ROW * NUM_COLS + HIGHLIGHT_COL])
    else: screen.blit(tick_image_1.image, (tick_image_1.x, tick_image_1.y))
    if thrash_image_1.x <= x <= thrash_image_1.x + thrash_image_1.width and thrash_image_1.y <= y <= thrash_image_1.y + thrash_image_1.height:
        screen.blit(thrash_image_2.image, (thrash_image_2.x, thrash_image_2.y))
        if click: 
            to_pop = HIGHLIGHT_ROW * NUM_COLS + HIGHLIGHT_COL
            if to_pop < len(boards) : boards.pop(to_pop)
            board_manager.save()
            time.sleep(0.1)
            click = False

    else: screen.blit(thrash_image_1.image, (thrash_image_1.x, thrash_image_1.y))
    if click:
        ROW = y // (SCREEN_WIDTH // NUM_COLS)
        COL = x // (SCREEN_WIDTH // NUM_COLS)
        if NUM_COLS * ROW + COL < len(boards):
            HIGHLIGHT_ROW = ROW
            HIGHLIGHT_COL = COL
    pygame.display.update()


def main(screen):
    click = False
    pos_x, pos_y = 0, 0
    while True:
        to_return = display_screen(screen, board_manager.boards, click, pos_x, pos_y)
        if to_return: return to_return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
            if event.type == pygame.MOUSEMOTION:
                pos_x, pos_y = event.pos;
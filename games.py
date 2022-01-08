import pygame
from data import *
pygame.init()

NUM_COLS = 4
GAP = SCREEN_WIDTH // (NUM_COLS * 7)
SPACE_LEFT = SCREEN_WIDTH - (NUM_COLS + 1) * GAP
WIDTH = SPACE_LEFT // NUM_COLS

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
    
    # for i in range(9):
    #     for j in range(9):
    #         if board.board[i][j][0] != 0:
    #             text = str(board.board[i][j][0])
    #             text = large_font.render(text, True, (0, 0, 0))
    #             screen.blit(text, (j * BOX_WIDTH + BOX_WIDTH // 2 - text.get_width() // 2, i * BOX_WIDTH + BOX_WIDTH // 2 - text.get_height() // 2))


def display_screen(screen, boards):
    screen.fill((255, 255, 255))
    # print(len(boards))
    for i in range(len(boards)):
        draw_board(screen, boards[i], i)
    pygame.display.update()


def main(screen):
    while True:
        display_screen(screen, board_manager.boards)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
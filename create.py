import pygame
import time
import pickle
from data import *

def draw_rect(screen, row, col, color):
    col_factor = 2 if col == 0 or col == 3 or col == 6 else 1
    row_factor = 2 if row == 0 or row == 3 or row == 6 else 1
    pygame.draw.rect(screen, color, (col * BOX_WIDTH + col_factor, row * BOX_WIDTH + row_factor, BOX_WIDTH - col_factor, BOX_WIDTH - row_factor))

def display_screen(screen, board, row, col, x, y, click):
    screen.fill((255, 255, 255))
    draw_rect(screen, row, col, (255, 255, 0))
    for i in range(9):
        for j in range(9):
            if board.board[i][j][0] != 0:
                if not board.is_valid(board.board[i][j][0], i, j):
                    draw_rect(screen, i, j, (255, 0, 0))
    for i in range(0, SCREEN_WIDTH + 1, BOX_WIDTH):
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, SCREEN_WIDTH))
        pygame.draw.line(screen, (0, 0, 0), (0, i), (SCREEN_WIDTH, i))
    for i in range(0, SCREEN_WIDTH + 1, 3 * BOX_WIDTH):
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, SCREEN_WIDTH), 2)
        pygame.draw.line(screen, (0, 0, 0), (0, i), (SCREEN_WIDTH, i), 2)
    
    for i in range(9):
        for j in range(9):
            if board.board[i][j][0] != 0:
                text = str(board.board[i][j][0])
                text = large_font.render(text, True, (0, 0, 0))
                screen.blit(text, (j * BOX_WIDTH + BOX_WIDTH // 2 - text.get_width() // 2, i * BOX_WIDTH + BOX_WIDTH // 2 - text.get_height() // 2))
    if back_image_1.x <= x <= back_image_1.x + back_image_1.width and back_image_1.y <= y <= back_image_1.y + back_image_1.height:
        screen.blit(back_image_2.image, (back_image_2.x, back_image_2.y))
        if click:
            return 1
    else: screen.blit(back_image_1.image, (back_image_1.x, back_image_1.y))
    if tick_image_1.x <= x <= tick_image_1.x + tick_image_1.width and tick_image_1.y <= y <= tick_image_1.y + tick_image_1.height:
        screen.blit(tick_image_2.image, (tick_image_2.x, tick_image_2.y))
        if click:
            invalids = []
            for i in range(9):
                for j in range(9):
                    if board.board[i][j][0] != 0 and not board.is_valid(board.board[i][j][0], i, j):
                        invalids.append((i, j))
            if len(invalids) == 0:
                board_manager.boards.append(board)
                board_manager.save()
                return 1
            else:
                for r, c in invalids:
                    draw_rect(screen, r, c, (255, 255, 255))
                pygame.display.update()
                time.sleep(0.5)
                for r, c in invalids:
                    draw_rect(screen, r, c, (255, 0, 0))
    else: screen.blit(tick_image_1.image, (tick_image_1.x, tick_image_1.y))

    pygame.display.update()

def main(screen):
    row = 0
    col = 0
    x = 0
    y = 0
    click = False
    board = Board()
    while True:
        to_return = display_screen(screen, board, row, col, x, y, click)
        if to_return: return to_return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                row = min(y // BOX_WIDTH, 8)
                col = x // BOX_WIDTH
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP0 or event.key == pygame.K_0: board.board[row][col][0] = 0
                if event.key == pygame.K_KP1 or event.key == pygame.K_1: board.board[row][col][0] = 1
                if event.key == pygame.K_KP2 or event.key == pygame.K_2: board.board[row][col][0] = 2
                if event.key == pygame.K_KP3 or event.key == pygame.K_3: board.board[row][col][0] = 3
                if event.key == pygame.K_KP4 or event.key == pygame.K_4: board.board[row][col][0] = 4
                if event.key == pygame.K_KP5 or event.key == pygame.K_5: board.board[row][col][0] = 5
                if event.key == pygame.K_KP6 or event.key == pygame.K_6: board.board[row][col][0] = 6
                if event.key == pygame.K_KP7 or event.key == pygame.K_7: board.board[row][col][0] = 7
                if event.key == pygame.K_KP8 or event.key == pygame.K_8: board.board[row][col][0] = 8
                if event.key == pygame.K_KP9 or event.key == pygame.K_9: board.board[row][col][0] = 9
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE: board.board[row][col][0] = 0
                if event.key == pygame.K_UP: row = max(row - 1, 0)
                if event.key == pygame.K_DOWN: row = min(row + 1, 8)
                if event.key == pygame.K_LEFT: col = max(col - 1, 0)
                if event.key == pygame.K_RIGHT: col = min(col + 1, 8)
            
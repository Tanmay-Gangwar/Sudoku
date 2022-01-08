import create

class Board:
    def __init__(self, original_board = None):
        self.original_board = [[0 for _ in range(9)] for _ in range(9)] if original_board is None else original_board
        self.board = [[[self.original_board[i][j], [0 for _ in range(9)]] for j in range(9)] for i in range(9)]
    
    def is_valid(self, num: int, row: int, col: int) -> bool:
        for i in range(9):
            if self.board[row][i][0] == num and i != col: return False
            if self.board[i][col][0] == num and i != row: return False
        
        for i in range(3):
            for j in range(3):
                if self.board[3 * (row // 3) + i][3 * (col // 3) + j][0] == num and 3 * (row // 3) + i != row and 3 * (col // 3) + j != col: 
                    return False
        return True
    
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j][0] == 0:
                    return (i, j)
        return None
    
    def solve(self, screen, show):
        if show: create.display_screen(screen, self, 0, 0, 0, 0, False)
        # pygame.display.update()
        empty_pos = self.find_empty()
        if empty_pos is None: return True
        row, col = empty_pos
        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row][col][0] = num
                if self.solve(screen, show): return True
                self.board[row][col][0] = 0
        return False

    def print_board(self) -> None:
        for row in self.board:
            for num in row:
                print(num[0], end = " ")
            print("")
        print("")        

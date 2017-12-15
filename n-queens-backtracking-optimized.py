import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time() * 1000
        func(*args, **kwargs)
        end = time.time() * 1000
        print "Time taken by {} is {} ms".format(func.__name__, str(end - start))
    return wrapper


class BacktrackingNQueensOptimizedSafetyCheck:
    def __init__(self, N):
        self.diagonals = {}
        self.anti_diagonals = {}
        self.rows = {}
        self.columns = {}
        self.N = N
        self.board = [[0 for x in range(N)] for y in range(N)]
        self.number_of_solutions = 0

    def is_cell_safe(self, r, c):
        if r in self.rows:
            return False
        if c in self.columns:
            return False
        if r - c in self.diagonals:
            return False
        if r + c  in self.anti_diagonals:
            return False

        return True

    def place_a_queen(self, r, c):
        self.rows[r] = True
        self.columns[c] = True
        self.diagonals[r - c] = True
        self.anti_diagonals[r + c] = True
        self.board[r][c] = 1

    def undo_placing_a_queen(self, r, c):
        del self.rows[r]
        del self.columns[c]
        del self.diagonals[r - c]
        del self.anti_diagonals[r + c]
        self.board[r][c] = 0

    @timer
    def run(self):
        self.solve(0)

    def solve(self, column):
        if column == self.N:
            self.number_of_solutions += 1
            return
        for i in range(self.N):
            if self.is_cell_safe(i, column):
                self.place_a_queen(i, column)
                self.solve(column + 1)
                self.undo_placing_a_queen(i, column)

    def get_number_of_solutions(self):
        return self.number_of_solutions

if __name__ == "__main__":
    for i in range(8, 16):
        solver = BacktrackingNQueensOptimizedSafetyCheck(i)
        solver.run()
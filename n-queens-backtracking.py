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


class BacktrackNQueens:
    def __init__(self, N):
        self.N = N
        self.board = [[0 for x in range(N)] for y in range(N)]
        self.number_of_solutions = 0

    def is_cell_safe(self, row, col):
        # Check this row on left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.N, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    @timer
    def run(self):
        self.solve(0)

    def solve(self, column):
        if column == self.N:
            self.number_of_solutions += 1
            return
        for i in range(self.N):
            if self.is_cell_safe(i, column):
                self.board[i][column] = 1
                self.solve(column + 1)
                self.board[i][column] = 0

    def get_number_of_solutions(self):
        return self.number_of_solutions

if __name__ == "__main__":
    for i in range(8,16):
        solver = BacktrackNQueens(i)
        solver.run()
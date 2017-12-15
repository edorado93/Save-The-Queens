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


class NQueensBitMagic:
    def __init__(self, N, print_solutions=False):
        self.N = N
        self.board = [[0 for x in range(N)] for y in range(N)]
        self.number_of_solutions = 0
        self.all_ones = (1 << N) - 1
        self.solution_board = []
        self.print_solutions = print_solutions

    @timer
    def run(self):
        self.solve(0, 0, 0, 0)

    def solve(self, column, left_diagonal, right_diagonal, queens_placed):
        if queens_placed == self.N:
            self.number_of_solutions += 1
            if self.print_solutions:
                print [(i, j) for i,j in enumerate(self.solution_board)]
            return

        valid_spots = self.all_ones & ~(column | left_diagonal | right_diagonal)
        while valid_spots != 0:
            current_spot = -valid_spots & valid_spots
            self.solution_board.append((current_spot & -current_spot).bit_length() - 1)
            valid_spots ^= current_spot
            self.solve((column | current_spot), (left_diagonal | current_spot) >> 1,
                            (right_diagonal | current_spot) << 1, queens_placed + 1)
            self.solution_board.pop()

    def get_number_of_solutions(self):
        return self.number_of_solutions

if __name__ == "__main__":
    for i in range(8, 16):
        solver = NQueensBitMagic(i)
        solver.run()
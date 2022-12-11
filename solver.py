#!/bin/python3

##  Created by Kowalskyyyy
##  https://github.com/kowalskyyy999

import math
import numpy as np
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, action='store', help='Sudoku board')

args = parser.parse_args()

class SudokuSolver:
    def __init__(self, file):
        self.files = self.__read_file(file)

    @staticmethod
    def __read_file(file):
        with open(file, 'r') as f:
            files = f.readlines()
        return files

    def _get_board(self):
        board = []
        for line in self.files:
            tmp = [int(x) for x in line.split('[')[-1].split(']')[0].split(',')]
            board.append(tmp)
        return np.array(board)

    def __solve(self):
        shape_board = len(self.files)
        dim_grid = int(math.sqrt(shape_board))

        board = self._get_board()
        for i in range(0, shape_board):
            tmps = []
            for j in range(0, shape_board):
                tmp = [x for x in range(1, shape_board+1)]

                if board[i][j] == 0:
                    for ii in board[i]:
                        if ii in tmp:
                            tmp.pop(tmp.index(ii))

                    for jj in board.T[j]:
                        if jj in tmp:
                            tmp.pop(tmp.index(jj))
                    
                    x0 = (i // dim_grid)*dim_grid
                    y0 = (j // dim_grid)*dim_grid

                    for x in range(dim_grid):
                        for y in range(dim_grid):
                            if board[x0+x][y0+y] in tmp:
                                tmp.pop(tmp.index(board[x0+x][y0+y]))

                    if len(tmp) > 1:
                        rand =  random.randrange(len(tmp))
                        board[i][j] = tmp[rand]
                    elif len(tmp) == 1:
                        board[i][j] = tmp[0]
                    else:
                        continue
            
    
        return board


    def __checker(self, board):
        n = len(board)
        total = sum([ i for i in range(1, n+1)])
        check = 0
        for i in range(0, n):
            check += board[i].sum()
            check += board.T[i].sum()

        return check / (2 * n) == total


    def solve(self):
        while True:
            solve_board = self.__solve()
            if self.__checker(solve_board):
                break
        return solve_board

def main():
    
    with open(args.file, 'r') as f:
        files = f.readlines() 
    sudokusolver = SudokuSolver(args.file)
    print("The Board: \n", sudokusolver._get_board())
    print("\nResult:")
    print(sudokusolver.solve())


if __name__ == "__main__":
    main()


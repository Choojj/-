import sys

def backtraking(depth):
    global exit_flag

    if (depth == len(blank_list)):
        exit_flag = True
        for i in range(9):
            for j in range(9):
                print(sudoku_board[i][j], end = " ")
            print()
    
    else:
        for k in range(1, 10):
            if (exit_flag):
                break

            if (row_check(blank_list[depth][0], k) and column_check(blank_list[depth][1], k) and box_check(blank_list[depth][0], blank_list[depth][1], k)):
                sudoku_board[blank_list[depth][0]][blank_list[depth][1]] = k
                backtraking(depth + 1)
                sudoku_board[blank_list[depth][0]][blank_list[depth][1]] = 0

def row_check(row, cell):
    for i in range(9):
        if (sudoku_board[row][i] == cell):
            return False
    return True

def column_check(column, cell):
    for i in range(9):
        if (sudoku_board[i][column] == cell):
            return False
    return True

def box_check(row, column, cell):
    for i in range(row // 3 * 3, row // 3 * 3 + 3):
        for j in range(column // 3 * 3, column // 3 * 3 + 3):
            if (sudoku_board[i][j] == cell):
                return False
    return True

sudoku_board = []
blank_list = []

for i in range(9):
    sudoku_board.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if (sudoku_board[i][j] == 0):
            blank_list.append([i, j])

exit_flag = False

backtraking(0)
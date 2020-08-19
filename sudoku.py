import numpy as np

def gen_row():
    current_row = []
    for i in range(9):
        random_int = np.random.randint(1, 10)
        while(current_row.__contains__(random_int)):
            random_int = np.random.randint(1, 10)
            if current_row.__contains__(random_int) == False:
                break
        current_row.append(random_int)
    return current_row

def row_copy_check(a, b):
    for i in range(len(a)):
        if(a[i] == b[i]):
            return True

def gen_board():
    board = [gen_row()]
    for i in range(8):
        current_row = gen_row()
        while row_copy_check(board[len(board)-1], current_row):
            current_row = gen_row()
        board.append(current_row)
    return board


def column_copy_check(board):
    for column in range(len(board[0])):
        current_column = []
        for row in range(len(board)):
            current_column.append(board[row][column])
        seen = []
        duplicates = []
        for i in current_column:
            if seen.__contains__(i):
                duplicates.append(i)
            seen.append(i)
        if duplicates != []:
            return True

trial, board = 0, gen_board()
while column_copy_check(board):
    trial += 1
    print("Trial " + str(trial))
    board = gen_board()
for row in board:
    print(row)

# worlds-slowest-sudoku-table-maker

I've tackled some pretty complex programming projects, some include making games and creating applications, but for the life of me I cant seem to solve what seems to be a simple challange of generating a sudoku board. I've gone out of my way to avoid looking up the algorithm online and came with my own. It functions on a trial and error system; generate a board if the board doesn't meet the correct parameters generate it again. My algorithm seems to do well in minimizing the maximum amount of permutations.

'''python
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
'''
This program is structured into four functions and a while loop. The first function as seen above generates a row with the numbers one through nine in a random sequence.

'''python
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
'''
These two functions when used together are able to generate the board, whilst making sure that no columns have repeating integers.


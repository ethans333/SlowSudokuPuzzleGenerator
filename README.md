# A Very Slow Sudoku Board Generator 🐌

I've tackled some pretty complex programming projects, some include making games and creating applications, but for the life of me I cant seem to solve what seems to be a simple challange of generating a sudoku board. I've gone out of my way to avoid looking up the algorithm online and came with my own. It functions on a trial and error system; generate a board if the board doesn't meet the correct parameters generate it again. My algorithm seems to do well in minimizing the maximum amount of permutations. To make a sudoku board the parameters are as follows; each row and column should contain the numbers one through nine and with no duplicate intergers.

```python
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
```
This program is structured into four functions and a while loop. The first function as seen above generates a row with the numbers one through nine in a random sequence.

```python
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
```
These two functions when used together are able to generate the board, whilst making sure that no rows have repeating integers.

```python
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
```
The final function passes in the board as an argument and checks to see if any columns have repeating integers, if one does than the function returns ```python True```.

```python
trial, board = 0, gen_board()
while column_copy_check(board):
    trial += 1
    print("Trial " + str(trial))
    board = gen_board()
for row in board:
    print(row)
```
This block of code is executed when the program runs, generating a board with no repeating integers in the rows, and then checks to see if there so happens to be any repeating integers in the columns, if there is then the while loop re-trys at generating another board. The maximum amount of permutations it may take before the program guesses a correct board is 2^81 or, for you human computers out there, 2.4178516e+24. Im gonna keep trying at this algorithm and try to make it work without sucking. 

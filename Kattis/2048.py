# https://open.kattis.com/problems/2048

from sys import stdin

def main():
    board = get_board()
    board = perform_operation(board)
    print_board(board)

# Reads input and returns board
def get_board():
    board = []
    for _ in range(4):
        line = [int(x) for x in next(stdin).split(" ")]
        board.append(line)
    return board

# Calls nessicary function based on move specified in input
def perform_operation(board):
    move = int(next(stdin))
    if move == 0:
        board = left(board)
    if move == 1:
        board = up(board)
    if move == 2:
        board = right(board)
    if move == 3:
        board = down(board)
    return board

# Calls operate row on every row
def left(board):
    new_board = []
    for row in board:
        new_board.append(operate_row(row))
    return new_board

# Calls the operate row on every column
def up(board):
    new_board = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        new_row = []
        for j in range(4):
            new_row.append(board[j][i])
        new_row = operate_row(new_row)
        for j in range(4):
            new_board[j][i] = new_row[j]
    return new_board

# Same as left, just reversed
def right(board):
    new_board = []
    for row in board:
        new_board.append(reversed(operate_row(reversed(row))))
    return new_board

# Same as up, just reversed
def down(board):
    new_board = up(list(reversed(board)))
    return list(reversed(new_board))

# Performs the merging of each number in a row
def operate_row(row):
    new_row = [n for n in row if n != 0] # Without 0s
    row = []
    skip = False  # Ensures skipping if two numbers are added
    for i in range(len(new_row)):
        if skip:  # Skip if previous numbers were merged
            skip = False
            continue
        if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
            row.append(new_row[i] * 2)
            skip = True  # Skip since already merged
        else:
            row.append(new_row[i])
    while len(row) < 4: 
        row.append(0) # Readds 0s
    return row

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
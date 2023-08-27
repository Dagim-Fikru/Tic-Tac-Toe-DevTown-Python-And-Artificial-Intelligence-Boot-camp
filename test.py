board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
def constBoard(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
for i in range(0, 9):
    print("Enter the position you want to place your X or O")
    pos = int(input())
    if i % 2 == 0:
        board[pos] = "X"
    else:
        board[pos] = "O"
constBoard(board)
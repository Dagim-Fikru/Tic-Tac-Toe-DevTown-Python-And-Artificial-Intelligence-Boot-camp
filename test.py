board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
def constBoard(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
for i in range(9):
    if i>0 and i%3==0:
        print("\n")
    if board[i]==0:
        print("_", end=" ")
    elif board[i]==-1:
        print("X", end=" ")
    else:
        print("O", end=" ")
constBoard(board)
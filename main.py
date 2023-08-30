def constBoard(board):
    print("current board: \n\n")
    for i in range(9):
        if i>0 and i%3==0:
            print("\n")
        if board[i]==0:
            print("_", end=" ")
        elif board[i]==-1:
            print("X", end=" ")
        elif board[i]==1:
            print("O", end=" ")
        else:
            print("Error")
    print("\n\n")
def playerTurn(board):
    position = input("Enter position from 1-9\n")
    position = int(position)
    if board[position-1]==0:
        board[position-1]=-1
    else:
        print("Wrong position")
        playerTurn(board)
def player2Turn(board):
    position = input("Enter position from 1-9\n")
    position = int(position)
    if board[position-1]==0:
        board[position-1]=1
    else:
        print("Wrong position")
        player2Turn(board)
def main():
    choice = input("How do you want to play \n 1-Single player \n 2-Multiplyer \n")
    choice = int(choice)
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
    if choice==1:
        print("Computer: O\n You:X")
        player = input("Enter to play 1st or 2nd\n 1-first\n 2-second\n")
        player = int(player)
        for i in range(9):
            if analyzeboard(board)!=0:
                break
            if (i+player)%2==0:
                compTurn(board)
            else:
                constBoard(board)
                playerTurn(board)
    elif choice==2:
        print("Player 1: O\n Player 2:X")
        for i in range(9):
            if analyzeboard(board)!=0:
                break
            if i%2==0:
                constBoard(board)   
                playerTurn(board)
            else:
                constBoard(board)
                player2Turn(board)   
    else:
        print("Wrong choice")
    x = analyzeboard(board) 
    if x==0:
        constBoard(board)
        print("Draw")
    elif x==-1:
        constBoard(board)
        print("Player 1 wins")
    elif x==1:
        constBoard(board)
        print("Player 2 wins")
    else:
        constBoard(board)
        print("Computer wins")


        
    
main()

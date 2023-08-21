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
            



        
    
main()

 # Main Function
def TicTacToe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Helper function to print the board
    def PrintBoard():
        print()
        print('', board[0], "|", board[1], "|", board[2])
        print("---|---|---")
        print('', board[3], "|", board[4], "|", board[5])
        print("---|---|---")
        print('', board[6], "|", board[7], "|", board[8])
        print()

    # Get the number of the move
    def GetMove():
        while True:
            num = input()
            try:
                num = int(num)
                if(num > 0 and num < 10):
                    return num
                else:
    	            print("Please select an available numbered spot.\n")
            except ValueError:
                print("Please enter a valid number.\n")

    # Check if a player is winning
    def isWinning(player):
        MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6]
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and z != x:
                        if board[x] == player and board[y] == player and board[z] == player:
                            if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                                return True

        if board.count("X") + board.count("O") == 9:
            print("The game has ended in a tie.")
            return True

    # Performs a player turn and checks if a space is preoccupied
    def Turn(player):
        print("Choose a box player", player)
        index = GetMove() - 1
        if board[index] == "X" or board[index] == "O":
            print("Box already occupied. Try another one\n")
            Turn(player)
        else:
            board[index] = player
    
    # Main game loop
    while True:
        PrintBoard()
        Turn("X")
        if isWinning("X"):
            print("X wins!")
            break

        PrintBoard()
        Turn("O")
        if isWinning("O"):
            print("O wins!")
            break

TicTacToe()

 # Main Function
class TicTacToe():
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def play(self):
        # Main game loop
        while True:
            self.PrintBoard()
            self.Turn("X")
            if self.isWinning("X"):
                print("X wins!")
                break

            self.PrintBoard()
            self.Turn("O")
            if self.isWinning("O"):
                print("O wins!")
                break
    # Helper function to print the board
    def PrintBoard(self):
        print()
        print('', self.board[0], "|", self.board[1], "|", self.board[2])
        print("---|---|---")
        print('', self.board[3], "|", self.board[4], "|", self.board[5])
        print("---|---|---")
        print('', self.board[6], "|", self.board[7], "|", self.board[8])
        print()

    # Get the number of the move
    def GetMove(self):
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
    def isWinning(self, player):
        MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6]
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and z != x:
                        if self.board[x] == player and self.board[y] == player and self.board[z] == player:
                            if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                                return True

        if self.board.count("X") + self.board.count("O") == 9:
            print("The game has ended in a tie.")
            return True

    # Performs a player turn and checks if a space is preoccupied
    def Turn(self, player):
        print("Choose a box player", player)
        index = self.GetMove() - 1
        if self.board[index] == "X" or self.board[index] == "O":
            print("Box already occupied. Try another one\n")
            self.Turn(player)
        else:
            self.board[index] = player

tictactoe = TicTacToe()
tictactoe.play()

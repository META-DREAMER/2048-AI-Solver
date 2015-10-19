import random

class Engine:

    def __init__(self):
        self.size = 4
        self.board = [[0 for i in range(self.size)] for i in range(self.size)]
        self.score = 0
        self.numMoves = 0
        self.moveList = ['d','l','u','r']
        self.addRandBlock()
        self.addRandBlock()

    def scoreBonus(self, val):
        """
        Returns the score to add when tile merged
        """
        score = {
            2: 4, 
            4: 8, 
            8: 16, 
            16: 32, 
            32: 64, 
            64: 128, 
            128: 256, 
            256: 512, 
            512: 1024, 
            1024: 2048, 
            2048: 4096, 
            4096: 8192,
            8192: 16384,
            16384: 32768,
            32768: 65536,
            65536: 131072,
        }
        return score[val]

    def rotateBoard(self, board, count):
        """
        Rotate the board in order to make moves in different directions 
        """
        for c in range(count):
            rotated = [[0 for i in range(self.size)] for i in range(self.size)]

            for row in range(self.size):
                for col in range(self.size):
                    rotated[self.size - col - 1][row] = board[row][col]

            board = rotated

        return rotated

    def makeMove(self, moveDir):
        """
        Shift the board to make the given move
        """
        # Check if the game is already over
        if self.gameOver(): 	
            pass

        board = self.board		

        # Set how many rotations based on the move
        rotateCount = self.moveList.index(moveDir) 
        moved = False

        # Rotate board to orient the board downwards
        if rotateCount:				
            board = self.rotateBoard(board, rotateCount)

        #make an array to track merged tiles
        merged = [[0 for i in range(self.size)] for i in range(self.size)] 


        for row in range(self.size - 1):
            for col in range(self.size):

                currentTile = board[row][col]
                nextTile = board[row+1][col]

                #go to next tile if current tile is empty
                if not currentTile:
                    continue 

                #if next position is empty, move all tiles down
                if not nextTile:
                    for x in range(row+1):
                        board[row-x+1][col] = board[row-x][col]
                    board[0][col] = 0
                    moved = True
                    continue
                #if tile was merged already, go to next tile
                if merged[row][col]:
                    continue

                if currentTile == nextTile:
                    #if three consecutive tiles of same value, dont merge first two
                    if (row < self.size - 2 and nextTile == board[row+2][col]):
                        continue     

                    #merge tiles and set new value, shift all other tiles down
                    board[row+1][col] *= 2                      
                    for x in range(row):
                        board[row-x][col] = board[row-x-1][col]
                    board[0][col] = 0

                    #mark tile as merged and add appropriate score
                    merged[row+1][col] = 1                      
                    self.score += self.scoreBonus(currentTile)  
                    moved = True

        #return board to original orientation
        if rotateCount:
            board = self.rotateBoard(board, 4 - rotateCount)

        self.board = board

        #if tiles were moved, increment number of moves and add a random block
        if moved:
            self.numMoves += 1
            self.addRandBlock()


    def addRandBlock(self, val=None):
        """
        Places a random tile (either 2 or 4) on the board
        tile = 4: 10 percent chance 
        tile = 2: 90 percent chance
        """
        avail = self.availableSpots()

        if avail:
            (row, column) = avail[random.randint(0, len(avail) - 1)]

            if random.randint(0,9) == 9:
                self.board[row][column] = 4
            else:
                self.board[row][column] = 2


    def availableSpots(self):
        """
        Returns a list of all empty spaces on the board
        """
        spots = []
        for row in enumerate(self.board):
            for col in enumerate(row[1]):
                if col[1] == 0:
                    spots.append((row[0], col[0]))
        return spots

    def gameOver(self):
        """
        Returns True if no move can be made
        """
        if self.availableSpots():
            return False

        board = self.board
        for row in range(self.size):
            for col in range(self.size):
                if (row < self.size - 1 and board[row][col] == board[row+1][col]) \
                or (col < self.size - 1 and board[row][col] == board[row][col+1]):
                    return False
        return True

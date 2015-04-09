import random

class Engine:
	''' initializing Engine class'''
    def __init__(self):
        self.size = 4
        self.board = [[0 for i in range(self.size)] for i in range(self.size)]
        self.score = 0
        self.numMoves = 0
        self.moveList = ['d','l','u','r']
        self.addRandBlock()
        self.addRandBlock()
	''' Function to add bonus score on merging'''
    def scoreBonus(self, val):
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
	''' Rotate the board in order to make moves in different directions '''
    def rotateBoard(self, board, count):
        for c in range(count):
            rotated = [[0 for i in range(self.size)] for i in range(self.size)]

            for row in range(self.size):
                for col in range(self.size):
                    rotated[self.size - col - 1][row] = board[row][col]

            board = rotated

        return rotated
	''' Make the appropriate move '''
    def makeMove(self, moveDir):
        if self.gameOver(): 	# Check if the game is already over
            pass

        board = self.board		
        rotateCount = self.moveList.index(moveDir) # Keep a track of the rotations
        moved = False
        
        if rotateCount:				# if required rotate the board
            board = self.rotateBoard(board, rotateCount)

        merged = [[0 for i in range(self.size)] for i in range(self.size)]

        for row in range(self.size - 1):
            for col in range(self.size):

                currentTile = board[row][col]
                nextTile = board[row+1][col]

                if not currentTile:
                    continue

                if not nextTile:
                    for x in range(row+1):
                        board[row-x+1][col] = board[row-x][col]
                    board[0][col] = 0
                    moved = True
                    continue

                if merged[row][col]:
                    continue

                if currentTile == nextTile:
                    if (row < 2 and nextTile == board[row+2][col]):
                        continue
                    board[row+1][col] *= 2
                    for x in range(row):
                        board[row-x][col] = board[row-x-1][col]
                    board[0][col] = 0
                    merged[row+1][col] = 1
                    self.score += self.scoreBonus(currentTile)
                    moved = True

        if rotateCount:
            board = self.rotateBoard(board, 4 - rotateCount)

        self.board = board

        if moved:
            self.numMoves += 1
            self.addRandBlock()


    def addRandBlock(self, val=None):
        avail = self.availableSpots()

        if avail:
            (row, column) = avail[random.randint(0, len(avail) - 1)]

            if random.randint(0,9) == 9:
                self.board[row][column] = 4
            else:
                self.board[row][column] = 2


    def availableSpots(self):
        spots = []
        for row in enumerate(self.board):
            for col in enumerate(row[1]):
                if col[1] == 0:
                    spots.append((row[0], col[0]))
        return spots

    def gameOver(self):
        if self.availableSpots():
            return False

        board = self.board
        for row in range(self.size):
            for col in range(self.size):
                if (row < self.size - 1 and board[row][col] == board[row+1][col]) \
                or (col < self.size - 1 and board[row][col] == board[row][col+1]):
                    return False
        return True

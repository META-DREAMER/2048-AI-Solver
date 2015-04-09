import random

class Engine:
    def __init__(self):
        self.board = [[0 for i in range(4)] for i in range(4)]
        self.score = 0
        self.moves = 0
        self.addRandBlock()
        self.addRandBlock()

    def left(self):
        self.moves += 1
        self.makeMove(1)

    def right(self):
        self.moves += 1
        self.makeMove(3)

    def up(self):
        self.moves += 1
        self.makeMove(2)

    def down(self):
        self.moves += 1
        self.makeMove()

    def rotateBoard(self, board, count):
        for c in range(0, count):
            rotated = [[0 for i in range(len(board))] for i in range(len(board[0]))]

            rows = len(board)

            for row in range(0, rows):
                columns = len(board[row])
                for column in range(0, columns):
                    rotated[columns - column - 1][row] = board[row][column]

            board = rotated

        return rotated

    def makeMove(self, rotateCount = 0):
        board = self.board
        
        if rotateCount:
            board = self.rotateBoard(board, rotateCount)

        merged = [[0 for i in range(len(board[0]))] for i in range(len(board))]

        for row in range(0, len(board) - 1):
            for item in range(0, len(board[row])):

                currentCell = board[row][item]
                nextCell = board[row+1][item]

                if not currentCell:
                    continue
                if not nextCell:
                    for x in range(row+1):
                        board[row-x+1][item] = board[row-x][item]
                    board[0][item] = 0
                    continue

                if merged[row][item]:
                    continue

                if currentCell == nextCell:
                    board[row+1][item] *= 2
                    for x in range(row):
                        board[row-x][item] = board[row-x-1][item]
                    board[0][item] = 0
                    merged[row+1][item] = 1
                    self.score += self.scoreBonus(currentCell)
     

        if rotateCount:
            board = self.rotateBoard(board, 4 - rotateCount)

        self.board = board
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
            for item in enumerate(row[1]):
                if item[1] == 0:
                    spots.append((row[0], item[0]))

        return spots

    def isBoardLocked(self):
        if self.availableSpots():
            return False

        board = self.board
        size = len(board[0])

        for row in range(0, size):
            for item in range(0, size):
                if (row < size - 1 and board[row][item] == board[row+1][item]) \
                or (item < size - 1 and board[row][item] == board[row][item+1]):
                    return False

        return True

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
            32768: 65536
        }

        return score[val]

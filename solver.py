import engine, sys, random, os
import curses

COLORS = {
		0:	  0,
        2:    1,
        4:    2,
        8:    3,
        16:   4,
        32:   5,
        64:   6,
        128:  7,
        256:  8,
        512:  9,
        1024: 10,
        2048: 11,
        # just in case people set an higher goal they still have colors
        4096: 12,
        8192: 11,
    }

def makegame():
	game = engine.Engine()
	return game

def cursesBoard(board, screen):
	screen.clear()
	screen.border(0)
	for row in enumerate(board):
		for item in enumerate(row[1]):
			screen.addstr(8+3*row[0], 40+6*item[0], str(item[1]), curses.color_pair(COLORS[item[1]]))
	screen.refresh()

def copyBoard(board):
	newBoard = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for row in enumerate(board):
		for item in enumerate(row[1]):
			newBoard[row[0]][item[0]] = item[1]

	return newBoard

def run_random(board, move):
	randomGame = makegame()
	randomGame.board = copyBoard(board)
	moveList = ['u','d','l','r']
	numMoves = 0

	sendMove(randomGame, move)

	while True:
		if randomGame.is_board_locked():
			break

		randMove = moveList[random.randint(0, 3)]
		sendMove(randomGame, randMove)
		numMoves += 1

	return [randomGame.score, numMoves]

def bestMove(board, runs):

	average = 0
	bestScore = 0
	moveList = ['u','d','l','r']

	for moveDir in moveList:
		average = 0
		for x in range(runs):
			simGame = makegame()
			simGame.board = copyBoard(board)
			result = run_random(board, moveDir)
			average += result[0]

		average = average/runs
		if average > bestScore:
			bestScore = average
			move = moveDir
	return move

def sendMove(game, move):
	if move == 'u':
		game.up()
	elif move == 'd':
		game.down()
	elif move == 'l':
		game.left()
	elif move == 'r':
		game.right()

def solveGame(runs, screen):
	end = False
	mainGame = makegame()
	counter = 0
	while not end:
		move = bestMove(mainGame.board, runs)
		counter += 1
		
		cursesBoard(mainGame.board, screen)

		if move == 'u':
			mainGame.up()
		elif move == 'd':
			mainGame.down()
		elif move == 'l':
			mainGame.left()
		elif move == 'r':
			mainGame.right()

		if mainGame.is_board_locked():
			end = True
			
			return(mainGame)


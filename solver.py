import engine, sys, random, os, curses

COLORS = {0:0,2:1,4:2,8:3,16:4,32:5,64:6,128:7,256:8,512:9,1024:10,2048:11,4096:12,8192:13,16384:13}
moveList = ['u','d','l','r']

def makegame():
	game = engine.Engine()
	return game

def cursesBoard(board, screen):
	for row in enumerate(board):
		for item in enumerate(row[1]):
			screen.addstr(8+3*row[0], 40+6*item[0], str(item[1]), curses.color_pair(COLORS[item[1]]))
	screen.refresh()

def copyBoard(board):
	newBoard = makegame().board
	for row in enumerate(board):
		for item in enumerate(row[1]):
			newBoard[row[0]][item[0]] = item[1]
	return newBoard

def runRandom(board, move):
	randomGame = makegame()
	randomGame.board = copyBoard(board)
	sendMove(randomGame, move)

	while True:
		if randomGame.is_board_locked():
			break
		randMove = moveList[random.randint(0, 3)]
		sendMove(randomGame, randMove)
	return randomGame.score

def bestMove(board, runs):
	average = 0
	bestScore = 0

	for moveDir in moveList:
		average = 0
		for x in range(runs):
			result = runRandom(board, moveDir)
			average += result
		average = average/runs
		if average > bestScore:
			bestScore = average
			move = moveDir
	return move

def sendMove(game, move):
	if move == moveList[0]:
		game.up()
	elif move == moveList[1]:
		game.down()
	elif move == moveList[2]:
		game.left()
	elif move == moveList[3]:
		game.right()

def solveGame(runs, screen):
	mainGame = makegame()
	counter = 0
	while True:
		if mainGame.is_board_locked():
			break
		move = bestMove(mainGame.board, runs)
		sendMove(mainGame, move)
		screen.clear()
		screen.border(0)
		cursesBoard(mainGame.board, screen)
	return(mainGame)
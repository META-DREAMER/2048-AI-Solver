import engine, random, curses

COLORS = {0:0,2:1,4:2,8:3,16:4,32:5,64:6,128:7,256:8,512:9,1024:10,2048:11,4096:12,8192:13,16384:13,32768:12}
moveList = ['u','d','l','r']

def makeGame():
	game = engine.Engine()
	return game

def drawBoard(board, screen):
	for row in enumerate(board):
		for item in enumerate(row[1]):
			screen.addstr(8+3*row[0], 40+6*item[0], str(item[1]), curses.color_pair(COLORS[item[1]]))
	screen.refresh()

def copyBoard(board):
	newBoard = makeGame().board
	for row in enumerate(board):
		for item in enumerate(row[1]):
			newBoard[row[0]][item[0]] = item[1]
	return newBoard

def runRandom(board, firstMove):
	randomGame = makeGame()
	randomGame.board = copyBoard(board)
	sendMove(randomGame, firstMove)

	while True:
		if randomGame.isBoardLocked():
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

		if average >= bestScore:
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
	mainGame = makeGame()
	counter = 0
	while True:
		if mainGame.isBoardLocked():
			break
		if runs > 0:
			move = bestMove(mainGame.board, runs)
		else:
			move = moveList[random.randint(0, 3)]
		sendMove(mainGame, move)
		screen.clear()
		screen.border(0)
		drawBoard(mainGame.board, screen)
	return(mainGame)
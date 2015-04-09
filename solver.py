import engine, random, curses

COLORS = {0:0,2:1,4:2,8:3,16:4,32:5,64:6,128:7,256:8,512:9,1024:10,2048:11,4096:12,8192:13,16384:13,32768:12}

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
	moveList = randomGame.moveList
	randomGame.board = copyBoard(board)
	randomGame.makeMove(firstMove)

	while True:
		if randomGame.gameOver():
			break
		randMove = moveList[random.randint(0, len(moveList) - 1)]
		randomGame.makeMove(randMove)

	return randomGame.score

def bestMove(game, runs):
	average = 0
	bestScore = 0
	moveList = game.moveList

	for moveDir in moveList:
		average = 0
		for x in range(runs):
			result = runRandom(game.board, moveDir)
			average += result
		average = average/runs
		if average >= bestScore:
			bestScore = average
			move = moveDir

	return move

def solveGame(runs, screen):
	mainGame = makeGame()
	counter = 0
	moveList = mainGame.moveList

	while True:
		if mainGame.gameOver():
			break
		if runs > 0:
			move = bestMove(mainGame, runs)
		else:
			move = moveList[random.randint(0, len(moveList) - 1)]
		mainGame.makeMove(move)
		screen.clear()
		drawBoard(mainGame.board, screen)

	return(mainGame)
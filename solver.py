import engine, random, curses

COLORS = {0:0,2:1,4:2,8:3,16:4,32:5,64:6,128:7,256:8,512:9,1024:10,2048:11,4096:12,8192:13,16384:13,32768:12,65536:12}

def makeGame():
	"""
	Creates a new instance of a game
	"""
	game = engine.Engine()
	return game

def drawBoard(board, screen):
	"""
	Draws a given board on a given curses screen
	"""
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
	"""
	Returns the end score of a given board played randomly after moving in a given direction.
	"""
	randomGame = makeGame()					#make a new game
	moveList = randomGame.moveList
	randomGame.board = copyBoard(board) 	#copy the given board to the new game
	randomGame.makeMove(firstMove) 			#send the initial move

	while True:								#keep sending random moves until game is over
		if randomGame.gameOver():
			break
		randMove = random.choice(moveList)
		randomGame.makeMove(randMove)

	return randomGame.score

def bestMove(game, runs):
	"""
	Returns the best move for a given board.
	Plays "runs" number of games for each possible move and calculates which move had best avg end score.
	"""
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
	"""
	AI that plays a game till the end given a number of runs to make per move

	"""
	mainGame = makeGame()
	moveList = mainGame.moveList
	isDynamic = False

	#If runs is set to dynamic, increase the number of runs as score increases
	if runs == 'Dynamic':
		isDynamic = True

	while True:
		if mainGame.gameOver():
			break

		if isDynamic:
			runs = int(1 + (0.01)*mainGame.score)

		if runs > 0:
			move = bestMove(mainGame, runs)
		else:
			move = random.choice(moveList)
			
		mainGame.makeMove(move)
		screen.clear()
		drawBoard(mainGame.board, screen)

	return(mainGame)
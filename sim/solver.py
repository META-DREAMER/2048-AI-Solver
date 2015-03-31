from interface import *


def makegame():
	game = engine.Engine()
	# print(game.board)
	return game


def bestMove(board, runs):
	simGame = makegame()
	simGame.board = board
	upAvg = 0
	downAvg = 0
	leftAvg = 0
	rightAvg = 0
	upNum = 1
	downNum = 1
	leftNum = 1
	rightNum = 1

	for x in range(runs):
		random.seed(123 + 6*x)
		result = run_simulation('./bot.py', simGame)
		print(result)
		if result[0] == 'u':
			upAvg += result[1]
			upNum += 1
		elif result[0] == 'd':
			downAvg += result[1]
			downNum += 1
		elif result[0] == 'l':
			leftAvg += result[1]
			leftNum += 1
		elif result[0] == 'r':
			rightAvg += result[1]
			rightNum += 1

	# print("1: " + str(upAvg))
	# print("2: " + str(downAvg))
	# print("3: " + str(leftAvg))
	# print("4: " + str(rightAvg))

	upAvg = upAvg/upNum
	downAvg = downAvg/downNum
	leftAvg = leftAvg/leftNum
	rightAvg = rightAvg/rightNum

	# print("5: " + str(upAvg))
	# print("6: " + str(downAvg))
	# print("7: " + str(leftAvg))
	# print("8: " + str(rightAvg))

	scoreList = [upAvg,downAvg,leftAvg,rightAvg]
	highScore = max(scoreList)
	# print("9: " + str(highScore))
	index = scoreList.index(highScore)

	if index == 0:
		return 'u'
	elif index == 1:
		return 'd'
	elif index == 2:
		return 'l'
	elif index == 3:
		return 'r'



def displayBoard(board):
	print(board)


end = False
mainGame = makegame()
runs = 5
counter = 0

while not end:

	move = bestMove(mainGame.board, runs)
	counter += 1

	if move == 'u':
		mainGame.up()
	elif move == 'd':
		mainGame.down()
	elif move == 'l':
		mainGame.left()
	elif move == 'r':
		mainGame.right()

	# displayBoard(mainGame.board)

	if mainGame.is_board_locked():
		end = True
		print(counter)
		print("Game over")
		#end game
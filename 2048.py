from solver import *

x = 0
runs = 0

screen = curses.initscr()
curses.curs_set(0)
curses.noecho()
screen.clear()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_CYAN)
curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_BLUE)
curses.init_pair(12, curses.COLOR_BLACK, curses.COLOR_YELLOW)
curses.init_pair(13, curses.COLOR_BLACK, curses.COLOR_WHITE)
drawBoard(makeGame().board, screen)

def getRuns():
	curses.echo()
	screen.clear()
	screen.border(0)
	screen.addstr(13, 14, "(reccomended: 75 if using PyPy, 10 if not)")
	screen.addstr(12, 14, "Enter the number of runs per move: ")
	screen.refresh()
	try:
		runs = int(screen.getstr(12, 50, 4))
	except ValueError:
		runs = 0
	screen.clear()
	curses.noecho()
	return runs

def drawEnd(game, screen):
	screen.clear()
	drawBoard(game.board, screen)
	screen.addstr(15, 5, "Score: " + str(game.score),curses.color_pair(3))
	screen.addstr(16, 5, "Moves: " + str(game.numMoves),curses.color_pair(3))
	screen.addstr(18, 5, "GAME OVER",curses.color_pair(4))
	screen.refresh()

while True:
	screen.border(0)
	screen.addstr(2, 24, "2048 Machine Learning AI", curses.color_pair(1))
	screen.addstr(3, 20, "- Hammad Jutt", curses.color_pair(0))
	screen.addstr(7, 5, "Runs per move: " + str(runs), curses.color_pair(2))
	screen.addstr(9, 5, "Please select an option", curses.color_pair(4))
	screen.addstr(10, 5, "1 - Set runs per move")
	screen.addstr(11, 5, "2 - Enable dynamic runs per move")
	screen.addstr(12, 5, "3 - Start AI")
	screen.addstr(13, 5, "4 - Exit")
	screen.refresh()

	x = screen.getch()
	if x == ord('1'):
		runs = getRuns()
	if x == ord('2'):
		runs = 'Dynamic'		
	if x == ord('3'):
		drawEnd(solveGame(runs, screen), screen)
	if x == ord('4'):
		break

curses.echo()
curses.endwin()
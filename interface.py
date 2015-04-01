from solver import *

# random.seed(sys.argv[1])


def getRuns():
	screen.clear()
	screen.border(0)
	screen.addstr(12, 14, "Enter the number of runs per move: ")
	screen.refresh()
	runs = -1
	try:
		runs = int(screen.getstr(12, 50, 4))
	except ValueError:
		pass

	if runs > 0:
		return runs
	return 1

def drawEnd(game, screen):
	screen.clear()
	cursesBoard(game.board, screen)
	screen.addstr(15, 5, "Score: " + str(game.score),curses.color_pair(3))
	screen.addstr(20, 45, "GAME OVER",curses.color_pair(4))
	screen.refresh()



x = 0
runs = 10
score = 0

screen = curses.initscr()
curses.curs_set(0)
screen.clear()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_CYAN)
curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLUE)
curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_YELLOW)
curses.init_pair(12, curses.COLOR_BLACK, curses.COLOR_WHITE)

while x != ord('3'):

	screen.border(0)
	screen.addstr(2, 24, "2048 Machine Learning AI", curses.color_pair(1))
	screen.addstr(3, 20, "- Hammad Jutt & Shivansh Singla", curses.color_pair(0))
	screen.addstr(7, 5, "Runs per move: " + str(runs), curses.color_pair(2))


	screen.addstr(9, 5, "Please select an option", curses.color_pair(4))
	screen.addstr(10, 5, "1 - Change runs per move")
	screen.addstr(11, 5, "2 - Run and solve game")
	screen.addstr(12, 5, "3 - Exit")
	
	screen.refresh()

	
	x = screen.getch()

	if x == ord('1'):
		runs = getRuns()
		curses.endwin()
		screen.clear()
	if x == ord('2'):
		drawEnd(solveGame(runs, screen), screen)
		curses.endwin()
	if x == ord('3'):
		curses.endwin()

curses.endwin()
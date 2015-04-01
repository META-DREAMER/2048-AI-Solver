from solver import *

# random.seed(sys.argv[1])


def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input



x = 0
runs = 5
score = 0

while x != ord('3'):
	screen = curses.initscr()
	curses.noecho()
	curses.start_color()
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

	screen.clear()
	screen.border(0)
	screen.addstr(2, 20, "2048 Machine Learning Algorithm", curses.color_pair(1))
	screen.addstr(4, 20, "Number of runs per move: " + str(runs))


	screen.addstr(6, 25, "Please select an option")
	screen.addstr(7, 25, "1 - Set number of runs")
	screen.addstr(8, 25, "2 - Run Algorithm")
	screen.addstr(9, 25, "3 - Exit")
	screen.addstr(13, 25, "Score: " + str(score))
	screen.refresh()

	x = screen.getch()

	if x == ord('1'):
		runs = int(get_param("Enter the number of runs per move"))
		curses.endwin()
	if x == ord('2'):
		score = solveGame(runs, screen)
		curses.endwin()
	if x == ord('3'):
		curses.endwin()

curses.endwin()
#!/usr/bin/env python3
import random
from bothelper import read_board, upBot, downBot, leftBot, rightBot, botsetup

s = botsetup("random-example")

previous_score = 0


while True:
	score = read_board(s)

	direction = random.randint(1, 4)

	if direction == 1:
		upBot(s)
	elif direction == 2:
		downBot(s)
	elif direction == 3:
		leftBot(s)
	else:
		rightBot(s)
#!/usr/bin/env python3
import engine, sys, uuid, random, subprocess, socket, os, time
import platform

# if len(sys.argv) < 3:
# 	sys.stderr.write("Usage: interface.py <randomseed> <executable>\n")
# 	sys.exit()

# set up seed from arguments
# random.seed(sys.argv[1])

# helpers for writing and reading to the socket connection
def write(conn, str):
	conn.send(str.encode("utf-8"))

def read(conn):
	return conn.recv(1024).decode("utf-8").strip()


def run_simulation(bot, game):

	identifier = ""

	if platform.system() == 'Windows':
		print ("Must connect differently")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(("", 8765))
		print (bot)
		process = subprocess.Popen([sys.executable, bot, '8765'])
	else:
		# create local unix socket for communication with child
		s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		s.settimeout(2)
		identifier = str(uuid.uuid4())
		s_path = "/tmp/4096-" + identifier
		s.bind(s_path)

		# launch child
		process = subprocess.Popen([bot, s_path])
	s.listen(1)
	conn, addr = s.accept()

	# set up engine and game meta information
	
	move_count = 0
	game_name = read(conn)

	# sys.stderr.write("Game: " + game_name + "\n")
	# sys.stderr.write("Identifier: " + identifier + "\n")

	# give client board and process input until finished
	write(conn, game.to_string())

	firstMove = True
	output = []

	try:
		while conn:
			c = read(conn)
			if firstMove:
				output.append(c)
				firstMove = False
			if c == 'u':
				game.up()
			elif c == 'd':
				game.down()
			elif c == 'l':
				game.left()
			elif c == 'r':
				game.right()

			write(conn, game.to_string())

			move_count += 1

			if game.is_board_locked():
				write(conn, "FIN " + str(game.score) + "\n")

				

	except (socket.timeout):
		sys.stderr.write(" * Socket timed out.\n")
	#except (BrokenPipeError, ConnectionResetError):
	except:
		pass

	# give score
	# sys.stderr.write("Score: " + str(game.score) + "\n")
	# sys.stderr.write("Moves: " + str(move_count) + "\n")

	# clean up
	process.terminate()
	if not platform.system() == 'Windows':
		os.remove(s_path)
	output.append(game.score)
	return output

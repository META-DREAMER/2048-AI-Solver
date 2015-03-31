import platform
import sys, socket


def read_board(s):
	board = []
	lines = s.recv(4096).decode("utf-8").split("\n")

	for line in lines:
		line = line.strip()

		if line.startswith("=="):
			return (board, int(line[3:]))

		if line.startswith("FIN"):
			# print("Done: " + line[4:])
			sys.exit()

		board.append(line.split(" "))

	return board

def upBot(s):
	s.send("u\n".encode("utf-8"))

def downBot(s):
	s.send("d\n".encode("utf-8"))

def leftBot(s):
	s.send("l\n".encode("utf-8"))

def rightBot(s):
	s.send("r\n".encode("utf-8"))


def botsetup(name):
	if platform.system() == 'Windows':
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("127.0.0.1", 8765))
	else:
		s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		s.connect(sys.argv[1])

	# register name
	name += "\n"
	s.send(name.encode("utf-8"))

	return s

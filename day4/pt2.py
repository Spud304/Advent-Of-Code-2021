import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

ll = [x for x in open(filename).read().strip().split('\n')]

numbers = ll[0]
boards = [[y.split() for y in x.split("\n")] for x in open(filename).read().strip().split('\n\n')][1:]

def checkwin(board):
	for i in range(5):
		works = True
		for j in range(5):
			if board[i][j] is not None:
				works = False
		if works:
			return True
	for i in range(5):
		works = True
		for j in range(5):
			if board[j][i] is not None:
				works = False
		if works:
			return True
	return False

won = set()

for number in numbers.split(","):
	for k in range(len(boards)):
		board = boards[k]
		for line in board:
			for i in range(len(line)):
				if line[i] == number:
					line[i] = None
		if checkwin(board) and (k not in won):
			un = 0
			for line in board:
				for x in line:
					if x is not None:
						un += int(x)
			print(un*int(number))
			won.add(k)
# Torbert, 11.30.2004

def show(board):
	print
	for r in range(n):
		s = ""
		for c in range(n):
			if (r + c) % 2 == 1:
				s += chr(27) + "[31;46"
			else:
				s += chr(27) + "[31;43"
			s += "m"
			if board[c] == r:
				s += chr(27) + "[1m" + "X"
			else:
				s += " "
		print s + chr(27) + "[0m"
	print

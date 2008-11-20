from random import randint, seed,choice
n=8
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
def conflicts(x1,y1,x2,y2):
	if(x1==x2):
		return True
	if(y1==y2):
		return True
	if(abs(x1-x2)==abs(y1-y2)):
		return True
	return False

def heuristic(board):
	temp=0
	for i in range(n):
		for k in range(i+1,n):
			if conflicts(i,board[i],k,board[k]):
				temp+=1
	return temp
def hillclimbing():
	board=randomboard()
	bestboard=board
	minheuristic=heuristic(board)
	count=0
	while True:
		equalboards=[]
		choices=[]
		for k in range(n):
			for j in range(n):
				tempboard=board[:]
				tempboard[k]=j
				h=heuristic(tempboard)
				if(h==0):
					print "I win:"
					show(tempboard)
					return True
				if(h<minheuristic):
					choices.append(tempboard)
				if(h==minheuristic):
					equalboards.append(tempboard)
		if len(choices)==0:
			if len(equalboards)==1:
				print "I lose"
				return False
			else:
				count+=1
				if(count>200):
					print "I lose (timeout)"
					return False
				board=choice(equalboards)

		else:
			vals=[]
			sum=0
			for i in range(len(choices)):
				vals.append(minheuristic-heuristic(choices[i]))
				sum+=vals[i]
			
			randval=randint(0,sum-1)
			tsum=0
			for i in range(len(vals)):
				tsum+=vals[i]
				if randval<tsum:
					board=choices[i]
					break
			count=0


def randomboard():
	temp=[]
	for i in range(n):
		temp.append(randint(0,n-1))
	return temp
#board = [1,2,3,4,3,0]
#show(board)
#print heuristic(board)
k=0
count=0
while k<100:
	if hillclimbing():
		count+=1
	k+=1
print "%d out of 100"%count

#101045226
#Bradley Gray-Hall

maxQueue = 10
Queue = []
def enqueue (valtobeadded):
	if len(Queue) < maxQueue:
		Queue.append(valtobeadded)
		return True
	else:
		return False

def dequeue():
	if len(Queue) != 0:
		 return Queue.pop(0)
	else:
		return None

def peek():
	if len(Queue) != 0:
		return Queue[0]
	else:
		return None

def isempty():
	if len(Queue) == 0:
		return True
	else:
		return False

def getlist():
	return Queue

def multienqueue(inputlist):
	counter = 0
	while True:
		if len(Queue) < maxQueue:
			Queue.append(inputlist.pop(0))
			counter+=1
		if len(Queue) == maxQueue or len(inputlist) == 0:
			return counter
			break
def multidequeue(N):
	newList = []
	for i in range(0,N):
		if len(Queue) != 0:
			newList.append(Queue.pop(0))
		else:
			return newList
	return newList

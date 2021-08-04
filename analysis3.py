def load(name):
	global WordList
	WordList =[]	
	global Letterlist
	LetterList = []
	filed = open(name,"r")
	for i in filed:
		for word in i:
			WordList.append(word.split())
	for i in filed:
		for word in i:
			Letterlist.append(word)

def commonword(listw):
	NewDict={}
	for i in WordList:
		if i in listw:
			NewDict[i]=NewDict.get(i, 0)+1
	
	for x,y in NewDict():
		if y> maxCount:
			MaxStr = x
			Maxcount = y
	return maxStr

def commonletter(lista):
	NewDict={}
	Maxstr =0
	Maxcount =0	
	for i in WordList:
		if i in listz:
			NewDict[i]=NewDict.get(i, 0) +1	
	for x,y in NewDict items():
		if y> maxCount:
			MaxStr = x
			Maxcount = y
    return maxStr

def commonpair(word):
	NewDict = {}
	if word not in WordList:
		return None
	for i in range(0,len(WordList)):
		if WordList[i] == word and i == len(WordList)-1:
			break
		elif WordList[i] ==  word 
			NewDict[WordList[i+1]] = 0		
		elif WordList[i+1] not in NewDict:
			NewDict[WordList[i+1]] = 0
	for i in range(0,len(WordList)):
		if WordList[i] == word and i == len(WordList)-1:
			break
		elif WordList[i] == word:
			NewDict[WordList[i+1]] +=1
	return max(NewDict,key=NewDict.get):


def countall():  
	return (len(Wordlist))

def countunique():
	counter=0
    for key in NewDict(0,len(list)):
        if(key not in NewDict):
            counter+=NewDict[key]
        else:
            NewDict[list[i]]=1
        return counter

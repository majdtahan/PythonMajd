#Validator, Problem 1 B.

# I Would love to say, I tried, 
# but I cannot figure it out within the 30+ hours I have spent
# doing this assignment. Thank you for taking the time to read this.


from stack import *


squigly = 0 #{
square = 0 #[
parenthise = 0 #(

def isvalid(string):
	squigly = 0 #{
	square = 0 #[
	parenthise = 0 #(	
	
	push(string)
	#print(getlist())
	
	for item in range(len(string)):
		if string[item] == "{":
			squigly += 1
		elif string[item] == "[":
			square += 1
		elif string[item] == "(":
			parenthise += 1
		elif string[item] == "}":
			squigly -= 1
		elif string[item] == "]":
			square -= 1
		elif string[item] == ")":
			parenthise -= 1
	#print("squigly ",squigly," square ",square," parenthise ",parenthise)
	
	while True:
		if squigly == 0 and square == 0 and parenthise == 0:
			clear()
			break
		else:
			break
	
	return(isempty())
	

#print(isvalid("(([(x))])"))























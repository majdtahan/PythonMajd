from SimpleGraphics import *

n=int(input("Enter a number of rows/columns"))
#Check if input is a number that evenly divides 600 here #####

resize(600,600)
background("white")
setFill("black")
variable=600//n
for x in range(n):
	for y in range(n):
		if y % 2 ==0:
			rect(x*variable,y*variable,variable,variable)
		else:
			if y % 2 != 0:
				rect(x*variable,y*variable,variable,variable)

def multiply(int,num):
	if num==0:
		return 0
	else:
		int=int+multiply(int,num-1)
	

print(multiply(9,3))

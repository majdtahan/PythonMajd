#Validator.py Majd El-Tahan 101037041 

from stack import*

def isvalid(p):
    for c in range(0,len(p)):
        c = p[c]
        if c=="(" or c=="[" or c=="{":
            push(c)
        if c==")" or c=="]" or c=="}":
		if c,k != "[" or c,k != "]" c,k !="{" or c,k != "}" or c,k != "(" or c,k != ")":
			return false
		else:
            if isempty():
                return False
            k = pop()
            if c == ")" and k != "(" or c == "]" and k != "[" or c== "}" and k != "{" :
                return False
    return isempty()
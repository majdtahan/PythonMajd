
cache = {}
def factorial(n):
    if n = 0:
        return (1)
    if n <0:   # base case
       return "Not a valid answer, please enter a value greater or equal to 0"

   else:
       num =n*factorial(n - 1 )  # recursive call
       print(str(n) + '! = ' + str(num))
       return num
def cachedfactorial(n):

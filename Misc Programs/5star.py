#input a movie
#input a rating
#response to rating of the movie

movie=input("What is the title of your movie?: ")

rating=input("Input the number of stars out of 5 by using * : ")
#find a way to make 5 = ***** and so on... most likely involves a string

if len(rating) == 5:
	rating ="*"*len(rating)
	print("Wow you must have really liked the movie!")
if len(rating) == 4:
	rating ="*"*len(rating)
	print("I guess the movie was pretty good!")
if len(rating) == 3:
	rating ="*"*len(rating)
	print("The movie must have been not good or bad")
if len(rating) == 2:
	rating ="*"*len(rating)
	print("Must have been a boring movie")
if len(rating) == 1:
	rating ="*"*len(rating)
	print("I'm for sure not watching that")


print("The movie " + movie + " has a " + str(len(rating)) + " star rating!")

# Guess_the_Number program

from random import choice
def main():
    ComputerNumber = choice(range(1, 10))#computer generates a random number between 1 and 10
    print('I am thinking of a number between 1 and 10.') #shows instructions
    PlayerGuess = input('What is the number? ') #prompt player to input guess
    print('The number was', str(ComputerNumber) + '.') #prints the computer generated number
    print('You guessed', PlayerGuess + '.') #prints players guess

main()

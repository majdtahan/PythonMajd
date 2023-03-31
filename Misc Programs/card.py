#A deck of cards can be viewed as a list of cards, each of which can be described by a value and suit.
#Write a program to generate a deck of cards represented as a multi-dimensional list.
#How can you shuffle the deck of cards?How can you deal cards?How can you implement a simple card game (e.g., blackjack)?
import random

#"C, "S", "H", "D"
#1, 2, 3, ..., 12, 13

def valueofcard(card):
	if card[1] > 10:
		return 10
	return card[1]

def valueofhand(hand):
	value = 0
	hasace = False
	for card in hand:
		if valueofcard(card) == 1:
			hasace = True
		value += valueofcard(card)
	
	if hasace and value <= 11:
		value += 10
		
	return value

def dealhand(deck, numcards):
	hand = []
	for i in range(numcards):
		hand.append(deck.pop(0))
	return hand
	
def addtohand(deck, hand):
	hand.append(deck.pop(0))


def shuffle(deck):
	newdeck = []
	while len(deck) > 0:
		index = random.randint(0,len(deck)-1)
		card = deck.pop(index)
		newdeck.append(card)
	return newdeck


cards = []

for suit in ["C", "S", "H", "D"]:
	for value in range(1, 14):
		card = [suit, value] #["C", 4]
		cards.append(card)

cards = shuffle(cards)		
cards.insert(0, ["T", 1])
cards.insert(0, ["J", 1])
	
hand1 = []
while True:
	command = input("hit or stay: ")
	
	if command == "hit":
		addtohand(cards, hand1)
		print(hand1)
		print(valueofhand(hand1))
		if valueofhand(hand1) > 21:
			print("BUST!")
			break
	else:
		break

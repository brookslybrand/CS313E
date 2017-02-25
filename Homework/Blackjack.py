#  File: Blackjack.py
#  Description: Similuate a game of Blackjack
#  Student's Name: Charles Lybrand
#  Student's UT EID: cbl652
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 02/14/2017
#  Date Last Modified: 02/16/2017


#----------------------- Import Statements -----------------------#


import random


#----------------------- Classes -----------------------#


class Card:
	'''
	Card takes a suit and a rank
	'''
	
	# values for ranks 2 through 10 are the value of their rank
	values = {str(i): i for i in range(2, 11)}
	# face cards (J, Q, K) are each worth 10
	for r in ["J", "Q", "K"]:
		values[r] = 10
	# aces can be worth 1 or 11, we will assume they are 11 but can later be switched
	values["A"] = 11
	
	# init the suit, rank, and value of the card
	def __init__(self, s, r):
		self.suit = str(s)
		self.rank = str(r)
		self.value = Card.values[self.rank]
		
	# when object is turned to a str, print rank/suit: "3S"
	def __str__(self):
		return self.rank + self.suit

	
class Deck:
	'''
	Creates a deck of 52 cards (using the Card class)
	'''
	
	# Initiate an unshuffled deck, sorted by suit and rank
	def __init__(self):
		self.cardList = [Card(s, r) for s in ["C", "D", "H", "S"]
									for r in list(range(2, 11)) + ["J", "Q", "K", "A"]]
		
	# turn the entire deck into an ordered string useful for printing
	def __str__(self):
		# get the number of cards
		l = len(self.cardList)
		# print the cards, printing a new line after every 13th card
		outStr = ""
		for c in range(l):
			# for regular rows, print two spaces before
			if(c % 13):
				outStr += str(self.cardList[c]).rjust(4)
			# if starting a new row, print a newline
			else:
				outStr += "\n" + str(self.cardList[c]).rjust(4)
		return outStr + "\n"
		
		
	# shuffle the deck
	def shuffle(self):
		random.shuffle(self.cardList)
		
	# deal a card to the player
	def dealOne(self, player):
		# get the card
		card = self.cardList[0]
		# remove the card from the deck
		self.cardList.pop(0)
		# add card to the players hand
		player.hand.append(card)
		player.calcTotal()


class Player:
	'''
	Creates a player who holds no cards, but can recieve some from a Deck object
	'''
	
	# init a hand of nothing with a value of 0
	def __init__(self):
		self.hand = []
		self.handTotal = 0
	   
	# when string is used, show the players list of cards on a single line
	def __str__(self):
		outStr = ""
		for c in self.hand:
			outStr += str(c) + " "
		return outStr
	
	# recalculate the total from the player
	def calcTotal(self):
		self.handTotal = sum([r.value for r in self.hand])
		
	# change the first aces value to a 1 (if it is not one already)
	def changeAce(self):
		for c in self.hand:
			# if card is an ace
			if(c.value == 11):
				# update value and recalculate total
				c.value = 1
				self.calcTotal()
				# quit to ensure not changing multiple aces
				return


#----------------------- Functions -----------------------#


def showHands(opponent, dealer):
	'''
	Reveal the hand of the oppenent and the dealer
	Expected input is oppenent first and dealer second
	'''
	
	print()
	# dealer's hand
	print("Dealer shows %s faceup" % dealer.hand[-1])
	# player's hand
	print("You show %s faceup" % opponent.hand[-1])
	print()
	
	
def hitOrStayOpponent(cardDeck, player):
	'''
	prompt the user if they want to add a card or not
	'''
	print("You hold", player, "for a total of", player.handTotal)
	# prompt user if they want to hit or stay
	choice = int(input("1 (hit) or 2 (stay)? "))
	
	# if 1, add a card to the opponents hand
	if(choice == 1):
		# return True to continue prompting the player if they want to hit or stay
		# if newCard returns False, it's because the player busted
		return newCard(cardDeck, player)
	
	# assume any other number given is a stay
	else:
		# print total
		print("Staying with", player.handTotal)
		# return False to exit the loop
		return False
	
	
def newCard(cardDeck, player):
	'''
	handle either player hitting
	'''
	
	# deal a card
	cardDeck.dealOne(player)
	card = player.hand[-1]
	print()

	# show the card delt
	if(player.name == "dealer"):
		print("Dealer hits:", card)
	else:
		print("Card dealt:", card)

	ifAce(card.rank, player)
	
	# if player has 21, tell the player
	if(player.handTotal == 21):
		# message for dealer
		if(player.name == "dealer"):
			print("21! Dealer wins!")
		# message for opponent
		else:
			print("21! My turn. . .")
		# return False since this players turn is automatically over
		return False
		
	# if handTotal is over 21 check if there is an ace that can be changed to value 1
	elif(player.handTotal > 21):
		
		if(True in [c.value == 11 for c in player.hand]):
			print("Over 21. Switching an ace from 11 points to 1.")
			player.changeAce()

		
	# print new total
	print("New total:", player.handTotal)
	print()
		
	# if players hand is over 21 the game ends
	if(player.handTotal > 21):
		# message for dealer
		if(player.name == "dealer"):
			print("Dealer has " + str(player.handTotal) + ". Dealer busts! You win.")
		# message for opponent
		else:
			print("You have " + str(player.handTotal) + ". You bust! Dealer wins.")
		# return False if the player busts to end their turn
		return False
	
	# return True if 21 or under to prompt the user agian
	return True
				  
			
def ifAce(rank, player):
	'''
	Checks if the newest card is an ace, if it is, print a message
	'''
	
	# if not an ace, return
	if(rank != "A"):
		return
	# message for dealer if card is ace
	if(player.name == "dealer"):
		print("Assuming 11 points for an ace I was dealt for now.")
	# message for opponent if card is ace
	else:
		print("Assuming 11 points for an ace you were dealt for now.")
  
	
def opponentTurn(cardDeck, dealer, opponent):
	'''
	Let the player play until either he/she busts or stays
	The opponent is from here on out refered to as "you"
	'''
	print("You go first.")
	print()
	
	# set names for the opponent and the dealer to be used throughout
	opponent.name = "opponent"
	dealer.name = "dealer"
	
	# initial check if the user has one or two aces
	aces = 0
	for r in opponent.hand:
		if(r.rank == "A"):
			aces += 1
	# if two aces were delt
	if(aces == 2):
		# Let the user know they have an ace being counted as 11 points
		ifAce(opponent.hand[0].rank, opponent)
		# In the case where two aces were delt, change one of the aces to 1
		opponent.changeAce()
	# if one ace was delt
	elif(aces == 1):
		# Let the user know they have an ace being counted as 11 points
		ifAce("A", opponent)
		
	# keep prompting the user to hit or stay until they bust, stay, or get 21 points
	opponent_turn = True
	while opponent_turn:
		opponent_turn = hitOrStayOpponent(cardDeck, opponent)
		
	
def dealerTurn(cardDeck, dealer, opponent):
	'''
	Let the dealer play until either busting or winning
	The dealer is from here on out refered to as "I"
	'''
	
	print()
	
	# if the opponent busted, print that the dealer won and end return
	if(opponent.handTotal > 21):
		return
	
	print("Dealers Turn")
	print("Your hand:", opponent, "for a total of", opponent.handTotal)
	print("Dealer's hand:", dealer, "for a total of", dealer.handTotal)
	
	# initial check if the dealer has one or two aces
	aces = 0
	for r in dealer.hand:
		if(r.rank == "A"):
			aces += 1
	# if two aces were delt
	if(aces == 2):
		# Let the user know they have an ace being counted as 11 points
		print()
		ifAce(dealer.hand[0].rank, dealer)
		# In the case where two aces were delt, change one of the aces to 1
		dealer.changeAce()
	# if one ace was delt
	elif(aces == 1):
		# Let the user know they have an ace being counted as 11 points
		print()
		ifAce("A", dealer)
		
	# keep hitting until total >= opponent's or until busting
	dealer_turn = True
	while dealer_turn:
		if(dealer.handTotal >= opponent.handTotal):
			print("Dealer has %s! Dealer wins!" % dealer.handTotal)
			print()
			return
		dealer_turn = newCard(cardDeck, dealer)

	# insert a new line before ending the program
	print()


#----------------------- Functions -----------------------#


def main():

	print()
	print("Initial deck:")
	cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
	print(cardDeck)                 # print the deck so we can see that you built it correctly
	
	print("Shuffled deck:")
	random.seed(25)                 # leave this in for grading purposes
	cardDeck.shuffle()              # shuffle the deck
	print(cardDeck)                 # print the deck so we can see that your shuffle worked
	
	dealer = Player()               # create the player:  you play for this Player
	opponent = Player()             # create the dealer:  the computer plays for this Player
	
	cardDeck.dealOne(opponent)      # face up
	cardDeck.dealOne(dealer)        # face down (the "hole" card)
	cardDeck.dealOne(opponent)      # face up
	cardDeck.dealOne(dealer)        # face up

	print("Deck after dealing two cards each:")
	print(cardDeck)					# print the deck so we can see that four cards were delt
	
	showHands(opponent,dealer)      # remember not to show face down cards
	
	opponentTurn(cardDeck,dealer,opponent)     # this is where half of the hard stuff is done
	dealerTurn(cardDeck,dealer,opponent)       # this is where the other half of the hard stuff is done
	
	print ("Game over.")
	print ("Final hands:")
	print ("   Dealer:   ", dealer)
	print ("   Opponent: ", opponent)


if __name__ == "__main__":
	main()


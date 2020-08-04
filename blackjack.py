import random


# Build of 100 decks of cards
deck = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*400

# Build of the beggining hand of 2 cards
def hand_creation(deck):
	hand = []
	for i in range(2):
		random.shuffle(deck)
		card = deck.pop()
		if card == 11:
			card = 'J'
		if card == 12:
			card = 'Q'
		if card == 13:
			card = 'K'
		hand.append(card)
	return hand

def play_again():
	player_hand = []
	bank_hand = []
	game()


#Calculation of score of a hand
def total(hand):
	total = 0
	for card in hand:
		if card == 'J' or card == 'Q' or card == 'K':
			total += 10
		elif card > 1 and card <=10:
			total += int(card)
	nb_ace = hand.count(1)
	while nb_ace>1:
		total += 1
		nb_ace-= 1
	if nb_ace == 1 and total + 11 <= 21:
		return total + 11
	elif 1 in hand:
		return total + 1
	else:
		return total
	return total
		
# Take a card
def hit(hand):
	card = deck.pop()
	if card == 11:
		card = 'J'
	if card == 12:
		card = 'Q'
	if card == 13:
		card = 'K'
	hand.append(card)
	return hand

def print_results(dealer_hand, player_hand):
	print("--------------------------------------------------------------------------------")
	print("Bank hand : " + str(dealer_hand) + " --- Score : " + str(total(dealer_hand)))
	print("Your hand : " + str(player_hand) + " --- Score : " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):

	if total(player_hand) == total(dealer_hand) == 21:
		print("It's a draw")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		play_again()
	elif total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print("You've got a blackjack")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		play_again()
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)
		print("Sorry, you lose. The dealer got a blackjack")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		play_again()

def score(dealer_hand, player_hand):

	if total(dealer_hand) > 21:
		print_results(dealer_hand, player_hand)
		print("You win. The dealer bursts")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
	elif total(player_hand) < total(dealer_hand):
		print_results(dealer_hand,player_hand)
		print("You loose")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
	elif total(player_hand) > total(dealer_hand):
		print_results(dealer_hand, player_hand)
		print("You win")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
	elif total(player_hand) == total(dealer_hand):
		print_results(dealer_hand, player_hand)
		print ("It's a draw")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
		print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")

def game():
	dealer_hand = hand_creation(deck)
	player_hand = hand_creation(deck)
	print("Bank hand : [" + str(dealer_hand[0]) + ", ?]")
	print("Your hand : " + str(player_hand) + " --- Score : " + str(total(player_hand)))
	blackjack(dealer_hand, player_hand)
	quit = False
	while not quit:
		choice = input("Do you want to [H]it, [S]tand ot [Q]uit").lower()
		if choice == 'h':
			hit(player_hand)
			print("Bank hand : [" + str(dealer_hand[0]) + ", ?]")
			print("Your hand : " + str(player_hand) + " --- Score : " + str(total(player_hand)))
			if total(player_hand) >21:
				print("Bank hand : " + str(dealer_hand) + " --- Score : " + str(total(dealer_hand)))
				print("Your hand : " + str(player_hand) + " --- Score : " + str(total(player_hand)))
				print("You loose")
				print("--------------------------------------------------------------------------------\n--------------------------------------------------------------------------------")
				play_again()
		elif choice == 's':
			while total(dealer_hand) < 17:
				hit(dealer_hand)
				if total(player_hand) > 21:
					play_again()
			score(dealer_hand, player_hand)
			play_again()
		elif choice == 'q':
			print("Bye!")
			quit = True
			exit()
if __name__ == "__main__":
	game()
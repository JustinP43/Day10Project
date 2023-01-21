"""Program to play simple game of Blackjack"""

from art import logo
import random
import os

deck = {
    "A" : 11,
    "K" : 10,
    "Q" : 10,
    "J" : 10,
    "10" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2
}

def deal_cards(i):
    """Takes integer, for how many cards you'd like to be generated.  Adds those to a list to return to player/dealer."""

    temp_list = []   
    for _ in range(i):
        card = random.randint(0,len(deck)-1)
        
        if card == 12:
            temp_list += ["K"]
        elif card == 11:
            temp_list += ["Q"]
        elif card == 10:
            temp_list += ["J"]
        elif card == 0:
            temp_list += ["A"]
        else:
            temp_list += [str(card + 1)]
    return temp_list


def calculate_score(list):
    """ 
        - Takes a string card from the player/dealer's list of cards and converts it to a score.
        - Converts Ace's to 1 or 11 depending on how many are in the hand.
        - Determines if the deal was a Blackjack, which will return -1 and end the game if a player/dealer has a Blackjack.
    """

    count = 0
    score = 0
    for key in list:
        if key == "A":
            count += 1
        score += deck[key]
    
    if count > 1:
        score = score - ((count -1) * 10)
    
    if len(list) == 2 and score == 21:
        return -1
    return score

def clear():
    """Quick function to clear the terminal."""
    os.system('cls')
    
     
def blackjack():
    """Generates players cards and dealers cards to play blackjack."""
    gameover = False
    
    player_cards = []
    dealer_cards = []
    
    player_score = 0
    dealer_score = 0

    while not gameover:
        print(logo)
        player_cards = deal_cards(2)
        dealer_cards = deal_cards(2)

        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        if player_score == -1 and dealer_score == -1:
            print(f"Your cards: {player_cards}  Score: 21")
            print(f"Dealer cards: {dealer_cards}  Score: 21")
            print("You both have a Blackjack, this game is a Draw.")
            gameover = True
        elif player_score == -1 and dealer_score != -1:
            print(f"Your cards: {player_cards}  Score: 21")
            print(f"Dealer cards: {dealer_cards}  Score: {dealer_score}")
            print("You have a Blackjack, you win!")
            gameover = True
        elif dealer_score == -1 and player_score != -1:
            print(f"Your cards: {player_cards}  Score: {player_score}")
            print(f"Dealer cards: {dealer_cards}  Score: 21")
            print("Dealer has a Blackjack, you lose.")
            gameover = True
        else:
            player_turn = True
            while player_turn:
                clear()
                print(logo)
                player_score = calculate_score(player_cards)
                print(f"Your cards: {player_cards}  Score: {player_score}")
                print(f"Dealer top card: {dealer_cards[0]}")
                

                if player_score <= 21:
                    user_input = input(f"Your score is: {player_score}.  Type 'y' to get another card, type 'n' to pass:  ").lower()
                    if user_input == "y":
                        player_cards.extend(deal_cards(1)) 
                    else:
                        player_turn = False
                else:
                    player_turn = False
            
            if player_score <= 21:
                while dealer_score < 16:
                    dealer_cards.extend(deal_cards(1))
                    dealer_score = calculate_score(dealer_cards)
                gameover = True
            else:
                gameover = True

        
        clear()
        print(logo)
        print(f"Your cards: {player_cards}  Score: {player_score}")
        print(f"Dealer's cards: {dealer_cards}  Score: {dealer_score}")
        
        if player_score > 21:
            print("You are over 21, bust!  You lose.")
        elif dealer_score > 21:
            print("Dealer is over 21, bust!  You win!")
        elif dealer_score == player_score:
            print("You have the same value, draw.")
        elif player_score > dealer_score:
            print("You win!")
        else:
            print("You lose.")


        keep_playing = input("Would you like to play another round of Blackjack?  'y' to continue, 'n' to quit: ").lower()
        if keep_playing == 'y':
            blackjack()


blackjack()
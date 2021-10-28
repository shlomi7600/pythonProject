import random
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from game_cards.Player import Player
class CardGame:
    def __init__(self,name1,name2,number_of_cards=26):
        self.deck_of_cards=DeckOfCards()
        self.player1=Player(name1,number_of_cards)
        self.player2=Player(name2,number_of_cards)
        self.new_game()




    def new_game(self):
        self.deck_of_cards.cards_shuff()
        self.player1.set_hand(self.deck_of_cards)
        self.player2.set_hand(self.deck_of_cards)


    # method that returns the winning player
    def get_winner(self):
        if len(self.player1.dec_of_cards_player)>len(self.player2.dec_of_cards_player):
            return self.player1.name

        elif len(self.player2.dec_of_cards_player)>len(self.player1.dec_of_cards_player):
            return self.player2.name

        else:
            return None

    def __repr__(self):

        return f"first player name:{self.player1.name},first player dec of cards:{self.player1.dec_of_cards_player}\n second player name:{self.player2.name},second player dec of cards:{self.player2.dec_of_cards_player}"


name_player1 = input("enter the name of the first player")
name_player2 = input("enter the name of the second player")
cardGame1 = CardGame(name_player1, name_player2, 26)
print(cardGame1)
for i in range(10):
    card1 = cardGame1.player1.get_card()
    card2 = cardGame1.player2.get_card()
    print(f"player1 card:{card1}\nplayer2 card:{card2}")

    if Card.__gt__(card1, card2):
        cardGame1.player1.add_card(card1)
        cardGame1.player1.add_card(card2)
        print(cardGame1.player1.name)

    else:
        cardGame1.player2.add_card(card1)
        cardGame1.player2.add_card(card2)
        print(cardGame1.player2.name)

if cardGame1.get_winner()==None:
    print("there is no winner in this match, it's a draw")
else:
    print(f"the winner is: {cardGame1.get_winner()}")



import random
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
class Player:
    def __init__(self,name,number_of_cards=26):

        self.name=name
        self.number_of_cards=number_of_cards
        self.dec_of_cards_player=[]
        if (self.number_of_cards > 26 or self.number_of_cards < 10):
            self.number_of_cards = 26
            
# method that receives a DeckDfCards and distributes cards to a player
    def set_hand(self,deck_of_cards1):
            for i in range(self.number_of_cards):
                self.dec_of_cards_player.append(deck_of_cards1.deal_one())


    # method that pulls a card from the list_cards of the player and returns it
    def get_card(self):
        get_card = self.dec_of_cards_player.pop(self.dec_of_cards_player.index(random.choice(self.dec_of_cards_player)))
        return get_card


    # method that getting a card and adding in to the dec_of_cards_player
    def add_card(self,card1):
        self.dec_of_cards_player.append(card1)

import random
from game_cards.Card import Card
class DeckOfCards:
    def __init__(self):
        self.list_cards=[]
        for suit in range (4):
            for value in range(13):
                card1=Card(suit+1,value+1)
                self.list_cards.append(card1)

# method that shuffles the cards
    def cards_shuff(self):
        random.shuffle(self.list_cards)


    # method that pulls a card from the list_cards and returns it
    def deal_one(self):
        removed_card=self.list_cards.pop(self.list_cards.index(random.choice(self.list_cards)))
        return removed_card





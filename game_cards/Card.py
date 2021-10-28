class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value=value


#method that decide which card wins in this round
    def __gt__(self, other):

        if (self.value>other.value) or (self.value==1 and other.value!=1):
            return True


        elif self.value==other.value:
            if self.suit>other.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return f"suit:{self.suit},value:{self.value}"
import random
from lab3.deck_of_cards.carte import Carte


class Pachet:

    def __init__(self):
        culori = ['rosu', 'negru', 'romb', 'trefla']
        valori = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
        self.carti = [Carte(val,cul) for val in valori for cul in culori]

    def __str__(self):
        s = ''
        for elem in self.carti:
            s += elem.__str__() +'\n'
        return s

    def shuffle(self):
        random.shuffle(self.carti)

    def get_card(self):
        return self.carti.pop()

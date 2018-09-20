# coding = utf-8

from interface.human import Human
from Deck import Deck

"""
==============
Player Class
==============
"""


class Player(Human):

    def __init__(self):
        super().__init__()

    def get_name(self):
        return self._name

    def greet(self):
        print('You: My name is ...', end="")
        self._name = str(input())
        return self._name

    def show_hand(self):
        print(self._name + '\'s hand is', end=' ')

        for card in self._hand:
            print(card.open(), end=' ')

        self.__show_score()

    def __show_score(self):
        print('(' + str(self._score) + ')')

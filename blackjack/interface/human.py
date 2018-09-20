# coding=utf8
from Deck import Deck
from abc import abstractmethod

"""
==========
human Class(interface)
==========
"""


class Human(object):

    def __init__(self):
        self._name = ''
        self._score = 0
        self._hand = list()

    def count_score(self):
        self._score = 0
        for card in self._hand:
            if card.get_number() > 10:
                self._score += 10
                return

            if card.get_number() == 1:
                if self._score > 10:
                    self._score += 1
                    return
                else:
                    self._score += 11
                    return

            self._score += card.get_number()

    @abstractmethod
    def greet(self):
        pass

    def hit(self, deck: Deck) -> bool:
        print(self._name + ": hit")
        self._hand.append(deck.pop())

        self.count_score()

        if self._score > 21:
            print('Busted!')
            return True, False

        if self._score == 21:
            print('BlackJack!')
            return False, True
        else:
            return False, False

    def stand(self):
        print(self._name + ' : stand')

    def first_draw(self, deck: Deck):
        self.hit(deck)
        self.hit(deck)

    def get_score(self) -> int:
        return self._score

    def get_name(self) -> str:
        return self._name

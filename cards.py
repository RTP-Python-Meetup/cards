import random

class Card(object):

    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit

    @property
    def rank(self):
        return self.__rank

    @property
    def position(self):
        suit_value = {
            'C': 1,
            'D': 2,
            'S': 3,
            'H': 4
        }[self.suit]
        return suit_value * 13 + self.rank

    def __str__(self):
        return "{} {}".format(self.suit, self.rank)

    def __repr__(self):
        return str(self)




class CardContainer(object):

    def __init__(self):
        self.__cards = []

    def add(self, card):
        self.__cards.append(card)

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards):
        self.__cards = sorted(cards, key=lambda card: card.position)

    @property
    def cards_by_rank(self):
        return sorted(self.__cards, key=lambda card: card.rank)

    @property
    def cards_by_suit(self):
        return sorted(self.__cards, key=lambda card: card.suit)

    def __repr__(self):
        return ', '.join((str(card) for card in self.cards))


class Deck(CardContainer):

    def __init__(self):
        self.cards = list(Card(suit, rank) for suit in 'CDSH' for rank in range(1,14))

    def deal_random_card(self):
        return self.cards.pop(random.randint(0, len(self.cards)))


my_deck = Deck()

p1_hand = CardContainer()
p1_playable = CardContainer()
p2_hand = CardContainer()
p2_playable = CardContainer()

card = my_deck.deal_random_card()
p1_hand.add(card)
p1_playable.add(card)
card = my_deck.deal_random_card()
p1_hand.add(card)
p1_playable.add(card)

card = my_deck.deal_random_card()
p2_hand.add(card)
p2_playable.add(card)
card = my_deck.deal_random_card()
p2_hand.add(card)
p2_playable.add(card)

community = CardContainer()

card = my_deck.deal_random_card()
community.add(card)
p1_playable.add(card)
p2_playable.add(card)
card = my_deck.deal_random_card()
community.add(card)
p1_playable.add(card)
p2_playable.add(card)
card = my_deck.deal_random_card()
community.add(card)
p1_playable.add(card)
p2_playable.add(card)

print('start')
print(p1_hand)
print(p2_hand)
print('flop')
print(community)
print(p1_playable)
print(p1_playable.cards_by_rank)
print(p1_playable.cards_by_suit)
print(p2_playable)
print(p2_playable.cards_by_rank)
print(p2_playable.cards_by_suit)

print('turn')
card = my_deck.deal_random_card()
community.add(card)
p1_playable.add(card)
p2_playable.add(card)

print(p1_playable)
print(p1_playable.cards_by_rank)
print(p1_playable.cards_by_suit)
print(p2_playable)
print(p2_playable.cards_by_rank)
print(p2_playable.cards_by_suit)

print('river')
card = my_deck.deal_random_card()
community.add(card)
p1_playable.add(card)
p2_playable.add(card)

print('p1_playable:', p1_playable)
print(p1_playable.cards_by_rank)
print(p1_playable.cards_by_suit)
print('p2_playable:', p2_playable)
print(p2_playable.cards_by_rank)
print(p2_playable.cards_by_suit)

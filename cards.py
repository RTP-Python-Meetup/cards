import random
import json

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


class CardContainer(object):

    def __init__(self):
        self.__cards = []

    def add(self, card):
        self.__cards.append(card)

    def shuffle(self):
        shuffled = []
        while self.cards:
            if len(self.cards) > 1:
                index = random.randint(0, len(self.cards) - 1)
            else:
                index = 0
            shuffled.append(self.cards.pop(index))
        self.__cards = shuffled

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

    def to_json(self):
        return json.dumps([str(card) for card in self.cards])

    def to_list(self):
        return list(str(card) for card in self.cards)


class Deck(CardContainer):

    def __init__(self, shuffle=True):
        self.cards = list(Card(suit, rank) for suit in 'CDSH' for rank in range(1,14))
        if shuffle:
            self.shuffle()

    def deal_random_card(self):
        if len(self.cards) > 1:
            index = random.randint(0, len(self.cards) - 1)
        else:
            index = 0
        return self.cards.pop(index)


class Player(object):

    def __init__(self):
        self.hand = CardContainer()
        self.community = None

    @property
    def playable_cards(self):
        return self.hand.cards + self.community.cards


def holdem(player_count=2):
    # Create community and list for containing players
    deck = Deck()
    community = CardContainer()
    players = []
    print(deck, end=": ")
    print(deck.to_list())


    # Create players
    for i in range(0, player_count):
        players.append(Player())
        players[-1].community = community

    # Deal
    for player in players:
        player.hand.add(deck.cards.pop())
        player.hand.add(deck.cards.pop())

    # Show players hands:
    print('Pre-flop')
    for player in players:
        print(player, end=": ")
        print(list(str(card) for card in player.playable_cards))
    print(community, end=": ")
    print(list(str(card) for card in community.cards))

    # Flop
    community.add(deck.cards.pop())
    community.add(deck.cards.pop())
    community.add(deck.cards.pop())

    # Show players hands:
    print('Flop')
    for player in players:
        print(player, end=": ")
        print(list(str(card) for card in player.playable_cards))
    print(community, end=": ")
    print(list(str(card) for card in community.cards))

    # Turn
    community.add(deck.cards.pop())

    # Show players hands:
    print('Turn')
    for player in players:
        print(player, end=": ")
        print(list(str(card) for card in player.playable_cards))
    print(community, end=": ")
    print(list(str(card) for card in community.cards))

    # River
    community.add(deck.cards.pop())

    # Show players hands:
    print('River')
    for player in players:
        print(player, end=": ")
        print(list(str(card) for card in player.playable_cards))
    print(community, end=": ")
    print(list(str(card) for card in community.cards))


holdem()

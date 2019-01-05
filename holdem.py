from cards import *

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

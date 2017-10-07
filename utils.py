def generate_test_data():

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    colors = ['spades', 'diamonds', 'hearths', 'clubs']

    cards = []

    for rank in ranks:
        for color in colors:
            card = {}
            card['suit'] = color
            card['rank'] = rank
            cards.append(card)

    hands = []

    for card_1 in cards:
        for card_2 in cards:
            if(card_1 == card_2):
                continue
            hand = [[]]
            hand[0] = card_1, card_2
            hands.append(hand)

    return hands


def getHandPower(hand):
    # [[{u'suit': u'spades', u'rank': u'8'}, {u'suit': u'diamonds', u'rank': u'Q'}]]
    rank = 0
    card_number = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 14,
        'A': 15
    }

    for card in hand[0]:
        rank += card_number[card['rank']]

    card_1 = hand[0][0]
    card_2 = hand[0][1]
    if(card_1['suit'] == card_2['suit']):
        rank *= 2
    if(card_1['rank'] == card_2['rank']):
        rank *= 3
    return rank


def test_hand_power():
    hands = generate_test_data()
    for hand in hands:
        print(hand)
        print(getHandPower(hand))

# test_hand_power()
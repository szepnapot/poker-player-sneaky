def generate_test_data():

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    colors = ['spades', 'diamonds']

    cards = []

    for rank in ranks:
        for color in colors:
            card = {}
            card['suit'] = color
            card['rank'] = rank
            cards.append(card)

    hands = []

    for i in range(len(cards)):
        card_1 = cards[i]
        for card_2 in cards[i:]:
            if(card_1 == card_2):
                continue
            hand = [[]]
            hand[0] = card_1, card_2
            hands.append(hand)

    return hands

def getHandPower(hand):
    # [[{u'suit': u'spades', u'rank': u'8'}, {u'suit': u'diamonds', u'rank': u'Q'}]]

    try:
        card_1 = hand[0][0]
        card_2 = hand[0][1]
    except:
        return 0

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
        'K': 13,
        'A': 15
    }

    for card in hand[0]:
        rank += card_number[card['rank']]



    if(card_1['suit'] == card_2['suit']):
        rank *= 1.115
    if(card_1['rank'] == card_2['rank']):
        rank += 10
    return rank

def convert_hand_two_short_form(hand):
    handstring = ''
    handstring += hand[0][0]['suit'][0]
    handstring += hand[0][0]['rank']
    handstring += ', '
    handstring += hand[0][1]['suit'][0]
    handstring += hand[0][1]['rank']
    return handstring

def test_hand_power():
    hands = generate_test_data()
    ranked_hands = []
    for hand in hands:
        power = getHandPower(hand)
        ranked_hands.append([power, convert_hand_two_short_form(hand)])

    ranked_hands.sort(key=lambda x: x[0])
    for hand in ranked_hands:
        print(hand)

# test_hand_power()
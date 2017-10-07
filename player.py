from utils import getHandPower

class Player:
    VERSION = "Default Python folding player"

    def get_hand(self, game_state):
        player = [elem['hole_cards'] for elem in game_state['players'] if elem['version'] == self.VERSION]
        return player

    def get_community_card(self, game_state):
        return game_state["community_cards"]

    def betRequest(self, game_state):
        print(game_state)
        hand = self.get_hand(game_state)
        community_cards = self.get_community_card(game_state)
        hand_power = getHandPower(hand)
        if hand_power >= 20:
            bet = 9999
        else:
            bet = 0
        print("#######################################")
        print("                 OUR HAND                       ")
        print(hand)
        print("#######################################")
        print("#######################################")
        print("                 COMMUNITY CARDS                ")
        print(community_cards)
        print("#######################################")
        print("#######################################")
        print("                 HAND POWER                      ")
        print(hand_power)
        print("#######################################")
        print("#######################################")
        print("                 OUR BET               ")
        print(bet)
        return bet

    def showdown(self, game_state):
        print(game_state['players'])
        # players_with_cards = [(elem['hole_cards'], elem['name']) for elem in game_state['players']]
        # print(players_with_cards)


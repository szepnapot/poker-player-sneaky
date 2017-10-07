import pprint
from utils import getHandPower

class Player:
    VERSION = "Default Python folding player"

    def get_hand(self, game_state):
        player = [elem['hole_cards'] for elem in game_state['players'] if elem['version'] == self.VERSION]
        return player

    def bets_per_round(self, game_state):
        bets = [(elem['player'], elem['bet']) for elem in game_state['players']]
        return bets

    def get_community_card(self, game_state):
        return game_state["community_cards"]

    def betRequest(self, game_state):
        print("#######################################")
        print("#######################################")
        print("                 GAME STATE                       ")
        pprint.pprint(game_state, width=1)
        print("#######################################")
        print("#######################################")
        print("                 PLAYER BETS                       ")
        bets = self.bets_per_round(game_state)
        pprint.pprint(bets, width=1)
        print("#######################################")
        print("#######################################")
        hand = self.get_hand(game_state)
        community_cards = self.get_community_card(game_state)
        hand_power = getHandPower(hand)

        if hand_power >= 29:
            bet = 9999
        elif hand_power >= 21:
            bet = 300
        elif hand_power >= 19:
            bet = 200
        elif hand_power > 10:
            bet = 0
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

    def get_winner_stats(self, game_state):
        winner = [elem for elem in game_state['players'] if elem['status'] == 'active'][0]
        winner_hand = [winner.get('hole_cards', {})]
        winner_hand_power = getHandPower(winner_hand)
        return {'winner': winner['name'],
                'hand': winner_hand,
                'hand_power': winner_hand_power}

    def showdown(self, game_state):
        winner_stats = self.get_winner_stats(game_state)
        print("#######################################")
        print("#######################################")
        print("                 PLAYERS ON SHOWDOWN            ")
        pprint.pprint(game_state['players'])
        print("#######################################")
        print("#######################################")
        print("            COMMUNITY CARDS IN SHOWDOWN         ")
        print(self.get_community_card(game_state))
        print("#######################################")
        print("#######################################")
        print("                WINNER STATS                          ")
        pprint.pprint(winner_stats, width=1)
        print("#######################################")
        print("#######################################")



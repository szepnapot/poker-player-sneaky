import pprint
from utils import getHandPower

class Player:
    VERSION = "Default Python folding player"

    def get_hand(self, game_state):
        player = [elem['hole_cards'] for elem in game_state['players'] if elem['version'] == self.VERSION]
        return player

    def bets_per_round(self, game_state):
        bets = [(elem['name'], elem['bet']) for elem in game_state['players']]
        return bets

    def get_community_card(self, game_state):
        return game_state["community_cards"]

    def hold(self, game_state, intended_bet):
        bets = self.bets_per_round(game_state)
        maxbet = intended_bet
        for bet in bets:
            if bet[1] > maxbet:
                maxbet = bet[1]

        return maxbet

    def get_active_players(self, game_state):
        active_players = [1 for elem in game_state['players'] if elem['status'] == 'active']
        return sum(active_players)


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

        if hand_power >= 35:
            bet = self.hold(self, game_state, 99999)
        elif hand_power >= 21:
            bet = self.hold(self, game_state, 300)
        elif hand_power >= 19:
            bet = self.hold(self, game_state, 200)
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
        winner = [{'winner': elem} for elem in game_state['players'] if elem['status'] == 'active']
        print(winner)
        # try:
        #     winner_hand = winner[0]['hole_cards']
        #     winner_hand_power = getHandPower(winner_hand)
        # except:
        #     winner_hand = 'COULD NOT FOUND'
        #     winner_hand_power = 'COULD NOT FOUND'
        # return {'winner': winner[0]['name'],
        #         'hand': winner_hand,
        #         'hand_power': winner_hand_power}

    def showdown(self, game_state):
        print(self.get_winner_stats(game_state))
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
        # pprint.pprint(winner_stats, width=1)
        # print("#######################################")
        # print("#######################################")



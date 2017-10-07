import pprint
from utils import getHandPower
import requests

ALL_IN = 99999
MAX_SACRIFICE_RATE = 0.7

class Player:
    VERSION = "Default Python folding player"

    def get_hand(self, game_state):
        player = [elem['hole_cards'] for elem in game_state['players'] if elem['version'] == self.VERSION]
        return player

    def get_own_stack(self, game_state):
        stack = [elem['stack'] for elem in game_state['players'] if elem['version'] == self.VERSION]
        return stack

    def bets_per_round(self, game_state):
        bets = [(elem['name'], elem['bet']) for elem in game_state['players']]
        return bets

    def get_community_card(self, game_state):
        return game_state["community_cards"]

    def hold(self, game_state, intended_bet, ownStack):
        bets = self.bets_per_round(game_state)
        maxbet = intended_bet

        for bet in bets:
            if bet[1] > maxbet:
                maxbet = bet[1]


        return maxbet

    def get_active_players(self, game_state):
        active_players = [1 for elem in game_state['players'] if elem['status'] == 'active']
        return sum(active_players)

    def get_past_winners(self):
        # MAY TAKE A LOT OF TIME !!
        # EXTERNAL SERVICE
        r = requests.get('https://lean-poker-db.herokuapp.com/get_winners')
        return r.json()

    def only_high_cards(self, game_state):
        try:
            isOnlyHigh = False;
            hand = self.get_hand(game_state)
            card_1 = hand[0][0]
            card_2 = hand[0][1]
            if (card_1['rank'] in 'JQKA' and card_2['rank'] in 'JQKA'):
                isOnlyHigh = True
            return isOnlyHigh
        except:
            return False


    def betRequest(self, game_state):
        try:
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

            ownStack = self.get_own_stack(game_state)

            if hand_power >= 35:
                bet = self.hold(game_state, ALL_IN, ownStack)
            elif hand_power >= 21:
                if (self.only_high_cards(game_state)):
                    bet = self.hold(game_state, 300, ownStack)
                else:
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

        except:
            return 90000

    def get_winner_stats(self, game_state):
        winner = [{'winner': elem} for elem in game_state['players'] if elem['status'] == 'active']
        try:
            winner_hand = winner[0]['winner']['hole_cards']
            winner_hand_power = getHandPower([winner_hand])
        except:
            winner_hand = 'HAND NOT SHOWN'
            winner_hand_power = 'HAND NOT SHOWN'
        return {'winner': winner[0]['winner']['name'],
                'hand': winner_hand,
                'hand_power': winner_hand_power}

    def showdown(self, game_state):
        print("#######################################")
        print("#######################################")
        print("        SHOWDOWN GAME STATE             ")
        pprint.pprint(game_state, width=1)
        print("#######################################")
        print("#######################################")
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
        print(self.get_winner_stats(game_state))
        print("#######################################")
        print("#######################################")
        try:
            requests.post("https://lean-poker-db.herokuapp.com/add", json=self.get_winner_stats(game_state), timeout=0.001)
        except:
            pass



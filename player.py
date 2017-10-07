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

            if hand_power >= 30:
                bet = 9999
                #bet = self.hold(game_state, 99999)
            elif hand_power >= 20:
                #if (self.only_high_cards(game_state)):
                #    bet = self.hold(game_state, 300)
                #else:
                bet = 600
            elif hand_power >= 15:
                bet = 150
            elif hand_power > 10:
                bet = 30
            else:
                bet = 10


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

        return 999999

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



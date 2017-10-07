import pprint
from utils import getHandPower


ALL_IN = 9999999
RANKS = ["", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

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


    def get_active_players(self, game_state):
        active_players = [1 for elem in game_state['players'] if elem['status'] == 'active']
        return sum(active_players)

    def has_pairs_over(self, game_state, over_card):
        hand = self.get_hand(game_state)
        return hand[0] == hand[1] and RANKS.index(hand[0]) > RANKS.index(over_card)

    def high_cards_only(self, game_state):
        hand = self.get_hand(game_state)
        return RANKS.index(hand[0]) > RANKS.index('10') and RANKS.index(hand[1]) > RANKS.index('10')

    def betRequest(self, game_state):

        if self.has_pairs_over(game_state, '10'):
            return ALL_IN

        if self.get_active_players(game_state) < 3 and self.has_pairs_over(game_state, '10'):
            return ALL_IN

        if self.high_cards_only(game_state):
            return ALL_IN

        return 0





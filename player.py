
class Player:
    VERSION = "Default Python folding player"

    def get_player(self, game_state):
        player = [elem['hole_cards'] for elem in game_state['players'] if elem['version'] == self.VERSION]
        return player

    def betRequest(self, game_state):
        print("###############################################")
        print("###############################################")
        print("                 OUR HAND                       ")
        print(self.get_player(game_state))
        print("###############################################")
        print("###############################################")
        print("                 COMMUNITY CARDS                ")
        print("Community cards: {}".format(game_state["community_cards"]))
        print("###############################################")
        print("###############################################")
        return 0

    def showdown(self, game_state):
        pass


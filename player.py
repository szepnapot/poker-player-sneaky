
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print("Community cards: {}".format(game_state["community_cards"]))
        return 9999

    def showdown(self, game_state):
        pass


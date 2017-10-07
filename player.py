
class Player:
    VERSION = "CsillámPóniEvőKígyóBűvölőMedveEmberek"

    def get_hand(self, game_state):
        player = [elem['hole_cards'] for elem in game_state['players'] if elem['version'] == self.VERSION]
        return player


    def get_community_card(self, game_state):
        return game_state["community_cards"]

    def printer(self, hand, community):
        print("#######################################")
        print("                 OUR HAND                       ")
        print(hand)
        print("#######################################")
        print("#######################################")
        print("                 COMMUNITY CARDS                ")
        print(community)
        print("#######################################")
        print("#######################################")

    def betRequest(self, game_state):
        hand = self.get_hand(game_state)
        community_cards = self.get_community_card(game_state)
        self.printer(hand, community_cards)
        return 9999

    def showdown(self, game_state):

        pass


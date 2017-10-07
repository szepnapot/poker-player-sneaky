from player import Player
from test_datas import test_game_state

pl = Player()

assert pl.betRequest(test_game_state) == 9999



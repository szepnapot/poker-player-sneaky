from player import Player
from test_datas import test_game_state, test_showdown

pl = Player()

assert pl.betRequest(test_game_state) == 99999


print(pl.showdown(test_showdown))
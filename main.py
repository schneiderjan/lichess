#%% Imports
import datetime as DT

import yaml

from src.lichess_client import LichessClient
from src.utils import is_user_white
from src.visualization import plot_top_3_first_moves


#%% Init lichess client.
with open("token.yaml", "r") as f:
    data = yaml.safe_load(f)
    token = data["token"]

client = LichessClient(token)

#%% collect data and find first moves.
user_name = "j2020"
games_df = client.load_as_dataframe(user_name=user_name, start=DT.datetime(2018, 12, 8), end=DT.datetime(2023, 10, 3))

first_move_white = []
first_move_black = []
for idx, row, in games_df.iterrows():
    # moves is a string space seperated. First move is white, second move is black.
    moves = row.moves.split(" ")
    if is_user_white(players = row.players, user_name=user_name):
        first_move_white.append(moves[0])
    else:
        first_move_black.append(moves[1])



#%% Visualize top 3 moves for each color
plot_top_3_first_moves(white_moves=first_move_white, black_moves=first_move_black)
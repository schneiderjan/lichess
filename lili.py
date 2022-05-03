import berserk
from datetime import datetime
import json

# auth
with open("token.json", "r") as f:
    token = json.load(f)["token"]
session = berserk.TokenSession(token)
client = berserk.Client(session)

start = berserk.utils.to_millis(datetime(2018, 12, 8))

end = berserk.utils.to_millis(datetime(2018, 12, 9))

games = client.games.export_by_player('LeelaChess', since=start, until=end, max=300)
print(len(list(games)))
print("yay.")
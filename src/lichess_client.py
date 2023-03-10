import datetime

import berserk
import pandas as pd


class LichessClient:
    def __init__(self, token: str):
        """Initializes a new LichessClient

        Args:
            token (str): Your lichess auth token. See https://lichess.org/account/oauth/token for more info.
        """        
        session = berserk.TokenSession(token)
        self.client = berserk.Client(session)

    def _load_records(self, start: datetime, end: datetime, user_name: str):
        game_data = self.client.games.export_by_player(
            user_name, since=start, until=end, max=500
        )
        # exclude other game modes than standard
        games = [game for game in game_data if game["variant"] == "standard"]
        return games

    def load_as_dataframe(self, start: datetime, end: datetime, user_name: str = "j2020") -> pd.DataFrame:
        """Load data from lichess standard rapid games by user name in specified time frame.

        Args:
            start (datetime): Start date to collect from.
            end (datetime): End date to collect until.
            user_name (str, optional): Your lichess user name. Defaults to "j2020".


        Returns:
            pd.DataFrame: DataFrame containing my lichess games.
        """
        records = self._load_records(start, end, user_name)
        return pd.DataFrame.from_records(records)
 

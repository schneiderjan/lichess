def is_user_white(players: dict, user_name: str) -> bool:
    """Determine whether the user played the white pieces in the game.

    Args:
        players (dict): Player info of a game.
        user_name (str): User name of player.

    Returns:
        bool: True if user played the white pieces, False otherwise.
    """    
    white = players.get("white", None)
    return white and white["user"]["name"] == user_name
    

import matplotlib.pyplot as plt
from typing import List
import numpy as np

def _rank_moves(moves: List[str]) -> set:
    # rank top moves.
    ranks = {}
    for element in set(moves):
        ranks[element] = moves.count(element)

    top_3 = {key: val for key, val in sorted(ranks.items(), key=lambda item: item[1], reverse=True)[:3]}
    return top_3

def plot_top_3_first_moves(white_moves: List[str], black_moves: List[str], filepath: str = "top_3_viz.png"):
    """Plots the top 3 first moves of each color and stores to disk.

    Args:
        white_moves (List[str]): Collection of first white move in chess annotation.
        black_moves (List[str]): Collection of first black move in chess annotation.
        filepath (str): Path on disk to store figure. Defaults to `top_3_viz.png`.
    """ 
    top_3_white = _rank_moves(white_moves)
    # # fill dummy data because I seem to be playing only 
    # top_3_white["O-O"] = 0
    top_3_black = _rank_moves(black_moves)
    
    # Define the data for white bars
    white_values = list(top_3_white.values())
    white_labels = list(top_3_white.keys())

    # Define the data for black bars
    black_values = list(top_3_black.values())
    black_labels = list(top_3_black.keys())

    bar_width = 0.35
    r1 = np.arange(len(white_values))
    r2 = [x + bar_width for x in r1]

    # Create white bars
    plt.bar(r1, white_values, color='white', width=bar_width, edgecolor='black', label='White')

    # Create black bars
    plt.bar(r2, black_values, color='black', width=bar_width, edgecolor='black', label='Black')

    # Add xticks on the middle of the group bars
    plt.xlabel('Color')
    plt.xticks([r + bar_width / 2 for r in range(len(white_values))], white_labels)

    # Add ylabel
    plt.ylabel('Count')

    # Add chart title
    plt.title('Top 3 moves for white and black pieces')

    # Add legend
    plt.legend()

    # Store to disk
    plt.savefig(filepath)


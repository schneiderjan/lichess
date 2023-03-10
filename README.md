# Lichess Top 3 Moves Plotter

This tool allows you to plot the top 3 moves of a player on Lichess, a popular online chess platform. The plots are generated using the data from the player's game history on Lichess.

## Installation


Clone this repository to your local machine using the following command:

``` git
git clone https://github.com/schneiderjan/lichess.git
```

Then, navigate to the directory where you cloned the repository and install the required Python packages by running the following command:
```
pip install -r requirements.txt
```

## Usage

To use the tool, you will need to obtain an API token from Lichess. You can do this by following these steps:

1. Log in to your Lichess account.
2. Click on your username in the top right corner and select "Account".
3. Click on the "API Access Token" tab.
4. Click on the "Create a new API token" button and follow the instructions to create a new token.
5. Copy a yaml file called `token.yaml`.

The file must contain this:
``` yaml
token: your-api-token
```

Once you have obtained your API token, run the `main.py` to generate a plot of the top 3 moves of a player:

Replace `user_name` with the Lichess username of the player you want to plot The tool will generate a plot of the top 3 moves of the player and save it to a file named `top_3_moves_viz.png` in the current directory.

## License

This tool is released under the Apache License. See LICENSE for more information.



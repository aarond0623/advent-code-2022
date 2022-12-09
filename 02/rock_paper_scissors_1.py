import sys


def score_rps(player1, player2):
    """
    Scores a round of rock paper scissors using the following rules:

    Each player scores according to the tool they choose, regardless of
    whether they win or lose: 1 point for Rock, 2 points for Paper, and 3
    points for Scissors. In addition, each player scores points according to
    the outcome of the round: 0 points for a loss, 3 points for a draw, and 6
    points for a win.

    Args:
        player1: A string representing player 1's choice, one of 'rock',
        'paper', or 'scissors'.
        player2: A string representing player 2's choice, one of 'rock',
        'paper', or 'scissors'.

    Returns:
        A tuple representing the points for player 1 and player 2.
    """
    points = {
        'win': 6,
        'draw': 3,
        'loss': 0,
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }
    tools = ['rock', 'paper', 'scissors']
    player1_score = 0
    player2_score = 0

    # Points for tool use:
    player1_score += points[player1]
    player2_score += points[player2]

    if player1 == tools[(tools.index(player2) + 1) % 3]:  # Player 1 wins
        player1_score += points['win']
        player2_score += points['loss']
    elif player2 == tools[(tools.index(player1) + 1) % 3]:  # Player 2 wins
        player2_score += points['win']
        player1_score += points['loss']
    else:  # There was a draw
        player1_score += points['draw']
        player2_score += points['draw']

    return (player1_score, player2_score)


def translate_rps(game_string):
    """
    Translates a string into a rock paper scissors game using the following
    key:

    Player 1: A = Rock, B = Paper, C = Scissors
    Player 2: X = Rock, Y = Paper, Z = Scissors

    Args:
        game_string: A three-character string of two letters representing the
        two players' choices.

    Returns:
        A two-item tuple of 'rock', 'paper', or 'scissors' representing the
        two players' choices.
    """
    choice_dict = {
        'A': 'rock',
        'X': 'rock',
        'B': 'paper',
        'Y': 'paper',
        'C': 'scissors',
        'Z': 'scissors'
    }
    choices = game_string.split()
    player1 = choice_dict[choices[0]]
    player2 = choice_dict[choices[1]]
    return (player1, player2)


if __name__ == '__main__':
    total = 0
    for line in sys.stdin:
        total += score_rps(*translate_rps(line))[1]
    print(total)

import sys
from rock_paper_scissors_1 import score_rps


def translate_rps(game_string):
    """
    Translates a string into a rock paper scissors game using the following
    key:

    Player 1: A = Rock, B = Paper, C = Scissors
    Outcome for Player 2: X = loss, Y = draw, Z = win

    Args:
        game_string: A three-character string of two letters representing
        player 1's choice and player 2's outcome.

    Returns:
        A two-item tuple of 'rock', 'paper', or 'scissors' representing the
        two players' choices for the round.
    """
    choice_dict = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': -1,
        'Y': 0,
        'Z': 1
    }
    tools = ['rock', 'paper', 'scissors']
    choices = game_string.split()
    player1 = choice_dict[choices[0]]
    player2 = choice_dict[choices[1]]
    player2 = tools[(tools.index(player1) + player2) % 3]
    return (player1, player2)


if __name__ == '__main__':
    total = 0
    for line in sys.stdin:
        total += score_rps(*translate_rps(line))[1]
    print(total)

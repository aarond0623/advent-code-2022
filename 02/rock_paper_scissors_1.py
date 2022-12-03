"""
--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets to be
closest to the snack storage, a giant Rock Paper Scissors tournament is already
in progress.

Rock Paper Scissors is a game between two players. Each game contains many
rounds; in each round, the players each simultaneously choose one of Rock,
Paper, or Scissors using a hand shape. Then, a winner for that round is
selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats
Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy
guide (your puzzle input) that they say will be sure to help you win. "The
first column is what your opponent is going to play: A for Rock, B for Paper,
and C for Scissors. The second column--" Suddenly, the Elf is called away to
help with someone's tent.

The second column, you reason, must be what you should play in response: X for
Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious,
so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your
total score is the sum of your scores for each round. The score for a single
round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3
for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if
the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you
should calculate the score you would get if you were to follow the strategy
guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

    - In the first round, your opponent will choose Rock (A), and you should
      choose Paper (Y). This ends in a win for you with a score of 8 (2
      because you chose Paper + 6 because you won).
    - In the second round, your opponent will choose Paper (B), and you
      should choose Rock (X). This ends in a loss for you with a score of 1
      (1 + 0).
    - The third round is a draw with both players choosing Scissors, giving
      you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a
total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your
strategy guide?
"""

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
    elif player2 == tools[(tools.index(player1) + 1) % 3]: # Player 2 wins
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

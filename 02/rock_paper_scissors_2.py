"""
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway,
the second column says how the round needs to end: X means you need to lose, Y
means you need to end the round in a draw, and Z means you need to win. Good
luck!"

The total score is still calculated in the same way, but now you need to figure
out what shape to choose so the round ends as indicated. The example above now
goes like this:

    - In the first round, your opponent will choose Rock (A), and you need the
      round to end in a draw (Y), so you also choose Rock. This gives you a
      score of 1 + 3 = 4.
    - In the second round, your opponent will choose Paper (B), and you choose
      Rock so you lose (X) with a score of 1 + 0 = 1.
    - In the third round, you will defeat your opponent's Scissors with Rock
      for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you
would get a total score of 12.

Following the Elf's instructions for the second column, what would your total
score be if everything goes exactly according to your strategy guide?
"""

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

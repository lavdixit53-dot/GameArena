import random

CHOICES = {
    "1": "Snake",
    "2": "Water",
    "3": "Gun"
}

def computer_choice():
    return random.choice(list(CHOICES.values()))


def decide_winner(player, computer):
    if player == computer:
        return "Draw"

    winning_pairs = {
        "Snake": "Water",
        "Water": "Gun",
        "Gun": "Snake"
    }

    if winning_pairs[player] == computer:
        return "Win"

    return "Loss"
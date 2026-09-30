def win_percentage(player):
    total = player.total_games()

    if total == 0:
        return 0

    return (player.wins / total) * 100


def display_statistics(player):
    total = player.total_games()
    percentage = win_percentage(player)

    print("\n========== PLAYER STATISTICS ==========")
    print("Player:", player.name)
    print("Total Games:", total)
    print("Wins:", player.wins)
    print("Losses:", player.losses)
    print("Draws:", player.draws)
    print(f"Win Percentage: {percentage:.2f}%")
    print("========================================")
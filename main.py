from player import Player
from game import CHOICES, computer_choice, decide_winner
from validator import get_player_choice, get_rounds
from statistics import display_statistics
from storage import save_result
from leaderboard import show_leaderboard


def play_game():
    print("\n" + "=" * 45)
    print("              GAME ARENA")
    print("          Snake - Water - Gun")
    print("=" * 45)

    name = input("\nEnter your name: ").strip()

    if not name:
        name = "Player"

    player = Player(name)

    rounds = get_rounds()

    for round_number in range(1, rounds + 1):
        print(f"\n---------- Round {round_number} ----------")

        choice = get_player_choice()
        player_choice = CHOICES[choice]

        computer = computer_choice()

        result = decide_winner(player_choice, computer)

        player.update_score(result)

        print("\nYou selected:", player_choice)
        print("Computer selected:", computer)
        print("Result:", result)

    display_statistics(player)

    save_result(player)

    print("\nYour result has been saved.")
    print("Thank you for playing!")


def main():
    while True:

        print("\n========== GAME ARENA MENU ==========")
        print("1. Start New Game")
        print("2. View Leaderboard")
        print("3. Exit")
        print("=====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            play_game()

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            print("\nExiting Game Arena...")
            break

        else:
            print("\nInvalid choice. Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()
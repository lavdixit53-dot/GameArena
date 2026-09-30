def get_player_choice():
    while True:
        print("\nChoose your option:")
        print("1. Snake")
        print("2. Water")
        print("3. Gun")

        choice = input("Enter choice: ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("Invalid choice. Please enter 1, 2 or 3.")


def get_rounds():
    while True:
        value = input("Enter number of rounds: ").strip()

        if value.isdigit():
            rounds = int(value)

            if 1 <= rounds <= 20:
                return rounds

        print("Please enter a number between 1 and 20.")
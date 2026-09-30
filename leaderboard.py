from storage import load_results


def show_leaderboard():
    records = load_results()

    if not records:
        print("\nNo previous records available.")
        return

    records.sort(key=lambda item: item["wins"], reverse=True)

    print("\n============= LEADERBOARD =============")
    print(f"{'Player':<20}{'Games':<10}{'Wins':<10}")

    for record in records:
        print(
            f"{record['name']:<20}"
            f"{record['games']:<10}"
            f"{record['wins']:<10}"
        )

    print("=======================================")
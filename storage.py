import json
import os

FILE_NAME = "results.json"


def save_result(player):
    data = []

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

    record = {
        "name": player.name,
        "games": player.total_games(),
        "wins": player.wins,
        "losses": player.losses,
        "draws": player.draws
    }

    data.append(record)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_results():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
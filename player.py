class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def update_score(self, result):
        if result == "Win":
            self.wins += 1
        elif result == "Loss":
            self.losses += 1
        else:
            self.draws += 1

    def total_games(self):
        return self.wins + self.losses + self.draws
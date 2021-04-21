class Player:
    count = 0

    def __init__(self, name):
        self.score = 0.0
        self.name = name.upper()
        self.symbol = 'x' if Player.count == 0 else 'o'
        Player.count += 1

    def award_points(self, points):
        self.score += points

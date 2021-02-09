class Team:

    def __init__(self, team_info):
        
        self.name, *self.games = team_info.split(",")
        self.points = self.count_points(self.games)

    def count_points(self, games):
        
        points = 0
        for game in games:
            this_team_score, opponent_score = game.split(":")
            if this_team_score > opponent_score:
                points += 3
            elif this_team_score == opponent_score:
                points += 1
        return points
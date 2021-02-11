class Team:

    def __init__(self, team_info):
        
        if team_info.endswith("\n"):
            team_info = team_info[:-1]

        self.name, *self.games = team_info.split(",")
        self.points = self.count_points(self.games)

    def __eq__(self, other):
        if self.points == other.points:
            return True
        return False
    
    def __gt__(self, other):
        if self.points > other.points:
            return True
        return False
    
    def __lt__(self, other):
        if self.points < other.points:
            return True
        return False

    def count_points(self, games):
        
        points = 0
        for game in games:
            this_team_score, opponent_score = game.split(":")
            if this_team_score > opponent_score:
                points += 3
            elif this_team_score == opponent_score:
                points += 1
        return points
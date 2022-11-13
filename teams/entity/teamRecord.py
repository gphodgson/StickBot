class TeamRecord():
    def __init__(self, stat_data) -> None:
        self.gamesPlayed = stat_data['gamesPlayed']
        self.wins = stat_data['wins']
        self.losses = stat_data['losses']
        self.otl = stat_data['ot']
        self.points = stat_data['pts']
        self.ppPercentage = stat_data['powerPlayPercentage']
        self.pkPercentage = stat_data['penaltyKillPercentage']
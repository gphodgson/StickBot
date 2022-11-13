from teams.entity.teamRecord import TeamRecord

class Team():
    def __init__(self, team_data, slim) -> None:
        self.id = team_data['id']
        self.name = team_data['name']
        if not slim:
            self.record = TeamRecord(team_data['teamStats'][0]["splits"][0]['stat'])
        else:
            self.record = None


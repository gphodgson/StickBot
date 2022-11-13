class TeamsView():
    def __init__(self, teams) -> None:
        self.teams = teams
        pass

    def createOutput(self) -> str:
        output = "**NHL Teams**:\n```"
        for team in self.teams:
            output += f'{team.name}: {team.id}\n'
        output += "```"
        return output
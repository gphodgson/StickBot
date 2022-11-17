from domain.view.view import View
from teams.teamService import TeamService
from teams.views.teamsView import TeamsView
from teams.views.teamView import TeamView

class TeamController():
    def __init__(self, requestService) -> None:
        self.requestService = requestService
        self.teamService = TeamService(self.requestService)

    def handleInput(self, input) -> View:
        if(input.startswith('team ')):
            input = input.lstrip('team ')
            team_id = input
            team = self.teamService.getTeamFromId(team_id)

            return TeamView(team)
        
        if(input.startswith('teams')):
            teamsList = self.teamService.getTeams()

            return TeamsView(teamsList)
        
        return None

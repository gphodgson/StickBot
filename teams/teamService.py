from typing import List
from urllib import response
from teams.entity.team import Team

class TeamService():

    URI_EXTENSTION = 'teams/'

    def __init__(self, requestService) -> None:
        self.requestService = requestService

    def getTeamFromId(self, id) -> Team:
        response = self.requestService.makeGetRequest(self.URI_EXTENSTION + f'{id}', {"expand": "team.stats"})
        team_data = response['teams'][0]
        return Team(team_data, False)

    def getTeams(self) -> List:
        response = self.requestService.makeGetRequest(self.URI_EXTENSTION, {})
        teams = []

        for team_data in response["teams"]:
            teams.append(Team(team_data, True))
        
        return teams
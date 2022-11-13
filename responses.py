from random import randint
import random, teams.team, teams.teamService, nhlRequest.nhlRequestService
import teams.views.teamsView

def handle_response(msg) -> str:
    p_msg = msg.lower()
    requestService = nhlRequest.nhlRequestService.nhlRequestService()

    if p_msg.startswith('$hockey '):
        p_msg = p_msg.lstrip('$hockey ')
        
        if(p_msg.startswith('team ')):
            p_msg = p_msg.lstrip('team ')
            team_id = p_msg
            teamService = teams.teamService.TeamService(requestService)
            team = teamService.getTeamFromId(team_id)

            return team.name
        
        if(p_msg.startswith('teams')):
            teamService = teams.teamService.TeamService(requestService)
            teamsList = teamService.getTeams();
            view = teams.views.teamsView.TeamsView(teamsList);

            return view.createOutput();
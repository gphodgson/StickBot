from nhlRequest.nhlRequestService import nhlRequestService
from teams.teamController import TeamController
from domain.invaildRequestView import InvaildRequestView

def handle_response(msg) -> str:
    p_msg = msg.lower()
    requestService = nhlRequestService()
    teamController = TeamController(requestService)

    if p_msg.startswith('$hockey '):
        p_msg = p_msg.lstrip('$hockey ')

        view = teamController.handleInput(p_msg)

        if view is None:
            view = InvaildRequestView([])

        return view.createOutput()
        
        if(p_msg.startswith('team ')):
            p_msg = p_msg.lstrip('team ')
            team_id = p_msg
            teamService = teams.teamService.TeamService(requestService)
            team = teamService.getTeamFromId(team_id)
            view = teams.views.teamView.TeamView(team)

            return view.createOutput()
        
        if(p_msg.startswith('teams')):
            teamService = teams.teamService.TeamService(requestService)
            teamsList = teamService.getTeams()
            view = teams.views.teamsView.TeamsView(teamsList)

            return view.createOutput()
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
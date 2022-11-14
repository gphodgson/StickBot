from nhlRequest.nhlRequestService import nhlRequestService
from play.playController import PlayController
from teams.teamController import TeamController
from domain.invaildRequestView import InvaildRequestView

async def handle_response(msg, client, true_client) -> str:
    p_msg = msg
    requestService = nhlRequestService()
    teamController = TeamController(requestService)
    playController = PlayController()

    view = None

    if p_msg.startswith('$play '):
        p_msg = p_msg.lstrip('$play ')

        view = await playController.handleInput(p_msg, client, true_client)

    if p_msg.startswith('$hockey '):
        p_msg = p_msg.lstrip('$hockey ')

        view = teamController.handleInput(p_msg)

    if view is None:
        view = InvaildRequestView([])

    return view.createOutput()
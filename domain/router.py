from domain.view.invaildRequestView import InvaildRequestView
from nhlRequest.nhlRequestService import nhlRequestService
from play.playController import PlayController
from teams.teamController import TeamController

class Router():

    COMMAND_KEY= '$'

    def __init__(self, content, msg, client) -> None:
        self.content = content
        self.msg = msg
        self.client = client
        self.output_view = None
        self.requestService = nhlRequestService()
        pass

    def getOutput(self):
        if self.output_view is None:
            return ""
        else:   
            return self.output_view.createOutput()

    async def Route(self):

        if(self.content.startswith(self.COMMAND_KEY)):
            request = self.content.lstrip(self.COMMAND_KEY)

            if(request.startswith(PlayController.PLAY_KEY)):
                request = request.lstrip(PlayController.PLAY_KEY)
                playController = PlayController()

                self.output_view = await playController.handleInput(request, self.msg, self.client)

            elif(request.startswith('hockey ')):
                request = request.lstrip('hockey ')
                teamController = TeamController(self.requestService)

                self.output_view = teamController.handleInput(request)
            
            else:
                self.output_view = InvaildRequestView();
            
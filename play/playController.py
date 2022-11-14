from domain.blankView import BlankView
from domain.view import View
from play.YTDLSource import YTDLSource
from play.views.joinChannelView import JoinChannelView
class PlayController():
    def __init__(self) -> None:
        pass


    async def handleInput(self, usr_input, client, true_client) -> View:
        if true_client.voice_clients == []:
            if client.author.voice:
                await client.author.voice.channel.connect()
            else: 
                return JoinChannelView([])

        player = await YTDLSource.from_url(usr_input, loop=None, stream=True)
        print("sep")
        true_client.voice_clients[0].play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        return BlankView([])
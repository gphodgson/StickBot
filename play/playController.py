from domain.view.blankView import BlankView
from domain.view.view import View
from play.YTDLSource import YTDLSource
from play.views.joinChannelView import JoinChannelView
from play.views.stopPlayingView import StopPlayingView

class PlayController():
    PLAY_KEY = 'play '

    def __init__(self) -> None:
        pass

    async def handleInput(self, content, msg, client) -> View:
        if content == "stop":
            if client.voice_clients != []:
                client.voice_clients[0].stop()
            return StopPlayingView([])
        else:
            if client.voice_clients == []:
                if msg.author.voice:
                    await msg.author.voice.channel.connect()
                else: 
                    return JoinChannelView([])

            player = await YTDLSource.from_url(content, loop=None, stream=True)
            client.voice_clients[0].play(player, after=lambda e: print(f'Player error: {e}') if e else None)

            return BlankView([])
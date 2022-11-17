from discord import VoiceClient


class MusicPlayer(VoiceClient):

    @classmethod
    def make(cls, voiceClient: VoiceClient):
        return cls(voiceClient.client, voiceClient.channel)

    async def on_voice_state_update(self, data) -> None:
        return await super().on_voice_state_update(data)
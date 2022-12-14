import discord, asyncio
import youtube_dl

class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_FORMAT_OPTIONS = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': False,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
    }

    FFMPEG_OPTIONS = {
        'options': '-vn',
    }

    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

        youtube_dl.utils.bug_reports_message = lambda: ''
        self.ytdl = youtube_dl.YoutubeDL(self.YTDL_FORMAT_OPTIONS)

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        youtube_dl.utils.bug_reports_message = lambda: ''
        ytdl = youtube_dl.YoutubeDL(cls.YTDL_FORMAT_OPTIONS)

        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **cls.FFMPEG_OPTIONS), data=data)
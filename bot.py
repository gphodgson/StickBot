import discord
import responses

async def send_msg(msg, usr_msg, is_private, client):
    try:
        response = await responses.handle_response(usr_msg, msg, client);
        await msg.author.send(response) if is_private else await msg.channel.send(response)
        # embed = discord.embeds.Embed(
        #     title="test Title",
        #     description= "This is apparently a description",
        # )
        # await msg.channel.send(embed=embed)
    except Exception as err:
        print(err)

def run_discord_bot(token):
    TOKEN = token

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running...')

    
    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
            
        usr_msg = str(msg.content)

        if usr_msg[0] == '?':
            usr_msg = usr_msg[1:]
            await send_msg(msg, usr_msg, is_private=True, client=client)
        else:
            await send_msg(msg, usr_msg, is_private=False, client=client)

    client.run(TOKEN)
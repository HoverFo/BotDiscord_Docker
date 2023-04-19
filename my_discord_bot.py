import sys
import discord

TOKEN = ''
f = open("TOKEN.txt", "r")
TOKEN = f.read()

if TOKEN == '' :
    sys.exit("Token non dÃ©fini")

intents = discord.Intents.default()
intents.message_content = True    

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'ping b03':
        await message.channel.send(f'pong, {message.author.display_name}!')
        return

client.run(TOKEN)
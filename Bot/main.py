import discord
import asyncio
import _pickle
import os
from Bot import Bot


bob = Bot()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith("!"):
        response = bob.create_response_string(message)
        await client.send_message(message.channel, response)

client.run('NTI0NjIxMjcwNjcxOTQ5ODI3.DvrU_g.dbhFdFN-Sbp_AXHanbOkZIaECTE')
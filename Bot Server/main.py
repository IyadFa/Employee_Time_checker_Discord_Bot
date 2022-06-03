import discord
import requests
import os

TOKEN = 'ADD_TOKEN_HERE_WITHOUT_QUOTES'
GUILD_ID = 'ADD_GUILD_ID_HERE_WITHOUT_QUOTES'
client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after):
    newChannel = before.channel.id if before.channel else None
    oldChannel = after.channel.id if after.channel else None
    if oldChannel == newChannel: 
        return
    
    if newChannel == None:
        paylod = dict(id=member.id, member=member.name, event="Joined")
        r = requests.post('https://your_backend_url/api/post-event/', data=paylod)
        return

    elif oldChannel == None:
        paylod = dict(id=member.id, member=member.name, event="Left")
        r = requests.post('https://your_backend_url/api/post-event/', data=paylod)
        return

    else:
        return

client.run(TOKEN)

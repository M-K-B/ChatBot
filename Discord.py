from http.client import responses
import ctx as ctx
import discord
import json
from click import command
from discord import channel, message
from discord.ext import commands
from pip._vendor.html5lib.treeadapters.sax import prefix
# import msg as msg
from Data import *
from run import functions

client = commands.Bot(command_prefix=',')

@client.event
async def on_message(ctx):
    #Begin: code from author 'abccd' on https://stackoverflow.com/questions/50072365/why-is-my-discord-bot-spamming
    #Used in order to stop the discord bot spamming the chat. ctx = message and message sender info and Client = bot information
    if ctx.author != client.user:
    #End
        user = User(ctx.author, ctx.author.id, 0, 0, 'na')
        action = functions(user, ctx.content)
        await ctx.channel.send(action.run())

#Begin: code from Mo - team member
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Status 29"))
    print('Bot is ready.')
client.run('NjMzMzc1OTI5OTg0NDgzMzI5.XclKAw.JLNvfVMv-4GcWP-ATbaHt3u7xTs')
#End
if __name__ == "__main__":
    pass
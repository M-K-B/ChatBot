from http.client import responses
from random import *
from FootballOdds import *
import random
import ctx as ctx
import discord
import msg as msg
from click import command
from discord import channel, message
from discord.ext import commands
from pip._vendor.html5lib.treeadapters.sax import prefix

client = commands.Bot(command_prefix=',')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Status 29"))
    print('Bot is ready.')
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don�t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes � definitely.',
                 'You may rely on it.']

    await ctx.send(f'question: {question}\nAnswer: {random.choice(responses)}')
@client.command()
async def RunFootballOdds(ctx, arg):
    await ctx.send(main(arg))
    
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
@client.command()
async def kick (ctx,member : discord.Member, reason=None):
    await member.kick(reason=reason)
    await ctx.send("KICKED!!")
@client.command()
async def ban (ctx,member : discord.Member, reason=None):
    await member.ban(reason=reason)
    await ctx.send("BANNED!!")
@client.command()
async def unban (ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
@client.command(pass_context=True)
async def DELETE(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("MESSAGES PURGED!!")
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRole):
        await ctx.send("You're not allowed to do that")
    elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("That's not a command. Use !help for a list of valid commands")
    else:
        print(error, type(error))
        await ctx.send(f'{error}\n{type(error)}\nThat information is useful for Zachary. Please make sure he sees it.')

client.run('NjMzMzc1OTI5OTg0NDgzMzI5.Xa2HRg.J64Fzhg2QVDhA5DwAMfFDpB_9pM')

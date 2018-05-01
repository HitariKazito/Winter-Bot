#winter bot
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import chalk
import time


startup_extensions = ["Music"]
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
class Main_Commands():
    def __init__(self, bot):
        self.bot = bot
        

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e) .__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
@bot.event
async def on_member_join(member):
    serverchannel = discord.Object("424362511136194562")
    msg = "Welcome {0}".format(member.mention, member.server.name)
    await bot.send_message(serverchannel, msg)
@bot.event
async def on_member_leave(member):
    serverchannel = discord.Object("424362511136194562")
    msg = "You'll be missed {0}".format(member.mention)
    await bot.send_message(serverchannel, msg)
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))



@bot.command(pass_context = True)
async def kick(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '':
        await bot.kick(member)
        embed=discord.Embed(title="User kicked!", description="**{0}** was kicked by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)


@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)
    if message.content.startswith('!'):
        userID = message.author.id
        if message.author.id == "194713190049775616":
            args = message.content.split(" ")
            if not args[1] == "!say":
                await bot.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await bot.send_message(message.channel, "You do not have the permission")
            
            
        
        
                
                
    
                
            
bot.run(str(os.environ.get('BOT_TOKEN')))

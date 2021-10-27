import pycord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=':')

@bot.command(name='hello')
async def Hello(ctx):
    await ctx.reply(f'Privyet! {ctx.author.name}')

@bot.command(name='about')
async def about(ctx):
    await ctx.reply('My name is Over.ai \nI am a bot written in the Python programming language. \nMy creator is an idiot (dont tell him i said that) \nMy creator plans to implement more features into me. \nHe says it will depend if he can learn Python quick enough.')


bot.run('ODk5MTE4MTYxNjcxMTAyNTA0.YWuHCg.cuBiSxqDI_u-vTljiiMpZ7_CY48')







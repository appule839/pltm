#main.py
import discord
import asyncio
from dice import *
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = True
intents.presences = True

bot = commands.Bot(command_prefix="p",intents = intents)  # 접두사를 $로 지정

client = discord.client(intents = intents)



@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕하세요!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("존재하지 않는 명령어입니다.")


@bot.command()
async def 주사위(ctx):
    result, _color, bot, user = dice()
    embed = discord.Embed(title = "주사위 게임!", description = None, color = _color)
    embed.add_field(name = "PLTM Bot의 숫자", value = ":game_die: " + bot, inline = True)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: " + user, inline = True)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)



bot.run("token")  #토큰내기
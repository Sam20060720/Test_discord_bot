import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/")


@bot.event
async def on_ready():
    print(">> Bot is online <<")
    channel = bot.get_channel(817937447932919808)
    await channel.send("Bot Online")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(817937447932919808)
    await channel.send(f"{member} join!!!")


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(817937447932919808)
    await channel.send(f"{member} leave!!!")

bot.run("ODE3Nzk3MTcyMDkwNjM0Mjcx.YEOu9w.8a9BKbcUjjLlX5lIiZvk1yoqTgw")

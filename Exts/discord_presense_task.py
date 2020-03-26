from discord.ext import tasks
from itertools import cycle
from App.bot import bot
import discord

status = cycle(
    [
        "404 Not Found",
        "Development version: 20200326",
        "Python Version: 3.8",
        "문의: @zeroday0619#0619"
    ]
)


@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(
            next(
                status
            )
        )
    )
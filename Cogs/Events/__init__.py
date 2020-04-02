from discord.ext import commands
import discord


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has joined a server!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left a server!")


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
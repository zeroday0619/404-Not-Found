from discord.ext import commands
from App.stock.naver import Stocks


class stock(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.stocks = Stocks()

    @commands.command(name="코스피")
    async def kospi(self, ctx):
        source = await self.stocks.KOSPI()
        await ctx.send(
            source
        )

    @commands.command(name="코스닥")
    async def kosdaq(self, ctx):
        source = await self.stocks.KOSDAQ()
        await ctx.send(
            source
        )


def setup(bot: commands.Bot):
    bot.add_cog(stock(bot))
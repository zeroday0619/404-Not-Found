from discord.ext import commands
import discord


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(selfm, ctx, *, member):
        bannedUsers = await ctx.guild.bans()
        memberName, memberDiscriminator = member.split("#")

        for banEntry in bannedUsers:
            user = banEntry.user
            if (user.name, user.memberDiscriminator) == (member.name, memberDiscriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.name}#{user.memberDiscriminator}")
                return


def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))
import discord
from discord.ext import commands


class moderation_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason):
        await ctx.guild.ban(user, reason=reason)
        embed = discord.Embed(
            title=f"El usuario {user} ha sido baneado",
            description=f"Por la siguiente razon **{reason}**",
            color=discord.Color.red(),
        )
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title="Error:",
                description="No tienes permiso para banear",
                color=discord.Color.red(),
            )
            embed.set_thumbnail(
                url="https://media4.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif?cid=ecf05e4796jpo63uru7kuhnzjib511ksrn2rvvrpfrrs4ll8&rid=giphy.gif"
            )
            await ctx.send(embed=embed)

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason):
        await ctx.guild.kick(
            user, reason=reason, delete_message_days=0
        )  # Bans the user.
        embed = discord.Embed(
            title=f"El usuario {user} ha sido kickeado",
            description=f"Por la siguiente razon **{reason}**",
            color=discord.Color.red(),
        )
        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title="Error:",
                description="No tienes permiso para kikear personas",
                color=discord.Color.red(),
            )
            embed.set_thumbnail(
                url="https://media4.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif?cid=ecf05e4796jpo63uru7kuhnzjib511ksrn2rvvrpfrrs4ll8&rid=giphy.gif"
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(moderation_commands(bot))

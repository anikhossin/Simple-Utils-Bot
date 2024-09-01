import discord
from discord.ext import commands


class Modration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(
        name='ban',
        description='Ban a user from the server',
        usage='ban <user> [reason]',
        aliases=['banish'],
        with_app_command=True
    )
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        await ctx.reply(embed=discord.Embed(description=f'`{user.name}` has been banned', color=discord.Color.red()))
        await user.ban(reason=reason)
        
        
    @commands.hybrid_command(
        name='kick',
        description='Kick a user from the server',
        usage='kick <user> [reason]',
        with_app_command=True
    )
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        await ctx.reply(embed=discord.Embed(description=f'`{user.name}` has been kicked', color=discord.Color.red()))
        await user.kick(reason=reason)
        
    
    
async def setup(bot):
    await bot.add_cog(Modration(bot))
        
    
        
    
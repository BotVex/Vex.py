import disnake
from disnake.ext import commands
from random import choice
import json


class Clear(commands.Cog):
    def __init__(self, bot):
    	self.bot: commands.Bot = bot
    
    
    @commands.command()
    @commands.has_permissions(manage_messages=True) 
    async def clear(self, ctx, amount=None):
    	try:
    		await ctx.channel.purge(limit=int(amount))
    	except:
    		pass

def setup(bot):
    bot.add_cog(Clear(bot))
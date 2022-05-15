import disnake
from disnake.ext import commands
from random import choice
import json


class Clear(commands.Cog):
    def __init__(self, bot):
    	self.bot: commands.Bot = bot
    
    
    @commands.slash_command(
    	name='clear',
    	description='apago uma quantidade específica de mensagens.')
    @commands.has_permissions(manage_messages=True) 
    async def clear(self, ctx: disnake.ApplicationCommandInteraction, amount: int):
    	await ctx.response.defer()
    	try:
    		await ctx.channel.purge(limit=amount)
    	except:
    		pass

def setup(bot):
    bot.add_cog(Clear(bot))
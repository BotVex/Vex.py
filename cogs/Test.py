import os
import json

import disnake
from disnake.ext import commands

from random import choice

from config import COWNER


class Test(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.command()
	async def test(self, ctx):
		
			
		await ctx.reply()
	
	
def setup(bot):
    bot.add_cog(Test(bot))
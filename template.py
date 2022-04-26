import os

import disnake
from disnake.ext import commands

from config import COWNER, CERROR, prefix


class COG(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
		#
		
		
def setup(bot):
    bot.add_cog(COG(bot))
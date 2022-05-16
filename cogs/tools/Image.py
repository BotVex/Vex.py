import os
import json

import disnake
from disnake.ext import commands


from config import COWNER


class Test(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(
		name='image',
		description='[🛠️] - eu adiciono efeitos a uma imagem.')
	async def image(self, inter: disnake.ApplicationCommandInteraction):
		
		await inter.send('ok')
	
	
def setup(bot):
    bot.add_cog(Test(bot))
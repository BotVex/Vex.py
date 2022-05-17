import os
import json
from typing import List

import disnake
from disnake.ext import commands

from random import choice

from config import COWNER
import requests 


class Test(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(guild_ids=[957509903273046067])
	async def setavatar(inter: disnake.ApplicationCommandInteraction, avatar: disnake.Attachment):
		await inter.response.defer()
		
		try:
			self.bot.user.edit(avatar=requests.get(avatar.url).content)
			await inter.send('avatar alterado!')
		except:
			await inter.send('falha ao setar o avatar')
	
	
def setup(bot):
    bot.add_cog(Test(bot))
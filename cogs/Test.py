import os
import json
from typing import List

import disnake
from disnake.ext import commands

from random import choice

from config import COWNER


class Test(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command()
	async def languages(inter: disnake.ApplicationCommandInteraction, language: str):
		await inter.send(language)
	
	
	@languages.autocomplete("language")
	async def test_autocomp(self, inter: disnake.ApplicationCommandInteraction, string: str):
		return ["XD", ":D", ":)", ":|", ":("]

	
	
	
	
def setup(bot):
    bot.add_cog(Test(bot))
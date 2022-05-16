import os
import json
from random import choice

import disnake
from disnake.ext import commands

from config import COWNER


class Furry(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		with open('data/games.json', 'r', encoding='utf8') as games:
			games = json.loads(games.read())
		self.games = games
		
		
	@commands.slash_command(
		name='furry',
		description='[🪀] - lhe mostro uma imagem de furry',
		hidden=True)
	async def furry(self, ctx: disnake.ApplicationCommandInteraction):
		await ctx.response.defer()
		
		await ctx.send('ok')
	
	
def setup(bot):
    bot.add_cog(Furry(bot))
import os
import json
from random import choice

import disnake
from disnake.ext import commands

from config import COWNER


class Rg(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		with open('data/games.json', 'r', encoding='utf8') as games:
			games = json.loads(games.read())
		self.games = games
		
		
	@commands.slash_command(
		name='rg',
		description='[🪀] - lhe recomendo um belo jogo.')
	async def rg(self, ctx: disnake.ApplicationCommandInteraction):
		await ctx.response.defer()
		embed = disnake.Embed(
			title='Você quer uma recomendação de jogo?',
			description=f'Aqui vai um belo jogo, o nome dele é:\n`{choice(self.games)}`',
			color=COWNER)
		embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2432/2432632.png')
		await ctx.send(embed=embed)
		
	
	
def setup(bot):
    bot.add_cog(Rg(bot))
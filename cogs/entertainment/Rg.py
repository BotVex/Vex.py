import os
import json

import disnake
from disnake.ext import commands

from random import choice

from config import COWNER


class Rg(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		with open('data/games.json', 'r', encoding='utf8') as games:
			games = json.loads(games.read())
		self.games = games
		
		
	@commands.command(
		name='rg',
		description='*lhe recomendo um belo jogo* :video_game:',
		aliases=[
			'jogo',
			'game'
			])
	async def rg(self, ctx):
		embed = disnake.Embed(
			title='Você quer uma recomendação de jogo?',
			description=f'Aqui vai um belo jogo, o nome dele é:\n`{choice(self.games)}`',
			color=COWNER)
		embed.set_thumbnail(url='https://media.discordapp.net/attachments/965785255321681960/967259857176657930/images__16_-removebg-preview.jpg')
		await ctx.reply(embed=embed)
		
	
	
def setup(bot):
    bot.add_cog(Rg(bot))
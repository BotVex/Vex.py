import os
import json
from pyowo import owo
from PIL import Image
from io import BytesIO
from random import choice
from kaomoji.kaomoji import Kaomoji
kao = Kaomoji()

import disnake
from disnake.ext import commands
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils import dominant_color


class Entertainment(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
		with open('data/animes.json', 'r', encoding='utf8') as animes:
			animes = json.loads(animes.read())
		self.animes = animes
	
	
	@commands.slash_command(
		name='anime',
		description=f'{E.entertainment} | eu envio uma foto de anime aleatória.')
	async def anime(self, inter: disnake.ApplicationCommandInteraction):
		
		await inter.response.defer()
		
		random_anime = choice(self.animes)
		
		get_image = requests.get(random_anime).content
		color = dominant_color(get_image)
		
		embed = disnake.Embed(color=color)
		embed.set_image(
			url=random_anime)
		await inter.send(embed=embed)
	
	
	@commands.slash_command(
		name='owo',
		description=f'{E.entertainment} | eu vou deixar seu texto fofo.',
		options=[
			disnake.Option(
				name='text',
				description='insira um texto para deixá-lo fofo uwu',
				type=disnake.OptionType.string,
				required=True)
			]
		)
	async def owo(self, inter: disnake.ApplicationCommandInteraction, *, text: str):
		await inter.response.defer()
		await inter.send(embed=EB(description=f'**{owo(text[0:4000])}**'))
	
	
	@commands.slash_command(
		name='kaomoji',
		description=f'{E.entertainment} | eu gero um belo kaomoji para você.',
		options=[
			disnake.Option(
				name='category',
				description='selecione uma categoria.',
				type=disnake.OptionType.string,
				required=True
				)
			]
		)
	async def kaomoji(self, inter: disnake.ApplicationCommandInteraction, category: str):
		
		await inter.response.defer()
		
		if category == 'indiferença':
			kaomoji = kao.create('indifference')
		elif category == 'felicidade':
			kaomoji = kao.create('joy')
		elif category == 'amoroso':
			kaomoji = kao.create('love')
		elif category == 'tristeza':
			kaomoji = kao.create('sadness')
		
		await inter.send(kaomoji)
	
	
	@kaomoji.autocomplete('category')
	async def categories(self, inter: disnake.ApplicationCommandInteraction, string: str):
		return [
			'indiferença',
			'felicidade',
			'amoroso',
			'tristeza'
			]
	
def setup(bot):
	bot.add_cog(Entertainment(bot))

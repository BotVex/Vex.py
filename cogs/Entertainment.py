import os
import json
import requests
from pyowo import owo
from PIL import Image
from io import BytesIO
from random import choice
from zalgolib import enzalgofy
from kaomoji.kaomoji import Kaomoji
kao = Kaomoji()

import disnake
from disnake.ext import commands
Localized = disnake.Localized
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.dominant_color import dominant_color


class Entertainment(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
		with open('data/animes.json', 'r', encoding='utf8') as animes:
			animes = json.loads(animes.read())
		self.animes = animes
	
	
	@commands.slash_command()
	async def fun(self, inter: ACI):
		pass
	
	
	@fun.sub_command(
		name='anime',
		description=f'{E.entertainment}Eu envio uma imagem de anime aleatória.')
	@commands.cooldown(1, 60, commands.BucketType.user)
	async def anime_(
		self, 
		inter: ACI):
		
		await inter.response.defer()
		
		random_anime = choice(self.animes)
		
		get_image = requests.get(random_anime).content
		color = dominant_color(get_image)
		
		embed = disnake.Embed(color=color)
		embed.set_image(
			url=random_anime)
		await inter.send(embed=embed)
	
	
	@fun.sub_command(
		name='owo',
		description=f'{E.entertainment}eu vou deixar seu texto fofo.',
		options=[
			disnake.Option(
				name='text',
				description='insira um texto para deixá-lo fofo uwu',
				type=disnake.OptionType.string,
				required=True)
			]
		)
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def owo(self, inter: disnake.ApplicationCommandInteraction, *, text: str):
		await inter.response.defer()
		await inter.send(embed=EB(description=f'**{owo(text[0:4000])}**'))
	
	
	@fun.sub_command(
		name='zalgo',
		description=f'{E.entertainment}eu vou z̸̢̝̈́͋͘a̸̡̫̗̿̈́̇̚ĺ̸̨̥g̴̬̓̈́͠i̷̯̫̎͗̇f̴̅͐ͅḭ̵̧͕̓̓̚c̴̙͆̋͠ͅā̴͇̟̎̄̏r̶̼̳̻͒͝ seu texto.',
		options=[
			disnake.Option(
				name='text',
				description='insira um texto.',
				type=disnake.OptionType.string,
				required=True),
			disnake.Option(
				name='intensity',
				description='intensidade.',
				type=disnake.OptionType.integer,
				min_value=1,
				max_value=100,
				required=False)
			]
		)
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def zalgo(self, inter: disnake.ApplicationCommandInteraction, *, text: str, intensity: int=20):
		await inter.response.defer()
		await inter.send(embed=EB(description=f'**{enzalgofy(text[0:4000])}**'))
	
	
	@fun.sub_command(
		name='kaomoji',
		description=f'{E.entertainment}eu gero um belo kaomoji para você.',
		options=[
			disnake.Option(
				name='category',
				description='selecione uma categoria.',
				type=disnake.OptionType.string,
				required=True
				)
			]
		)
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def kaomoji(
		self, 
		inter: ACI, 
		category: str):
		
		await inter.response.defer()
		
		if category == 'neutral':
			kaomoji = kao.create('indifference')
		elif category == 'happy':
			kaomoji = kao.create('joy')
		elif category == 'random':
			kaomoji = kao.create()
		elif category == 'love':
			kaomoji = kao.create('love')
		elif category == 'sad':
			kaomoji = kao.create('sadness')
		
		await inter.send(kaomoji)
	
	
	@kaomoji.autocomplete('category')
	async def categories(
		self, 
	inter: ACI, 
	string: str):
		return [
			'random',
			'neutral',
			'happy',
			'love',
			'sad'
			]
	
	
	@fun.sub_command(
		name='coinflip',
		description=f'{E.entertainment}jogue o clássico cara ou coroa.',
		options=[
			disnake.Option(
				name='choose',
				description='escolha entre cara ou coroa.',
				type=disnake.OptionType.string,
				required=True
				)
			]
		)
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def coinflip(self, 
	inter: ACI, 
	choose: str):
		
		await inter.response.defer()
		
		bot_choose = choice(['cara', 'coroa'])
		
		if bot_choose == choose:
			embed = EB(
				title=f'`{bot_choose}` x `{choose}`'
				,
				description='você ganhou!',
				color=C.general)
		else:
			embed = EB(
				title=f'`{bot_choose}` x `{choose}`'
				,
				description='você perdeu!',
				color=C.general)
		
		await inter.send(embed=embed)
	
	
	@coinflip.autocomplete('choose')
	async def categories(
		self, 
		inter: ACI, 
		string: str):
		return [
			'cara',
			'coroa'
			]
	
	
def setup(bot):
	bot.add_cog(Entertainment(bot))

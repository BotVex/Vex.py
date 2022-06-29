import os
import json
 
from random import choice
from pyowo import owo as owofy
from kaomoji.kaomoji import Kaomoji
kaofy = Kaomoji()

import disnake
from disnake.ext import commands
from disnake import Localized
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
	
		with open('data/anime_roleplay.json', 'r', encoding='utf8') as animes:
			anime_roleplay = json.loads(animes.read())
		self.anime_roleplay = anime_roleplay
	
	
	@commands.slash_command()
	async def fun(self, inter: ACI):
		pass

	@fun.sub_command(
		name='roleplay',
		description=f'{E.entertainment}Faça um roleplay.',
		options=[
			disnake.Option(
				name='user',
				description='Escolha um usuário.',
				type=disnake.OptionType.user,
				required=True
				),
			disnake.Option(
				name='roleplay',
				description='Escolha uma categoria.',
				type=disnake.OptionType.string,
				required=True
				)
			])
	@commands.cooldown(1, 7, commands.BucketType.user)
	async def roleplay(
		self, 
		inter: ACI,
		user: disnake.Member,
		roleplay: str):
		
		await inter.response.defer()
		
		chosen_anime = choice(self.anime_roleplay[roleplay])
		name = chosen_anime['name']
		url = chosen_anime['url']
		color = chosen_anime['color']
		
		match roleplay:
			case 'highfive':
				message = f'🙏 | {inter.author.mention} deu um highfive em {user.mention}!'
			case 'handhold':
				message = f'🤝 | {inter.author.mention} segurou a mão de {user.mention}!'
			case 'kiss':
				message = f'💋 | {inter.author.mention} beijou {user.mention}!'
			case 'wave':
				message = f'👋 | {inter.author.mention} acenou para  {user.mention}!'
			case 'thumbsup':
				message = f'👍 | {inter.author.mention} fez um "👍" para {user.mention}!'
			case 'stare':
				message = f'👀 | {inter.author.mention} olhou fixamente para {user.mention}!'
			case 'stare':
				message = f'🥺 | {inter.author.mention} fez carinho em {user.mention}!'
			case 'baka':
				message = f'🤬 | {inter.author.mention} chamou {user.mention} de idiota!'
			case 'wink':
				message = f'🔫 | {inter.author.mention} deu um TIRO em {user.mention}!'
			case 'shrug':
				message = f'🤷 | {inter.author.mention} fez um ¯\_(ツ)_/¯ para {user.mention}!'
			case 'kick':
				message = f'🦶 | {inter.author.mention} chutou {user.mention}!'
			case 'hug':
				message = f'🤗 | {inter.author.mention} abraçou {user.mention}!'
			case 'slap':
				message = f'👋 | {inter.author.mention} deu um tapa em {user.mention}!'
			case 'pat':
				message = f'🥰 | {inter.author.mention} fez cafuné em {user.mention}!'
			case 'punch':
				message = f'👊 | {inter.author.mention} deu um soco em {user.mention}!'
			case 'dance':
				message = f'🕺 |  {inter.author.mention} dançou com {user.mention}!'
			case 'bite':
				message = f'🍽️ |  {inter.author.mention} mordeu {user.mention}!'
			case 'shoot':
				message = f'🔫 | {inter.author.mention} atirou em {user.mention}!'
			case _:
				message = f'❓ |  {inter.author.mention}  fez algo que ainta não foi terminado com {user.mention}!'
	
		
		embed = disnake.Embed(
		color=color)
		embed.set_footer(text='Fonte: ' + name)
		embed.set_image(
			url=url)
		await inter.send(content=message, embed=embed)


	@roleplay.autocomplete('roleplay')
	async def categories_(
		self, 
	inter: ACI, 
	string: str):
		categories = []
		for category in self.anime_roleplay:
			if category not in ['happy', 'sleep', 'feed', 'smile', 'laugh', 'poke', 'tickle', 'blush', 'think', 'pout', 'facepalm', 'bored', 'cry', 'cuddle']:
				categories.append(category)
		return sorted(categories)

	
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
	async def owo(
		self, 
		inter: ACI, 
		text: str): 
		await inter.response.defer()
		await inter.send(f'{owofy(text[0:1000])}')
	
	
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
		
		match category:
			case 'neutral':
				kaomoji = kaofy.create('indifference')
			case 'happy':
				kaomoji = kaofy.create('joy')
			case 'random':
				kaomoji = kaofy.create()
			case 'love':
				kaomoji = kaofy.create('love')
			case 'sad':
				kaomoji = kaofy.create('sadness')
		
		await inter.send(kaomoji)
	
	
	@kaomoji.autocomplete('category')
	async def categories(
		self, 
	inter: ACI, 
	string: str):
		return sorted([
			'random',
			'neutral',
			'happy',
			'love',
			'sad'
			])
	
	
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
				title=f'`eu jogei {bot_choose}` e você `{choose}`!'
				,
				description='você ganhou!',
				color=C.general)
		else:
			embed = EB(
				title=f'`eu jogei {bot_choose}` e você `{choose}`!'
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

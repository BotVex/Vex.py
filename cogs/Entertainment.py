import os
import json
import requests #Replace 
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
		
		message = ''
		if roleplay == 'highfive':
			message=f'🙏 | <@{inter.author.id}> deu um highfive em <@{user.id}>!'
		elif roleplay == 'handhold':
			message=f'🤝 | <@{inter.author.id}> segurou a mão de <@{user.id}>!'
		elif roleplay == 'kiss':
			message=f'💋 | <@{inter.author.id}> beijou <@{user.id}>!'
		elif roleplay == 'wave':
			message=f'👋 | <@{inter.author.id}> acenou para  <@{user.id}>!'
		elif roleplay == 'thumbsup':
			message=f'👍 | <@{inter.author.id}> fez um "👍" para <@{user.id}>!'
		elif roleplay == 'stare':
			message=f'👀 | <@{inter.author.id}> olhou fixamente para <@{user.id}>!'
		elif roleplay == 'cuddle':
			message=f'🥺 | <@{inter.author.id}> fez carinho em <@{user.id}>!'
		elif roleplay == 'baka':
			message=f'🤬 | <@{inter.author.id}> chamou <@{user.id}> de idiota!'
		elif roleplay == 'wink':
			message=f'😉 | <@{inter.author.id}> piscou para <@{user.id}>!'
		elif roleplay == 'shoot':
			message=f'🔫 | <@{inter.author.id}> deu um TIRO em <@{user.id}>!'
		elif roleplay == 'shrug':
			message=f'🤷 | <@{inter.author.id}> fez um ¯\_(ツ)_/¯ para <@{user.id}>!'
		elif roleplay == 'kick':
			message=f'🦶 | <@{inter.author.id}> chutou <@{user.id}>!'
		elif roleplay == 'hug':
			message=f'🤗 | <@{inter.author.id}> abraçou <@{user.id}>!'
		elif roleplay == 'slap':
			message=f'👋 | <@{inter.author.id}> deu um tapa em <@{user.id}>!'
		elif roleplay == 'pat':
			message=f'🥰 | <@{inter.author.id}> fez cafuné em <@{user.id}>!'
		elif roleplay == 'punch':
			message=f'👊 | <@{inter.author.id}> deu um soco em <@{user.id}>!'
		elif roleplay == 'dance':
			message=f'🕺 |  <@{inter.author.id}> dançou com <@{user.id}>!'
		elif roleplay == 'bite':
			message=f'😳 |  <@{inter.author.id}> deu um chupão em <@{user.id}>!'
		
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
			if category not in ['happy', 'sleep', 'feed', 'smile', 'laugh', 'poke', 'tickle', 'blush', 'think', 'pout', 'facepalm', 'bored', 'cry']:
				categories.append(category)
		return categories

	
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
		await inter.send(f'**{owofy(text[0:4000])}**')
	
	
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
			kaomoji = kaofy.create('indifference')
		elif category == 'happy':
			kaomoji = kaofy.create('joy')
		elif category == 'random':
			kaomoji = kaofy.create()
		elif category == 'love':
			kaomoji = kaofy.create('love')
		elif category == 'sad':
			kaomoji = kaofy.create('sadness')
		
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

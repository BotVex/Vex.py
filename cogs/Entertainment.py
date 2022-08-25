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
from utils.assets import MediaUrl
from utils.dominant_color import dominant_color


class Entertainment(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
		with open('data/anime_roleplay.json', 'r', encoding='utf8') as animes:
			self.anime_roleplay = json.loads(animes.read())

		with open('data/oracle.json', 'r', encoding='utf8') as oracle_phrases:
			self.oracle_phrases = json.loads(oracle_phrases.read())
	
	
	@commands.slash_command(name=Localized('fun' , key='ENT_FUN_NAME'))
	async def fun(self, inter: ACI):
		pass

	@fun.sub_command(
		name=Localized('roleplay' , key='ENT_FUN_CMD_ROLEPLAY_NAME'),
		description=Localized('Do an roleplay with someone.' , key='ENT_FUN_CMD_ROLEPLAY_DESC'),
		options=[
			disnake.Option(
				name='user',
				description=Localized('Choice a user.' , key='ENT_FUN_CMD_ROLEPLAY_USERDESC'),
				type=disnake.OptionType.user,
				required=True
				),
			disnake.Option(
				name='roleplay',
				description=Localized('Choice a roleplay.' , key='ENT_FUN_CMD_ROLEPLAY_ROLEPLAYDESC'),
				type=disnake.OptionType.string,
				required=True
				)
			])
	@commands.cooldown(1, 7, commands.BucketType.user)
	async def roleplay(self, inter: ACI, user: disnake.Member, roleplay: str):
		
		await inter.response.defer()
		
		if roleplay not in self.anime_roleplay:
			await inter.send('Encenação desconhecida!', ephemeral=True)
			embed = EB()
			return
		else:
			chosen_anime = choice(self.anime_roleplay[roleplay])
			name = chosen_anime['name']
			url = chosen_anime['url']
			color = chosen_anime['color']
			
			embed = EB(color=color)
			embed.set_image(url=url)
			embed.set_footer(text=f'Fonte: {name}')
		
		
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
				message = f'😉 | {inter.author.mention} piscou para {user.mention}!'
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
				message = f'🕺 | {inter.author.mention} dançou com {user.mention}!'
			case 'bite':
				message = f'🍽️ | {inter.author.mention} mordeu {user.mention}!'
			case 'shoot':
				message = f'🔫 | {inter.author.mention} atirou em {user.mention}!'
		

		if inter.author.id == user.id:
			match roleplay:
				case 'highfive':
					message = f'🙏 | {inter.author.mention} deu um highfive em... si mesmo?'
				case 'handhold':
					message = f'🤝 | {inter.author.mention} segurou sua própia mão?'
				case 'kiss':
					message = f'💋 | {inter.author.mention} beijou a si mesmo? Como isso funciona??'
				case 'wave':
					message = f'👋 | {inter.author.mention} acenou para ninguém?\n{self.bot.user.mention} acenou de volta para {inter.author.mention}!'
				case 'thumbsup':
					message = f'👍 | {inter.author.mention} fez um "👍" para ninguém. :smiling_face_with_tear:'
				case 'stare':
					message = f'👀 | {inter.author.mention} olhou fixamente para... si mesmo? :mirror:'
				case 'stare':
					message = f'🥺 | {inter.author.mention} fez carinho em... ninguém? Que estranho.'
				case 'baka':
					message = f'🤬 | {inter.author.mention} chamou a si mesmo de idiota!\nNão fassa isso contigo :('
				case 'wink':
					message = f'😉 | {inter.author.mention} piscou... para ninguém?\n{self.bot.user.mention} piscou para {inter.author.mention}!'
				case 'shrug':
					message = f'🤷 | {inter.author.mention} fez um ¯\_(ツ)_/¯ para si mesmo. ¯\_(ツ)_/¯'
				case 'kick':
					message = f'🦶 | {inter.author.mention} chutou a si mesmo?'
				case 'hug':
					message = f'🤗 | {inter.author.mention} abraçou... ninguém?\n{self.bot.user.mention} abraçou {inter.author.mention}!'
				case 'slap':
					message = f'👋 | {inter.author.mention} deu um tapa em ~si mesmo~ uma mosca!'
				case 'pat':
					message = f'🥰 | {inter.author.mention} fez cafuné em... ninguém?'
				case 'punch':
					message = f'👊 | {inter.author.mention} deu um soco em si mesmo?\nEi ei, sem essa.'
				case 'dance':
					message = f'🕺 | {inter.author.mention} dançou com ninguém?\n{self.bot.user.mention} dançou {inter.author.mention}!'
				case 'bite':
					message = f'🍽️ | {inter.author.mention} mordeu a si mesmo?\nVirou cachorro agora, é?'
				case 'shoot':
					message = f'🔫 | {inter.author.mention} deu um TIRO em si mesmo!\nAinda bem que ele(a) estava usando um colete aprova de balas.'
		
		
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
		name='vidente',
		description=f'{E.entertainment}Faça uma pergunta para o oráculo Ben 10.',
		options=[
			disnake.Option(
				name='question',
				description='Digite sua questão.',
				type=disnake.OptionType.string,
				required=True
				)
			])
	@commands.cooldown(1, 7, commands.BucketType.user)
	async def vidente(self, inter: ACI, question: str):
		
		await inter.response.defer()
		
		channel = inter.channel
		
		channel_webhooks = await channel.webhooks()
		
		for webhook in channel_webhooks:
			if webhook.user == self.bot.user and webhook.name == "Bot Webhook":
				break
		else:
			webhook = await channel.create_webhook(name="Bot Webhook")
		
		await inter.edit_original_message(content='Contactando Ben 10...')

		content = f'{inter.author.mention}, *"{question}"* \n\n{choice(self.oracle_phrases).capitalize()}'

		await webhook.send(username='Ben 10', content=content, avatar_url=MediaUrl.ben10icon)

	
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
			case 'love':
				kaomoji = kaofy.create('love')
			case 'sad':
				kaomoji = kaofy.create('sadness')
			case _:
				kaomoji = kaofy.create()
		
		await inter.send(kaomoji)
	
	
	@kaomoji.autocomplete('category')
	async def categories(
		self, 
	inter: ACI, 
	string: str):
		return sorted([
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
		
		if choose not in ['cara', 'coroa']:
			await inter.send(f'{choose}? não conheço essa moeda...')
			return
		
		if bot_choose == choose:
			embed = EB(
				title=f'`{bot_choose}` X `{choose}`!'
				,
				description='você ganhou!',
				color=C.general)
		else:
			embed = EB(
				title=f'`{bot_choose}` X `{choose}`!'
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

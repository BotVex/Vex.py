import os
import json
import aiohttp
import datetime
 
from random import choice, randint
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
				choices=[
					disnake.OptionChoice(Localized('highfive', key='ENT_FUN_CMD_ROLEPLAY_HIGHFIVE'), 'highfive'),
					disnake.OptionChoice(Localized('handhold', key='ENT_FUN_CMD_ROLEPLAY_HANDHOLD'),  'handhold'),
					disnake.OptionChoice(Localized('kiss', key='ENT_FUN_CMD_ROLEPLAY_KISS'),  'kiss'),
					disnake.OptionChoice(Localized('wave', key='ENT_FUN_CMD_ROLEPLAY_WAVE'),  'wave'),
					disnake.OptionChoice(Localized('thumbsup', key='ENT_FUN_CMD_ROLEPLAY_THUMBSUP'),  'thumbsup'),
					disnake.OptionChoice(Localized('stare', key='ENT_FUN_CMD_ROLEPLAY_STARE'),  'stare'),
					disnake.OptionChoice(Localized('baka', key='ENT_FUN_CMD_ROLEPLAY_BAKA'),  'baka'),
					disnake.OptionChoice(Localized('wink', key='ENT_FUN_CMD_ROLEPLAY_WINK'),  'wink'),
					disnake.OptionChoice(Localized('shoot', key='ENT_FUN_CMD_ROLEPLAY_SHOOT'),  'shoot'),
					disnake.OptionChoice(Localized('shrug', key='ENT_FUN_CMD_ROLEPLAY_SHRUG'),  'shrug'),
					disnake.OptionChoice(Localized('kick', key='ENT_FUN_CMD_ROLEPLAY_KICK'),  'kick'),
					disnake.OptionChoice(Localized('hug', key='ENT_FUN_CMD_ROLEPLAY_HUG'), 'hug'),
					disnake.OptionChoice(Localized('slap', key='ENT_FUN_CMD_ROLEPLAY_SLAP'), 'slap'),
					disnake.OptionChoice(Localized('pat', key='ENT_FUN_CMD_ROLEPLAY_PAT'), 'pat'),
					disnake.OptionChoice(Localized('punch', key='ENT_FUN_CMD_ROLEPLAY_PUNCH'), 'punch'),
					disnake.OptionChoice(Localized('dance', key='ENT_FUN_CMD_ROLEPLAY_DANCE'), 'dance'),
					disnake.OptionChoice(Localized('bite', key='ENT_FUN_CMD_ROLEPLAY_BITE'), 'bite')
					],
				type=disnake.OptionType.string,
				required=True
				)
			])
	@commands.cooldown(1, 15, commands.BucketType.user)
	async def roleplay(self, inter: ACI, user: disnake.User, roleplay: str):
		
		await inter.response.defer()
		
		chosen_anime = choice(self.anime_roleplay[roleplay])
		name = chosen_anime['name']
		url = chosen_anime['url']
		color = chosen_anime['color']
		
		embed = EB(
			color=color,
			timestamp=datetime.datetime.now()
		)

		embed.set_footer(text=f'Fonte: {name} (by nekos.best) | {inter.author.display_name}', icon_url=inter.author.display_avatar)
		embed.set_image(url=url)
	
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
		

		class Retribue(disnake.ui.View):
			def __init__(self):
				super().__init__()
				self.retribued = False
				self.timeout = 60.0
			

			async def on_timeout(self):
				self.clear_items()


			@disnake.ui.button(label="Retrubuir", style=disnake.ButtonStyle.primary, emoji=E.red_reverse)
			async def retribue(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
				if interaction.author.id != user.id:
					await interaction.send(f':octagonal_sign: | Ei!, apenas {user.mention} pode usar isso!', ephemeral=True)
				else:
					self.retribued = True
					button.disabled = True
					self.stop()

		view = Retribue()
		await inter.send(content=message, embed=embed, view=view)
		await view.wait()
		if view.retribued is True: 

			chosen_anime = choice(self.anime_roleplay[roleplay])
			name = chosen_anime['name']
			url = chosen_anime['url']
			color = chosen_anime['color']

			embed_retribued = EB(
				color=color, 
				timestamp=datetime.datetime.now()
			)

			embed_retribued.set_footer(text=f'Fonte: {name} (by nekos.best) | {inter.author.display_name}', icon_url=inter.author.display_avatar)
			embed_retribued.set_image(url=url)

			await inter.send(content=f'{inter.author.mention}, {user.mention} Retribuiu!', embed=embed_retribued)


#['happy', 'sleep', 'feed', 'smile', 'laugh', 'poke', 'tickle', 'blush', 'think', 'pout', 'facepalm', 'bored', 'cry', 'cuddle']


	@commands.bot_has_permissions(manage_webhooks=True)
	@fun.sub_command(
		name=Localized('oracle', key='ENT_FUN_CMD_ORACLE_NAME'),
		description=Localized('Choose an oracle and ask you a question!', key='ENT_FUN_CMD_ORACLE_DESC'),
		options=[
			disnake.Option(
				name='oracle',
				description=Localized('select an oracle.', key='ENT_FUN_CMD_ORACLE_ORACLE'),
				choices=[
					disnake.OptionChoice('Ben 10', 'Ben 10'),
					disnake.OptionChoice('Finn', 'Finn'),
					disnake.OptionChoice('Vovó Juju', 'Vovó Juju')
					],
				type=disnake.OptionType.string,
				required=True
				),
			disnake.Option(
				name='question',
				description=Localized('Enter a question.', key='ENT_FUN_CMD_ORACLE_QUESTION'),
				type=disnake.OptionType.string,
				required=True
				)
			])
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def oracle(self, inter: ACI, oracle: str, question: str):
		
		await inter.response.defer()
		
		channel = inter.channel
		
		channel_webhooks = await channel.webhooks()
		
		for webhook in channel_webhooks:
			if webhook.user == self.bot.user and webhook.name == "Bot Webhook":
				break
		else:
			webhook = await channel.create_webhook(name="Bot Webhook")
		
		await inter.edit_original_message(content=f'Contactando {oracle}...')

		content = f'{inter.author.mention}, *"{question}"* \n\n{choice(self.oracle_phrases)}'

		await webhook.send(username=oracle, content=content, avatar_url=MediaUrl.get_oracle(oracle))

	
	@fun.sub_command(
		name=Localized('owo', key='ENT_FUN_CMD_OWO_NAME'),
		description=Localized('Leave your text Kwai.', key='ENT_FUN_CMD_OWO_DESC'),
		options=[
			disnake.Option(
				name='text',
				description=Localized('Enter a text.', key='ENT_FUN_CMD_OWO_TEXTDESC'),
				type=disnake.OptionType.string,
				required=True)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def owo(self, inter: ACI, text: str): 

		await inter.response.defer()

		avatar_color = self.bot.user.display_avatar.with_size(16)
		async with aiohttp.ClientSession() as session:
			async with session.get(str(avatar_color)) as resp:
				color = dominant_color(await resp.content.read())

		embed = EB(
			color=color,
			timestamp=datetime.datetime.now()
		)

		embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

		embed.description = f'```text\n{owofy(text[0:1000])}\n```'
		await inter.send(embed=embed)
	
	
	@fun.sub_command(
		name=Localized('kaomoji', key='ENT_FUN_CMD_KAOMOJI_NAME'),
		description=Localized('Generate a custom kaomoji.', key='ENT_FUN_CMD_KAOMOJI_DESC'),
		options=[
			disnake.Option(
				name='category',
				description=Localized('Choose a category.', key='ENT_FUN_CMD_KAOMOJI_DESC'),
				choices=[
					disnake.OptionChoice(Localized('neutral', key='ENT_FUN_CMD_KAOMOJI_CATEGORY_CHOICE_NEUTRAL'), 'neutral'),
					disnake.OptionChoice(Localized('happy', key='ENT_FUN_CMD_KAOMOJI_CATEGORY_CHOICE_HAPPY'), 'happy'),
					disnake.OptionChoice(Localized('love', key='ENT_FUN_CMD_KAOMOJI_CATEGORY_CHOICE_LOVE'), 'love'),
					disnake.OptionChoice(Localized('sad', key='ENT_FUN_CMD_KAOMOJI_CATEGORY_CHOICE_SAD'), 'sad'),
					disnake.OptionChoice(Localized('random', key='ENT_FUN_CMD_KAOMOJI_CATEGORY_CHOICE_RANDOM'), 'random')
					],
				type=disnake.OptionType.string,
				required=True
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def kaomoji(self, inter: ACI, category: str):
		
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
			case 'random':
				kaomoji = kaofy.create()

		avatar_color = self.bot.user.display_avatar.with_size(16)
		async with aiohttp.ClientSession() as session:
			async with session.get(str(avatar_color)) as resp:
				color = dominant_color(await resp.content.read())

		embed = EB(
			color=color,
			timestamp=datetime.datetime.now()
		)

		embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

		embed.description = f'```text\n{kaomoji}\n```'
		await inter.send(embed=embed)

	
def setup(bot):
	bot.add_cog(Entertainment(bot))

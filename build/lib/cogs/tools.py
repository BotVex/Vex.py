import io
import qrcode
import aiohttp
import datetime
import tempyrature
from typing import Union

import disnake
from disnake.ext import commands
from disnake import Localized

from src.utils.newassets import GetColor, Emojis

EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

T = tempyrature.Converter


class Tools(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(name=Localized('user', key='TOOLS_USER_NAME'), dm_permission=True)
	async def user(self, inter: ACI):
		pass
	
	
	@commands.slash_command(name=Localized('server', key='TOOLS_SERVER_NAME'), dm_permission=False)
	async def server(self, inter: ACI):
		pass
	
	
	@commands.slash_command(name=Localized('qrcode', key='TOOLS_QRCODE_NAME'), dm_permission=True)
	async def qrcode(self, inter: ACI):
		pass


	@commands.slash_command(name=Localized('convert', key='TOOLS_CONVERT_NAME'), dm_permission=True)
	async def convert(self, inter: ACI):
		pass
	

	#server icon
	@commands.cooldown(2, 10, commands.BucketType.user)
	@server.sub_command(
		name=Localized('tools', key='TOOLS_SERVER_CMD_ICON_NAME'),
		description=Localized('Gets the server icon.', key='TOOLS_SERVER_CMD_ICON_DESC')
	)
	async def icon(self, inter: ACI):
		server_icon = inter.guild.icon
		
		if server_icon != None:
			color = await GetColor.general_color_url(server_icon.with_size(16))
			
			embed = EB(color=color)
			embed.title = f'Icone de `{inter.guild.name}`'
			embed.set_image(url=server_icon)
			
			class OpenInBrowser(disnake.ui.View): 
				def __init__(self):
					super().__init__()
					self.add_item(
						disnake.ui.Button(
							style=disnake.ButtonStyle.link,
							label='Abrir no navegador',
							url=str(inter.guild.icon))
						)
			
			await inter.send(embed=embed, view=OpenInBrowser())
			return
		else:
			await inter.send('O servidor não possuí um ícone.', ephemeral=True)
			return
	
	
	#server banner
	@commands.cooldown(2, 10, commands.BucketType.user)
	@server.sub_command(
		name=Localized('banner', key='TOOLS_SERVER_CMD_BANNER_NAME'),
		description=Localized('Get the server banner.', key='TOOLS_SERVER_CMD_BANNER_DESC'))
	async def banner(self, inter: ACI):
		server_banner = inter.guild.banner
		
		if server_banner != None:
			color = await GetColor.general_color_url(server_banner.with_size(16))
			
			embed = EB(color=color)
			embed.title = f'Banner de `{inter.guild.name}`'
			embed.set_image(url=server_banner)
			
			class OpenInBrowser(disnake.ui.View): 
				def __init__(self):
					super().__init__()
					self.add_item(
						disnake.ui.Button(
							style=disnake.ButtonStyle.link,
							label='Abrir no navegador',
							url=str(inter.guild.icon))
						)
			
			await inter.send(embed=embed, view=OpenInBrowser())
			return
		else:
			await inter.response.send_message('O servidor não possuí um banner.', ephemeral=True)
			return

	
	#user avatar
	@commands.cooldown(2, 10, commands.BucketType.user)
	@user.sub_command(
		name=Localized('avatar', key='TOOLS_USER_CMD_AVATAR_NAME'),
		description=Localized("Gets the user's avatar.", key='TOOLS_USER_CMD_AVATAR_DESC'),
		option=[
			disnake.Option(
				name='user',
				description='Selecione um usuário.',
				type=disnake.OptionType.user,
				required=False
				)
			])
	async def avatar(self, inter: ACI, user: Union[disnake.User, disnake.Member]=None):
			await inter.response.defer()
			
			if user == None:
				user = inter.author
			
			if user.avatar is not None:
				avatar = user.avatar
			else:
				avatar = user.display_avatar
			
			username = user.name

			if isinstance(user, disnake.Member):
				member = await inter.guild.fetch_member(user.id)
				
				if member.guild_avatar is not None:
					avatar = member.guild_avatar
					username = member.display_name
			
			color = await GetColor.general_color_url(avatar.with_size(16))
			
			embed = EB(color=color)
			embed.title = f'Avatar de {username}'
			embed.set_image(url=avatar)

			class Views(disnake.ui.View):
				def __init__(self):
					super().__init__()
					self.value = None
					self.timeout = None
					self.add_item(
						disnake.ui.Button(
							style=disnake.ButtonStyle.link,
							label='Abrir no navegador',
							url=str(avatar)))
				
				
				#TODO: isso não é a melhor forma de fazer, melhorar depois
				@disnake.ui.button(label='Ver avatar global', style=disnake.ButtonStyle.blurple)
				async def view_global_avatar(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
					if user.avatar is not None:
						avatar = user.avatar
					else:
						avatar = user.display_avatar
					
					color = await GetColor.general_color_url(avatar.with_size(16))
					
					embed.color = color
					embed.title = f'Avatar global de {user.name}'
					embed.set_image(url=avatar)
					
					await interaction.send(embed=embed, ephemeral=True, view=disnake.ui.View().add_item(disnake.ui.Button(style=disnake.ButtonStyle.link, label='Abrir no navegador', url=str(avatar))))


			view = Views()
			
			await inter.send(embed=embed, view=view)


	#user banner
	@commands.cooldown(2, 10, commands.BucketType.user)
	@user.sub_command(
		name=Localized('banner', key='TOOLS_USER_CMD_BANNER_NAME'),
		description=Localized('Gets the user\'s banner.', key='TOOLS_USER_CMD_BANNER_DESC'),
		option=[
			disnake.Option(
				name='user',
				description='Selecione um usuário.',
				type=disnake.OptionType.user,
				required=False
				)
			])
	async def banner(self, inter: ACI, user: disnake.User=None):
			if user == None:
				user = inter.author
			
			user_fetch = await self.bot.fetch_user(user.id)
			if user_fetch.banner is not None:
				banner = user_fetch.banner
			
				color = await GetColor.general_color_url(banner.with_size(16))
				
				embed = EB(color=color)
				embed.title = f'Banner de {user.name}'
				embed.set_image(url=banner)
	
				class Link(disnake.ui.View):
					def __init__(self):
						super().__init__()
						self.add_item(
							disnake.ui.Button(
								style=disnake.ButtonStyle.link,
								label='Abrir no navegador',
								url=str(banner)))
	
	
				await inter.send(embed=embed, view=Link())
			else:
				await inter.send(f'{user.display_name} não possui um banner', ephemeral=True)		
	

	#user info
	@commands.cooldown(2, 10, commands.BucketType.user)
	@user.sub_command(
		name=Localized('info', key='TOOLS_USER_CMD_INFO_NAME'),
		description=Localized('Gets information about the user.', key='TOOLS_USER_CMD_INFO_DESC'),
		options=[
			disnake.Option(
				name='user',
				description=Localized('The user to see the information.', key='TOOLS_USER_CMD_INFO_USER'),
				type=disnake.OptionType.user,
				required=False)
			])
	async def info(self, inter: ACI, user: Union[disnake.User, disnake.Member]=None):
		await inter.response.defer()
		
		embeds = []
		
		if user is None:
			user = inter.author
		
		if user.bot is True:
			usertag = f'`{user}` {Emojis.BOT_TAG}'
		else:
			usertag = f'`{user}`'
		
		username = f'`{user.name}`'
		
		user_id = f'`{user.id}`'
		
		user_discrim = f'`{user.discriminator}`'
		
		account_created = f'<t:{int(round(user.created_at.timestamp()))}:f> (<t:{int(round(user.created_at.timestamp()))}:R>)'
		
		if user.avatar is not None:
			avatar = user.avatar
		else:
			avatar = user.display_avatar
			
		_color = await GetColor.general_color_url(avatar.with_size(16))
		
		user_embed = EB(color=_color)
		user_embed.title = f'Informações do usuário:' 
		user_embed.set_thumbnail(url=avatar)
		user_embed.add_field(name='Tag:', value=usertag, inline=False)
		user_embed.add_field(name='Nome:', value=username, inline=True)
		user_embed.add_field(name='Discriminador:', value=user_discrim, inline=True)
		user_embed.add_field(name='ID:', value=user_id, inline=True)
		user_embed.add_field(name='Conta criada em:', value=account_created, inline=True)
		
		user_fetch = await self.bot.fetch_user(user.id)
		
		if user_fetch.banner != None:
			user_embed.set_image(url=user_fetch.banner)
		
		embeds.append(user_embed)
		
		if isinstance(user, disnake.Member):
			member = await inter.guild.fetch_member(user.id)
			
			joined_date = f'<t:{int(round(member.joined_at.timestamp()))}:f> (<t:{int(round(member.joined_at.timestamp()))}:R>)'
			
			member_embed = EB(color=member.color)
			member_embed.title = 'Informações do membro:'
			
			if member.nick is not None:
				member_embed.add_field(name='Apelido no servidor:', value=member.nick, inline=True)
			
			member_embed.add_field(name='Entrou no servidor em:', value=joined_date, inline=True)
			
			if member.current_timeout is not None:
				timestamp = f'<t:{int(round(member.current_timeout.timestamp()))}:f> (<t:{int(round(member.current_timeout.timestamp()))}:R>)'
				
				member_embed.add_field(name='De castigo até:', value=timestamp, inline=True)
			
			if member.top_role.name != '@everyone':
				member_embed.add_field(name='Maior cargo:', value=member.top_role.mention, inline=True)
			
			if member.voice is not None:
				member_embed.add_field(name='Em call em:', value=member.voice.channel.mention, inline=True)
			
			if member.premium_since is not None:
				premium_since_time = f'<t:{int(round(member.premium_since.timestamp()))}:f> (<t:{int(round(member.premium_since.timestamp()))}:R>)'
				
				member_embed.add_field(name='Impulsionando o servidor desde:', value=premium_since_time, inline=True)
			
			if member.guild_avatar is not None:
				member_embed.set_thumbnail(url=member.guild_avatar)
			
			embeds.append(member_embed)
		
		if user.bot is True:
			bot_embed = EB(color=_color)
			bot_embed.title = 'Informações do bot:'
			
			API = f'https://discord.com/api/v10/applications/{user.id}/rpc'
			
			async with aiohttp.ClientSession() as session:
				async with session.get(str(API)) as resp:
					response = await resp.json()
			
			bot_is_public_string = (':white_check_mark: ' if response['bot_public'] is True else ':x: ') + 'Bot público'
			bot_requires_oauth2_string = (':white_check_mark: ' if response['bot_require_code_grant'] is True else ':x: ') + 'Requer código de autenticação via OAuth2'

			bot_other_info = f'''{bot_is_public_string}\n{bot_requires_oauth2_string}'''

			verify_key = f'`{response["verify_key"]}`'
			
			if response['icon'] is not None: 
				application_icon = f'https://cdn.discordapp.com/app-icons/{response["id"]}/{response["icon"]}.png'
				bot_embed.color = await GetColor.general_color_url(application_icon+'?size=16')
				bot_embed.set_thumbnail(url=application_icon)
			
			bot_embed.description = response['description']
			bot_embed.add_field(name='Nome:', value=response['name'], inline=True)
			bot_embed.add_field(name='ID:', value=response['id'], inline=True)
			bot_embed.add_field(name='Outros:', value=bot_other_info, inline=False)
			bot_embed.add_field(name='Chave Pública de Verificação de Requisições HTTP:', value=verify_key, inline=False)

			
			embeds.append(bot_embed)
		
		await inter.send(embeds=embeds)


	#qrcode create
	@commands.cooldown(2, 10, commands.BucketType.user)
	@qrcode.sub_command(
		name=Localized('create', key='TOOLS_QRCODE_CMD_CREATE_NAME'),
		description=Localized('Create a qrcode.', key='TOOLS_QRCODE_CMD_CREATE_DESC'),
		options=[
			disnake.Option(
				name='text',
				description=Localized('Text of qrcode.', key='TOOLS_QRCODE_CMD_CREATE_TEXT'),
				type=disnake.OptionType.string,
				required=True)
			])
	async def create(self, inter: ACI, text: str):
		await inter.response.defer()

		image_qr_code = qrcode.make(text)

		with io.BytesIO() as img_bytes:
			image_qr_code.save(img_bytes, 'png')

			img_bytes.seek(0)

			img_file = disnake.File(img_bytes, filename=f'{hash(img_bytes)}.png')

		embed = EB(color=disnake.Color.from_rgb(255, 255, 255))

		embed.title = 'QR Code'
		embed.set_image(file=img_file)

		embed.timestamp=datetime.datetime.now()
		embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)


		await inter.send(embed=embed)


	#convert temperature
	@commands.cooldown(2, 10, commands.BucketType.user)
	@convert.sub_command(
		name=Localized('temperature', key='TOOLS_CONVERT_CMD_TEMPERATURE_NAME'),
		description=Localized('Convert temperature.', key='TOOLS_CONVERT_CMD_TEMPERATURE_DESC'),
		options=[
			disnake.Option(
				name='value',
				description=Localized('The temperature value.', key='TOOLS_CONVERT_CMD_TEMPERATURE_FROM_VALUE_DESC'),
				type=disnake.OptionType.integer,
				required=True),
			disnake.Option(
				name='scale',
				description=Localized('The temperature scale.', key='TOOLS_CONVERT_CMD_TEMPERATURE_FROM_SCALE_DESC'),
				type=disnake.OptionType.string,
				required=True,
				choices=[
					disnake.OptionChoice(name=Localized('Celcius', key='CELCIUS_NAME'), value='Celcius'),
					disnake.OptionChoice(name=Localized('Fahrenheit', key='FAHRENHEIT_NAME'), value='Fahrenheit'),
					disnake.OptionChoice(name=Localized('Kelvin', key='KELVIN_NAME'), value='Kelvin')
				]),
			disnake.Option(
				name='to_scale',
				description=Localized('The target scale.', key='TOOLS_CONVERT_CMD_TEMPERATURE_TO_SCALE_DESC'),
				type=disnake.OptionType.string,
				required=True,
				choices=[
					disnake.OptionChoice(name=Localized('Celcius', key='CELCIUS_NAME'), value='Celcius'),
					disnake.OptionChoice(name=Localized('Fahrenheit', key='FAHRENHEIT_NAME'), value='Fahrenheit'),
					disnake.OptionChoice(name=Localized('Kelvin', key='KELVIN_NAME'), value='Kelvin')
				])
			])
	async def temperature(self, inter: ACI, value: int, scale: str, to_scale: str):
		await inter.response.defer()

		if to_scale == scale:
			await inter.send('Você não pode converter uma temperatura para ela mesma.', ephemeral=True)
			return
		
		else:
			# C > F
			if scale == 'Celcius' and to_scale == 'Fahrenheit': 
				conversion = T.celsius2fahrenheit(value)

			# C > K
			if scale == 'Celcius' and to_scale == 'Kelvin':
				conversion = T.celsius2kelvin(value)
			# F > C
			if scale == 'Fahrenheit' and to_scale == 'Celcius':
				conversion = T.fahrenheit2celsius(value)
			# F > K
			if scale == 'Fahrenheit' and to_scale == 'Kelvin':
				conversion = T.fahrenheit2kelvin(value)
			# K > C
			if scale == 'Kelvin' and to_scale == 'Celcius':
				conversion = T.kelvin2celsius(value)
			# K > F
			if scale == 'Kelvin' and to_scale == 'Fahrenheit':
				conversion = T.kelvin2fahrenheit(value)


			color = await GetColor.general_color_url(inter.author.display_avatar.with_size(16))

			embed = EB(color=color, timestamp=datetime.datetime.now())

			embed.title = f'{scale} > {to_scale}'
			embed.description = f'{str(value)}{"°" if scale in ["Celcius", "Fahrenheit"] else ""}'+scale[0:1] + ' = ' + f'{str(round(conversion, 2))}{"°" if to_scale in ["Celcius", "Fahrenheit"] else ""}'+to_scale[0:1]
			embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)
			
			
			await inter.send(embed=embed)


	#TODO: adicionar os comandos de cores novamente


def setup(bot):
	bot.add_cog(Tools(bot))

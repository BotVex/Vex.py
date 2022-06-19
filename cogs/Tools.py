import os
import qrcode
import aiohttp
from PIL import Image


import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Colors as C
from utils.assets import Emojis as E
from utils.buttonLink import ButtonLink
from utils.assets import MediaUrl
from utils.dominant_color import dominant_color


class Tools(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(name='tools')
	async def tools(self, inter: ACI):
		pass
	
	
	@tools.sub_command_group(name='colors')
	async def colors(self, inter: ACI):
		pass
	
	
	@tools.sub_command_group(name='discord')
	async def discord(self, inter: ACI):
		pass
	
	
	#servericon
	@commands.guild_only()
	@commands.cooldown(1, 7, commands.BucketType.user)
	@tools.sub_command()
	async def uptime(
		self, 
		inter: ACI):
		await inter.response.defer()
		
		await inter.send(BOTUPTIME)


	@commands.guild_only()
	@commands.cooldown(1, 7, commands.BucketType.user)
	@discord.sub_command(
		name='servericon',
		description=f'{E.tools}Obtém o ícone do servidor.')
	async def servericon(
		self, 
		inter: ACI):
		await inter.response.defer()
		
		if inter.guild.icon == None:
			no_icon = True
		else:
			no_icon = False
			icon_color = inter.guild.icon.with_size(16)
			async with aiohttp.ClientSession() as session:
				async with session.get(str(icon_color)) as resp:
					color = dominant_color(await resp.content.read())
		
		image_icon = MediaUrl.noguildicon if no_icon is True else inter.guild.icon
		
		embed = EB(
			title=f'Ícone de `{inter.guild.name}`.',
			description='' if no_icon is False else 'Como o servidor não possuí um ícone, eu decidi te mostrar essa bela imagem.',
			color=0xFFFFFF if no_icon is True else color)
		embed.set_image(url=image_icon)
	
		
		await inter.send(embed=embed, view=ButtonLink('ver no navegador', str(image_icon)))
	
	
	#serverbanner
	@commands.guild_only()
	@commands.cooldown(1, 7, commands.BucketType.user)
	@discord.sub_command(
		name='serverbanner',
		description=f'{E.tools}Obtém o baner do servidor.')
	async def banner(self, inter: disnake.ApplicationCommandInteraction):
		await inter.response.defer()
		
		if inter.guild.banner == None:
			no_icon = True
		else:
			no_icon = False
			icon_color = inter.guild.icon.with_size(16)
			async with aiohttp.ClientSession() as session:
				async with session.get(str(icon_color)) as resp:
					color = dominant_color(await resp.content.read())
		
		image_icon = MediaUrl.noguildicon if no_icon is True else inter.guild.banner

		embed = EB(
			title=f'Baner de `{inter.guild.name}`.',
			description='' if no_icon == False else 'Como o servidor não possuí um baner, eu decidi te mostrar essa bela imagem.',
			color=0xFFFFFF if no_icon is True else color)
		embed.set_image(url=image_icon)

		
		await inter.send(embed=embed, view=ButtonLink('ver no navegador', str(image_icon)))
	
	
	#avatar
	@commands.guild_only()
	@commands.cooldown(1, 7, commands.BucketType.user)
	@discord.sub_command(
		name='avatar',
		description=f'{E.tools}Obtém o avatar de um usuário do servidor.',
		option=[
			disnake.Option(
				name='user',
				description='Selecione um usuário.',
				type=disnake.OptionType.user,
				required=False
				)
			])
	async def avatar(
		self,
		inter: ACI,
		user: disnake.Member=None):
			await inter.response.defer()
			if user==None:
				user = inter.author
			
			avatar = user.display_avatar
			avatar_color = avatar.with_size(16)
			
			async with aiohttp.ClientSession() as session:
				async with session.get(str(avatar_color)) as resp:
					color = dominant_color(await resp.content.read())
			
			embed = EB(color=color)
			embed.set_image(url=avatar)
			
			await inter.send(f'Avatar de {user.mention}', embed=embed, view=ButtonLink('ver no navegador', str(user.display_avatar)))

	"""
	#channelinfo
	commands.is_owner()
	commands.cooldown(1, 7, commands.BucketType.user)
	@discord.sub_command(
		name='channelinfo',
		description='Obtém informações de um canal do servidor.',
		options=[
			disnake.Option(
				name='channel',
				description='Selecione um canal.',
				type=disnake.OptionType.channel,
				required=True
				)
			]
		)
	async def channelinfo(
	self, 
	inter: ACI, 
	channel: disnake.TextChannel):
			embed = disnake.Embed(
					color=C.general, 
					description=channel.mention)
			embed.add_field(
					name='Hash:', 
					value=str(hash(user))
					)
			embed.add_field(
					name='Nome:', 
					value=channel.name
					)
			embed.add_field(
					name='Servidor:', 
					value=channel.guild
					)
			embed.add_field(
					name='ID:', 
					value=channel.id
					)
			embed.add_field(
					name='ID da categoria:', 
					value=channel.category_id
					)
			embed.add_field(
					name='Posição:', 
					value=channel.position
					)
			embed.add_field(
					name='NSFW:', 
					value=str('Não' if channel.is_nsfw() is False else 'Sim')
					)
			embed.add_field(
					name='Membros (em cache)', 
					value=str(len(channel.members))
					)
			embed.add_field(
					name='Categoria:', 
					value='Sem categoria' if channel.category is None else channel.category
					)
			
			await inter.send(embed=embed)
"""
	
	#userinfo
	@commands.guild_only()
	@commands.cooldown(1, 7, commands.BucketType.user)
	@discord.sub_command(
		name='userinfo',
		description='Obtém informações de um usuário do servidor.',
		options=[
			disnake.Option(
				name='user',
				description='Selecione um usuário.',
				type=disnake.OptionType.user,
				required=False)
			])
	async def userinfo(
		self, 
		inter: ACI, 
		user: disnake.Member=None):
			if user is None:
					user = inter.author
			
			if user.bot is True:
				name = f'{user.name} {E.botTag}'
			else:
				name= f'{user.name}'
			
			if user.nick is None:
				nick = name 
			else: 
				nick = user.nick
				#nick = f'{nick} {E.botTag}'
			
			id = f'`{user.id}`'
			status = f'`{user.status}`' 
	
			voice_state = 'Não está em call' if not user.voice else user.voice.channel
			voice = f'`{voice_state}`'
			toprole = f'{user.top_role.name}'
			if toprole == '@everyone':
					toprole = 'Não possui cargo'
			else:
				toprole = f'<@&{user.top_role.id}>'
			
			roles = ' '.join([r.mention for r in user.roles][1:])
			
			avatar = f'{user.display_avatar}'
			embed = disnake.Embed(
					title=f'Informações de {name}:', 
					color=user.colour
					)
			embed.set_thumbnail(
					url=avatar
					)
			embed.add_field(
					name='Nick:',
					value=nick,
					inline=True
					)
			embed.add_field(
					name='Discriminador:',
					value=user.discriminator,
					inline=True
					)
			embed.add_field(
					name='Hash:',
					value=str(hash(user)),
					inline=False
					)
			embed.add_field(
					name='ID:',
					value=id,
					inline=True
					)
			embed.add_field(
					name='Em call em:',
					value=voice,
					inline=False
					)
			embed.add_field(
					name=f'Cargos - ({len(user.roles)-1}):',
					value=roles,
					inline=False
					)
			embed.add_field(
					name='Maior cargo:',
					value=toprole,
					inline=False
					)
			user_fetch = await self.bot.fetch_user(user.id)
			if user_fetch.banner != None:
				embed.set_image(url=user_fetch.banner)
			await inter.send(embed=embed)


	#generate
	@commands.guild_only()
	@commands.cooldown(1, 7, commands.BucketType.user)
	@colors.sub_command(
		name='generate',
		description=f'{E.tools}Gera uma cor.')
	async def color(self, inter: ACI):
		await inter.response.defer()
		try:
			
			RGB = C.genRGBtuple()
			
			embed = EB(
				title='Informações sobre a cor:',
				color=int(C.RGB2HEX(RGB), 16))
			embed.add_field('RGB:', value=RGB, inline=True)
			
			embed.add_field('HEX:', value='#'+C.RGB2HEX(RGB), inline=True)
			
			embed.add_field('HSV:', value=C.RGB2HSVtuple(RGB), inline=False)
			
			color_img_obj = Image.new(mode='RGB', size=(100, 100), color=RGB)
			color_img_obj.save('data/temp/Color.png', format='png')
			
			embed.set_image(file=disnake.File('data/temp/Color.png'))
			os.remove('data/temp/Color.png')
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error}Não foi possivel gerar a cor.',
				color=C.error)
			await inter.send(embed=embed)
	
	
	#renderrgb
	@commands.guild_only()
	@commands.cooldown(1, 7, commands.BucketType.user)
	@colors.sub_command(
		name='renderrgb',
		description=f'{E.tools}Renderiza uma cor através de um RGB.',
		options=[
			disnake.Option(
				name='r',
				description='red',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=255
				),
			disnake.Option(
				name='g',
				description='green',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=255
				),
			disnake.Option(
				name='b',
				description='blue',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=255
				)
			])
	async def renderRGB(
		self, 
		inter: ACI,
		r: int=0,
		g: int=0,
		b: int=0):
		await inter.response.defer()
		try:
			
			RGB = (r, g, b)
			
			embed = EB(
				title='Informações sobre a cor:',
				color=int(C.RGB2HEX(RGB), 16))
			embed.add_field('RGB', value=RGB)
			embed.add_field('HEX', value='#'+C.RGB2HEX(RGB))
			embed.add_field('HSV:', value=C.RGB2HSVtuple(RGB), inline=False)
			
			color_img_obj = Image.new(mode='RGB', size=(100, 100), color=RGB)
			color_img_obj.save('data/temp/Color.png', format='png')
			
			embed.set_image(file=disnake.File('data/temp/Color.png'))
			os.remove('data/temp/Color.png')
			await inter.send(embed=embed)
		except Exception as e:
			print(e)
			embed = EB(
				title=f'{E.error}Não foi possivel renderizar a cor.',
				color=C.error)
			await inter.send(embed=embed)
	
	
	#renderhex
	@commands.guild_only()
	@commands.cooldown(1, 7, commands.BucketType.user)
	@colors.sub_command(
		name='renderhex',
		description=f'{E.tools}Renderiza uma cor através de um código hexadecimal.',
		options=[
			disnake.Option(
				name='hex_code',
				description='Código hexadecimal. (EX: #B12345)',
				type=disnake.OptionType.string,
				required=True
				)
			])
	async def renderHEX(
		self, 
		inter: ACI,
		hex_code: str):
		await inter.response.defer()
		try:
			
			if not hex_code.startswith('#'):
				hex_code = '#'+hex_code
			
			RGB = C.HEX2RGBtuple(hex_code)
			print(RGB)
			
			embed = EB(
				title='Informações sobre a cor:',
				color=int(C.RGB2HEX(RGB), 16))
			embed.add_field('RGB', value=RGB)
			embed.add_field('HEX', value='#'+C.RGB2HEX(RGB)) 
			embed.add_field('HSV:', value=C.RGB2HSVtuple(RGB), inline=False)
			
			color_img_obj = Image.new(mode='RGB', size=(100, 100), color=RGB)
			color_img_obj.save('data/temp/Color.png', format='png')
			
			embed.set_image(file=disnake.File('data/temp/Color.png'))
			os.remove('data/temp/Color.png')
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error}Não foi possivel renderizar a cor.',
				color=C.error)
			await inter.send(embed=embed)
	
	
	#qrcode
	@commands.guild_only()
	@commands.cooldown(1, 7, commands.BucketType.user)
	@tools.sub_command(
		name='qrcode',
		description=f'{E.tools}Gera um qrcode.',
		options=[
			disnake.Option(
				name='text',
				description='Informe um texto para transformar em qrcode.',
				required=True)])
	async def qrcode(self, inter: ACI, text: str):
		await inter.response.defer()
		try:
			embed = disnake.Embed(
				description=f'**{text[0:2000]}**',
				color=0xFFFFFF)
				
			qr = qrcode.make(text)
			qr.save('data/temp/QRcode.png')
			
			embed.set_image(file=disnake.File('data/temp/QRcode.png'))
			
			os.remove('data/temp/QRcode.png')
			
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error}Não foi possivel gerar o qrcode.',
				color=C.error)
			await inter.send(embed=embed)
	
	
def setup(bot):
	bot.add_cog(Tools(bot))
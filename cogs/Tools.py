import os
import qrcode
import requests
from PIL import Image


import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Colors as C
from utils.assets import Emojis as E
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
	@discord.sub_command(
		name='servericon',
		description=f'{E.tools}Obtém o ícone do servidor.')
	async def servericon(
	  self, 
	  inter: ACI):
		await inter.response.defer()
		
		if inter.guild.icon == None:
			no_icon = True
			icon = MediaUrl.noguildicon
		else:
			no_icon = False
			icon = inter.guild.icon
		
		color = dominant_color(requests.get(icon).content)
		
		embed = EB(
			title=inter.guild.name,
			description='' if no_icon == False else 'Como o servidor não possuí um ícone, eu decidi te mostrar essa bela imagem.',
			color=color)
		embed.set_image(url=icon)
		
		await inter.send(embed=embed)
	
	
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
			icon = MediaUrl.noguildicon
		else:
			no_icon = False
			icon = inter.guild.icon
		
		color = dominant_color(requests.get(icon).content)
		
		embed = EB(
			title=inter.guild.name,
			description='' if no_icon == False else 'Como o servidor não possuí um baner, eu decidi te mostrar essa bela imagem.',
			color=color)
		embed.set_image(url=icon)
		
		await inter.send(embed=embed)
	
	
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
			
			embed = EB(
				description=f'**Avatar de <@{user.id}>**',
				color=dominant_color(requests.get(avatar).content))
			embed.set_image(url=avatar)
			
			await inter.send(embed=embed)
	
	
	#generate
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
			embed.add_field('RGB:', value=RGB, inline=False)
			
			embed.add_field('HEX:', value='#'+C.RGB2HEX(RGB), inline=False)
			
			embed.add_field('HSV:', value=C.RGB2HSVtuple(RGB), inline=False)
			
			color_img_obj = Image.new(mode='RGB', size=(100, 100), color=RGB)
			color_img_obj.save('data/temp/Color.png', format="png")
			
			embed.set_image(file=disnake.File('data/temp/Color.png'))
			os.remove('data/temp/Color.png')
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error}Não foi possivel gerar a cor.',
				color=C.error)
			await inter.send(embed=embed)
	
	
	#renderrgb
	@commands.cooldown(1, 7, commands.BucketType.user)
	@colors.sub_command(
		name='render_rgb',
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
			color_img_obj.save('data/temp/Color.png', format="png")
			
			embed.set_image(file=disnake.File('data/temp/Color.png'))
			os.remove('data/temp/Color.png')
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error}Não foi possivel renderizar a cor.',
				color=C.error)
			await inter.send(embed=embed)
	
	
	#renderhex
	@commands.cooldown(1, 7, commands.BucketType.user)
	@colors.sub_command(
		name='render_hex',
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
			color_img_obj.save('data/temp/Color.png', format="png")
			
			embed.set_image(file=disnake.File('data/temp/Color.png'))
			os.remove('data/temp/Color.png')
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error}Não foi possivel renderizar a cor.',
				color=C.error)
			await inter.send(embed=embed)
	
	
	#qrcode
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
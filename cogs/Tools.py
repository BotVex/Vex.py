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
	
	
	@discord.sub_command(
		name='servericon',
		description=f'{E.tools} | lhe envio o ícone do servidor.')
	async def Tools(self, inter: disnake.ApplicationCommandInteraction):
		await inter.response.defer()
		
		if inter.guild.icon == None:
			no_icon = True
			icon = 'https://media.discordapp.net/attachments/845865181283352616/976544576640794624/9152fdef6eda843249ed83a5606fa745279afbae7681b1b33a8f1b43746cdb99_3.jpg'
		else:
			no_icon = False
			icon = inter.guild.icon
		
		color = dominant_color(requests.get(icon).content)
		
		embed = EB(
			title=inter.guild.name,
			description='' if no_icon == False else 'como o servidor não tem um ícone, eu decidi te mostrar essa bela imagem.',
			color=color)
		embed.set_image(url=icon)
		
		await inter.send(embed=embed)
	
	
	@discord.sub_command(
		name='avatar',
		description=f'{E.tools} | lhe mostro o avatar de um usuário do servidor.',
		option=[
			disnake.Option(
				name='user',
				description='selecione um usuário.',
				type=disnake.OptionType.user,
				required=False
				)
			])
	async def avatar(
		self,
		inter: ACI,
		user: disnake.Member=None):
			if user==None:
				user = inter.author
			
			avatar = user.display_avatar
			
			embed = EB(
				title=f'avatar de <@{user.id}>',
				color=dominant_color(requests.get(avatar).content))
			embed.set_image(url=avatar)
			
			await inter.send(embed=embed)
	
	
	@colors.sub_command(
		name='generate',
		description=f'{E.tools} | eu gero uma bela cor para você.')
	@commands.cooldown(1, 7, commands.BucketType.user)
	async def color(self, inter: ACI):
		try:
			await inter.response.defer()
			
			RGB = C.genRGBtuple()
			
			embed = EB(
				title='informações sobre a cor:',
				color=int(C.RGB2HEX(RGB), 16))
			embed.add_field('RGB:', value=RGB, inline=False)
			
			embed.add_field('HEX:', value='#'+C.RGB2HEX(RGB), inline=False)
			
			embed.add_field('HSV:', value=C.RGB2HSVtuple(RGB), inline=False)
			
			color_img_obj = Image.new(mode='RGB', size=(100, 100), color=RGB)
			color_img_obj.save('data/Color.png', format="png")
			
			embed.set_image(file=disnake.File('data/Color.png'))
			os.remove('data/Color.png')
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error} | não foi #possivel gerar a cor.',
				color=C.error)
			await inter.send(embed=embed)
	
	
	@colors.sub_command(
		name='render_rgb',
		description=f'{E.tools} | eu vou renderizar uma cor através de um RGB.',
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
	@commands.cooldown(1, 7, commands.BucketType.user)
	async def renderRGB(
		self, 
		inter: ACI,
		r: int=0,
		g: int=0,
		b: int=0):
		try:
			await inter.response.defer()
			
			RGB = (r, g, b)
			
			embed = EB(
				title='informações sobre a cor:',
				color=int(C.RGB2HEX(RGB), 16))
			embed.add_field('RGB', value=RGB)
			embed.add_field('HEX', value='#'+C.RGB2HEX(RGB))
			embed.add_field('HSV:', value=C.RGB2HSVtuple(RGB), inline=False)
			
			color_img_obj = Image.new(mode='RGB', size=(100, 100), color=RGB)
			color_img_obj.save('data/Color.png', format="png")
			
			embed.set_image(file=disnake.File('data/Color.png'))
			os.remove('data/Color.png')
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error} | não foi possivel renderizar a cor.',
				color=C.error)
			await inter.send(embed=embed)
	
	

	@colors.sub_command(
		name='render_hex',
		description=f'{E.tools} | eu vou renderizar uma cor através de um código hexadecimal.',
		options=[
			disnake.Option(
				name='hex_code',
				description='o código hexadecimal. (EX: #B12345)',
				type=disnake.OptionType.string,
				required=True
				)
			])
	@commands.cooldown(1, 7, commands.BucketType.user)
	async def renderHEX(
		self, 
		inter: ACI,
		hex_code: str):
		try:
			await inter.response.defer()
			
			if not hex_code.startswith('#'):
				hex_code = '#'+hex_code
			
			RGB = C.HEX2RGBtuple(hex_code)
			print(RGB)
			
			embed = EB(
				title='informações sobre a cor:',
				color=int(C.RGB2HEX(RGB), 16))
			embed.add_field('RGB', value=RGB)
			embed.add_field('HEX', value='#'+C.RGB2HEX(RGB)) 
			embed.add_field('HSV:', value=C.RGB2HSVtuple(RGB), inline=False)
			
			color_img_obj = Image.new(mode='RGB', size=(100, 100), color=RGB)
			color_img_obj.save('data/Color.png', format="png")
			
			embed.set_image(file=disnake.File('data/Color.png'))
			os.remove('data/Color.png')
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error} | não foi possivel renderizar a cor.',
				color=C.error)
			await inter.send(embed=embed)
			
	
	@tools.sub_command(
		name='qrcode',
		description=f'{E.tools} | eu vou gerar um belo qrcode para você.',
		options=[
			disnake.Option(
				name='text',
				description='informe um texto para transformar em qrcode.',
				required=True)])
	@commands.cooldown(1, 7, commands.BucketType.user)
	async def qrcode(self, inter: ACI, text: str):
		await inter.response.defer()
		try:
			embed = disnake.Embed(
				description=f'**{text[0:2000]}**',
				color=0xFFFFFF)
				
			qr = qrcode.make(text)
			qr.save('data/QRcode.png')
			
			embed.set_image(file=disnake.File('data/QRcode.png'))
			
			os.remove('data/QRcode.png')
			
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error} | não foi possivel gerar o qrcode.',
				color=C.error)
			await inter.send(embed=embed)
	
	
def setup(bot):
	bot.add_cog(Tools(bot))
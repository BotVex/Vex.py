import os
import qrcode
import requests
from PIL import Image
from random import randint as rint

import disnake
from disnake.ext import commands
EB = disnake.Embed

from utils.assets import Colors as C
from utils.assets import Emojis as E
from utils.dominant_color import dominant_color


class Tools(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
	
	
	@commands.slash_command(
		name='servericon',
		description=f'{E.tools_emoji} | lhe envio o ícone do servidor.')
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
	
	
	@commands.slash_command(
		name='color',
		description=f'{E.tools_emoji} | eu gero uma bela cor para você.')
	async def color(self, inter: disnake.ApplicationCommandInteraction):
		
		await inter.response.defer()
		
		RGB = C.genRGBtuple()
		
		embed = EB(
			title='informações sobre a cor:',
			color=int(C.RGB2HEX(RGB), 16))
		embed.add_field('RGB', value=RGB)
		embed.add_field('HEX', value='#'+C.RGB2HEX(RGB))
		
		color_img_obj = Image.new(mode='RGB', size=(100, 100), color=RGB)
		color_img_obj.save('data/Color.png', format="png")
		
		embed.set_image(file=disnake.File('data/Color.png'))
		os.remove('data/Color.png')
		await inter.send(embed=embed)
	
	
	@commands.slash_command(
		name='qrcode',
		description=f'{E.tools_emoji} | eu vou gerar um belo qrcode para você.')
	async def qrcode(self, inter: disnake.ApplicationCommandInteraction, text: str):
		
		await inter.response.defer()
		
		embed = disnake.Embed(
			description=f'**{text}**',
			color=0xFFFFFF)
			
		qr = qrcode.make(text)
		qr.save('data/QRcode.png')
		
		embed.set_image(file=disnake.File('data/QRcode.png'))
		
		os.remove('data/QRcode.png')
		
		await inter.send(embed=embed)
	
	
def setup(bot):
	bot.add_cog(Tools(bot))
import os
from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageGrab
from io import BytesIO
import requests

import disnake
from disnake.ext import commands

from config import prefix, CERROR


class Ph(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
	@commands.command(
		name='ph',
		description=f'',
		aliases=[
			'photoshop'
			])
	async def colorize(self, ctx):
		embed = disnake.Embed(
			title='',
			description='')
		embed.set_author(name='baixando... [1/3]', icon_url='https://media.discordapp.net/attachments/965785255321681960/967475227149865010/output-onlinegiftools.gif')
		msg = await ctx.reply(embed=embed)
			
		image_bytes = requests.get(ctx.message.attachments[0]).content
		embed = disnake.Embed(
				title='',
				description='')
		embed.set_author(name='gerando... [2/3]', icon_url='https://media.discordapp.net/attachments/965785255321681960/967475227149865010/output-onlinegiftools.gif')
		msg = await msg.edit(embed=embed)
			
		image = BytesIO(image_bytes)
			
		#img = Image.open(image).convert('RGB')
		#img = ImageOps.autocontrast(img, cutoff=5, ignore=5)
		#img = img.filter(ImageFilter.GaussianBlur(radius = 1))
		img = ImageGrab.grab(bbox = None)
		img.save('data/Crop.png', 'png')
		file = disnake.File('data/Crop.png', filename='Crop.png')
			
		embed_ = disnake.Embed(
				title='',
				description='')
		embed_.set_image(file=file)
			
		os.remove('data/Crop.png')
		
		embed = disnake.Embed(
				title='',
				description='')
		embed.set_author(name='enviando... [3/3]', icon_url='https://media.discordapp.net/attachments/965785255321681960/967475227149865010/output-onlinegiftools.gif')
		msg = await msg.edit(embed=embed)
		
		await msg.edit(embed=embed_)
		
		
def setup(bot):
    bot.add_cog(Ph(bot))
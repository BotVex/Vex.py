import os
from PIL import Image, ImageOps
from colorthief import ColorThief

from io import BytesIO
import requests

import disnake
from disnake.ext import commands

from config import prefix, CERROR


class Mirror(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
	@commands.command(
		name='espelhar',
		description=f'*eu vou espelhar horizontalmente sua imagem*',
		aliases=[
			'mirror'
			])
	async def equlize(self, ctx):
		progress = disnake.Embed()
		
		progress_gif = 'https://media.discordapp.net/attachments/965785255321681960/967475227149865010/output-onlinegiftools.gif'
		error_gif = 'https://media.discordapp.net/attachments/900417473499779102/967871875160105040/output-onlinegiftools_1.gif'
		
		#[1/3]
		progress.set_author(
			name='baixando... [1/3]', 
			icon_url=progress_gif)
		msg = await ctx.reply(embed=progress)
		
		attachments = ctx.message.attachments
		
		if len(attachments) != 0:
			name, extension = os.path.splitext(str(attachments[0]))
		else:
			extension = 'no_file.nan'
		
		if extension not in ['.gif', '.GIF', '.png', '.PNG', '.jpg', '.JPG']:
			progress.set_author(
				name='você preciza enviar uma imagem!\n(gif, png ou jpg)', 
				icon_url=error_gif)
			await msg.edit(embed=progress)
			return
		else:
			attachment = attachments[0]
		
		try:
			image_bytes = requests.get(attachment).content
		except:
			progress.set_author(
				name='não foi possível baixar a imagem',
				icon_url=error_gif)
			await msg.edit(embed=progress)
			return
		
		#[2/3]
		progress.set_author(
			name='gerando...  [2/3]', 
			icon_url=progress_gif)
		msg = await msg.edit(embed=progress)
		try:
			img = BytesIO(image_bytes)
				
			img_obj = Image.open(img).convert('RGB')
			img_cont = ImageOps.mirror(img_obj)
			img_cont.save('datamirrored.png', 'png')
			color_thief = ColorThief('datamirrored.png')
			dominant_color = color_thief.get_color(quality=1)
			material = ''.join(f'{i:02X}' for i in dominant_color)
			file = disnake.File('datamirrored.png', filename='autocontrast.png')
			os.remove('datamirrored.png')
			
			file_embed = disnake.Embed(
				color=int(material, 16))
			file_embed.set_image(file=file)
		except:
			progress.set_author(
				name='não foi possível processar a imagem',
				icon_url=error_gif)
			await msg.edit(embed=progress)
			return

		#[3/3]
		progress.set_author(
			name='enviando... [3/3]', 
			icon_url=progress_gif)
		msg = await msg.edit(embed=progress)
		try:
			await msg.edit(embed=file_embed)
		except:
			progress.set_author(
				name='não foi possível enviar a imagem',
				icon_url=error_gif)
			await msg.edit(embed=progress)
			return
		
		
def setup(bot):
    bot.add_cog(Mirror(bot))
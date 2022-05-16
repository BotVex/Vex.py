import os
from PIL import Image, ImageOps
from colorthief import ColorThief

from io import BytesIO
import requests

import disnake
from disnake.ext import commands

from config import prefix, CERROR


class Contrast(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
	@commands.slash_command(
		name='contraste',
		description=f'eu vou tentar ajustar o contraste de sua foto automaticamente.')
	async def contraste(self, inter: disnake.ApplicationCommandInteraction, file: disnake.file):
		
		await inter.response.defer()
		
		await inter.send(file=file)
		"""
		
		if len(attachments) != 0:
			name, extension = os.path.splitext(str(attachments[0]))
		else:
			extension = 'no_file.nan'
		
		if extension not in ['.gif', '.GIF', '.png', '.PNG', '.jpg', '.JPG', '.jpeg', '.JPEG']:
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
		
		try:
			img = BytesIO(image_bytes)
				
			img_obj = Image.open(img).convert('RGB')
			img_cont = ImageOps.autocontrast(img_obj, cutoff=5, ignore=5)
			img_cont.save('data/autocontrast.png', 'png')
			color_thief = ColorThief('data/autocontrast.png')
			dominant_color = color_thief.get_color(quality=1)
			material = ''.join(f'{i:02X}' for i in dominant_color)
			file = disnake.File('data/autocontrast.png', filename='autocontrast.png')
			os.remove('data/autocontrast.png')
			
			file_embed = disnake.Embed(
				color=int(material, 16))
			file_embed.set_image(file=file)
		except Exception as e:
			print(e)
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
		
		"""
def setup(bot):
    bot.add_cog(Contrast(bot))
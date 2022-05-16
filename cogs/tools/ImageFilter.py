import os
import json
from io import BytesIO
from PIL import Image, ImageOps, ImageFilter
import requests

from colorthief import ColorThief

import disnake
from disnake.ext import commands
EB = disnake.Embed

from config import COWNER, CERROR


class Imagefilter(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(
		name='imagefilter',
		description='[🛠️] - eu adiciono efeitos a uma imagem.')
	async def imagefilter(self, inter: disnake.ApplicationCommandInteraction, filter: str, file: disnake.Attachment):
		await inter.response.defer()
		
		filter = filter.strip()
		
		
		if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
			await inter.send(embed=EB(title='<:unknown_file:975886833181421661> | formato de arquivo não suportado', color=CERROR))
			return
		else:
			img = BytesIO(await file.read())
			
			if filter == 'contraste':
				img_obj = Image.open(img).convert('RGB')
				filtered_image = ImageOps.autocontrast(img_obj, cutoff=5, ignore=5)
			
			elif filter == 'equalizar':
				img_obj = Image.open(img).convert('RGB')
				filtered_image = ImageOps.equalize(img_obj, mask=None)
			
			elif filter == 'virar':
				img_obj = Image.open(img).convert('RGB')
				filtered_image = ImageOps.flip(img_obj)
			
			elif filter == 'espelhar':
				img_obj = Image.open(img).convert('RGB')
				filtered_image = ImageOps.mirror(img_obj)
			
			elif filter == 'inverter':
				img_obj = Image.open(img).convert('RGB')
				filtered_image = ImageOps.invert(img_obj)
			
			elif filter == 'posterizar':
				img_obj = Image.open(img).convert('RGB')
				filtered_image = ImageOps.posterize(img_obj, 2)
			
			elif filter == 'solarizar':
				img_obj = Image.open(img).convert('RGB')
			
			elif filter == 'acizentar':
				img_obj = Image.open(img).convert('RGB')
				filtered_image = ImageOps.grayscale(img_obj)
			
			elif filter == 'clareza':
				img_obj = Image.open(img).convert('RGB')
				filtered_image = img_obj.filter(ImageFilter.UnsharpMask())
			
			elif filter == 'borrar':
				img_obj = Image.open(img).convert('RGB') 
				filtered_image = img_obj.filter(ImageFilter.GaussianBlur(radius=10))
			else:
				await inter.send(embed=EB(title='<:unavailable_filter:975888355051044874> | filtro indisponível', color=CERROR))
				return
			
			
			filtered_image.save(f'data/{file.filename}', format='png')
			await inter.send(file=disnake.File(f'data/{file.filename}', filename=file.filename))
			os.remove(f'data/{file.filename}')

	@imagefilter.autocomplete('filter')
	async def filters_list(self, inter: disnake.ApplicationCommandInteraction, string: str):
		return [
			'contraste',
			'equalizar',
			'virar',
			'espelhar',
			'inverter',
			'posterizar',
			'solarizar',
			'acizentar',
			'clareza',
			'borrar'
		]
	
	
def setup(bot):
    bot.add_cog(Imagefilter(bot))
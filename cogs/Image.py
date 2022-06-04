import os
import json
import requests
from io import BytesIO
from PIL import Image, ImageOps, ImageFilter


import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.imagefilter import Filters as F

class Image_(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command()
	async def image(self, inter: ACI):
		pass
	
	@image.sub_command_group()
	async def filter(self, inter: ACI):
		pass
	
	@image.sub_command_group()
	async def fun(self, inter: ACI):
		pass
	
	
	#autocontrast
	@filter.sub_command(
		name='autocontrast',
		description=f'{E.image} | normalize o contraste da imagem.',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				),
			disnake.Option(
				name='cutoff',
				description='porcentagem a remover dos pixels claros e escuros. [0-100]',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=100
				),
			disnake.Option(
				name='ignore',
				description='o valor do pixel a ser ignorado [0-255]',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=255
				),
			disnake.Option(
				name='preserve_tone',
				description='preserva o tom da imagem.',
				type=disnake.OptionType.boolean,
				required=False
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def autocontrast(
		self, 
		inter: ACI,
		file: disnake.Attachment,
		cutoff: int=0,
		ignore: int=None,
		preserve_tone: bool=False):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.autocontrast(await file.read(), cutoff, ignore, preserve_tone=preserve_tone)
				img.save('data/autocontrast.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/autocontrast.png')
				os.remove('data/autocontrast.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	#equalize
	@filter.sub_command(
		name='equalize',
		description=f'{E.image} | cria uma distribuição uniforme de tons de cinza na imagem.',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def equalize(
		self, 
		inter: ACI,
		file: disnake.Attachment):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.equalize(await file.read())
				img.save('data/equalize.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/equalize.png')
				os.remove('data/equalize.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	#flip
	@filter.sub_command(
		name='flip',
		description=f'{E.image} | vire a imagem verticalmente (de cima para baixo).',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def flip(
		self, 
		inter: ACI,
		file: disnake.Attachment):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.flip(await file.read())
				img.save('data/flip.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/flip.png')
				os.remove('data/flip.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	#mirror
	@filter.sub_command(
		name='mirror',
		description=f'{E.image} | vire a imagem horizontalmente (da esquerda para a direita).',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def mirror(
		self, 
		inter: ACI,
		file: disnake.Attachment):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.mirror(await file.read())
				img.save('data/mirror.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/mirror.png')
				os.remove('data/mirror.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	#invert
	@filter.sub_command(
		name='invert',
		description=f'{E.image} | inverta as cores da imagem.',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def invert(
		self, 
		inter: ACI,
		file: disnake.Attachment):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.invert(await file.read())
				img.save('data/invert.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/invert.png')
				os.remove('data/invert.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	#grayscale
	@filter.sub_command(
		name='grayscale',
		description=f'{E.image} | converta a imagem para tons de cinza.',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def grayscale(
		self, 
		inter: ACI,
		file: disnake.Attachment):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.grayscale(await file.read())
				img.save('data/grayscale.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/grayscale.png')
				os.remove('data/grayscale.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	#posterize
	@filter.sub_command(
		name='posterize',
		description=f'{E.image} | reduza o número de bits da imagem.',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				),
			disnake.Option(
				name='bits',
				description='o número de bits a serem mantidos. [1-8]',
				type=disnake.OptionType.integer,
				required=False,
				min_value=1,
				max_value=8
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def posterize(
		self, 
		inter: ACI,
		file: disnake.Attachment,
		bits: int=3):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.posterize(await file.read(), bits=bits)
				img.save('data/posterize.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/posterize.png')
				os.remove('data/posterize.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	#solarize
	@filter.sub_command(
		name='solarize',
		description=f'{E.image} | inverta todos os valores de um pixel acima de um limite.',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				),
			disnake.Option(
				name='threshold',
				description='todos os pixels acima deste nível de escala de cinza são invertidos. [0-255]',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=255
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def solarize(
		self, 
		inter: ACI,
		file: disnake.Attachment,
		threshold: int=20):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.solarize(await file.read(), threshold=threshold)
				img.save('data/solarize.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/solarize.png')
				os.remove('data/solarize.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	#unsharp
	@filter.sub_command(
		name='unsharp',
		description=f'{E.image} | nitidez.',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				),
			disnake.Option(
				name='radius',
				description='raio de desfoque. [0-100]',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=100
				),
			disnake.Option(
				name='percent',
				description='intensidade. [0-100]',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=100
				),
			disnake.Option(
				name='threshold',
				description='mudança mínima de brilho que será aprimorada. [0-100]',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=100
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def unsharp(
		self, 
		inter: ACI,
		file: disnake.Attachment,
		radius: int=0,
		percent: int=10,
		threshold: int=3):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.unsharp(await file.read(), radius=radius, percent=percent, threshold=threshold)
				img.save('data/unsharp.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/unsharp.png')
				os.remove('data/unsharp.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	#blur
	@filter.sub_command(
		name='blur',
		description=f'{E.image} | desfoca a imagem.',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				),
			disnake.Option(
				name='intensity',
				description='intensidade do desfocamento. [0-100]',
				type=disnake.OptionType.integer,
				required=False,
				min_value=0,
				max_value=100
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def blur(
		self, 
		inter: ACI,
		file: disnake.Attachment,
		intensity: int=10):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.gaussianblur(await file.read(), radius=intensity)
				img.save('data/blur.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/blur.png')
				os.remove('data/blur.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
				"""	
	#ascii
	@filter.sub_command(
		name='ascii',
		description=f'{E.image} | converte a imagem em um texto ascii',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				),
			disnake.Option(
				name='characters',
				description='caracteres que serão usados para formar a imagem. (EX: .:!?%$@&#)',
				type=disnake.OptionType.string,
				required=False
				)
			]
		)
	async def ascii_(
		self, 
		inter: ACI,
		file: disnake.Attachment,
		characters: str='.:!?%$@&#'):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				ascii_text = F.image2ascii(await file.read(), ascii_chars=characters)
				
				with open('data/ascii_art.txt', 'w') as f:
					f.write(ascii_text)
				file_ = disnake.File('data/ascii_art.txt')
				os.remove('data/ascii_art.txt')
				await inter.send(file=file_)"""
	#pixelize
	@filter.sub_command(
		name='pixelize',
		description=f'{E.image} | pixelize a imagem.',
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				),
			disnake.Option(
				name='pixels',
				description='a quantidade de pixels da imagem. [1-512]',
				type=disnake.OptionType.integer,
				required=True,
				min_value=0,
				max_value=512
				),
			disnake.Option(
				name='resize',
				description='manter a imagem no tamanho original?',
				type=disnake.OptionType.boolean,
				required=False
				)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)
	async def pixelize(
		self, 
		inter: ACI,
		file: disnake.Attachment,
		pixels: int,
		resize: bool=True):
			await inter.response.defer()
			if file.content_type not in ['image/bmp', 'image/jpeg', 'image/x-icon', 'image/x-portable-pixmap', 'image/png']:
				await inter.send(embed=EB(title=f'{E.unknown_file} | formato de arquivo não suportado.', color=C.error))
				return
			elif int(file.size) > 2000000:
				await inter.send(embed=EB(title=f'{E.error} | o arquivo é muito grante.', description='máximo 2MB', color=C.error))
				return
			else:
				img = F.pixelize(await file.read(), bits=pixels, resize=resize)
				img.save('data/pixelize.png', 'png', optimize=True, quality=80)
				
				file = disnake.File('data/pixelize.png')
				os.remove('data/pixelize.png')
				embed = EB()
				embed.set_image(file=file)
				await inter.send(embed=embed)
	
	
	@commands.guild_only()
	@fun.sub_command(
		name='stonks',
		description=f'{E.image} | faço um meme do stonks com o avatar de algum usuário.',
		options=[
			disnake.Option(
				name='user',
				description='mencione um usuário.',
				type=disnake.OptionType.user,
				required=False)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)	
	async def stonks(
		self, 
		inter: ACI, 
		user: disnake.Member=None):
		
		await inter.response.defer()
		
		if user == None:
			user = inter.author
		
		stonks_img = Image.open("data/stonks.jpg")
		stonks_obj = stonks_img.copy()
		avatar = user.avatar.with_size(128)
		avatar_obj = Image.open(BytesIO(await avatar.read()))
		avatar_obj = avatar_obj.resize((140, 140))
		stonks_obj.paste(avatar_obj, (83, 45))
		
		stonks_obj.save("data/stonked.jpg")
		file = disnake.File("data/stonked.jpg", filename='stonked.jpg')
		os.remove("data/stonked.jpg")
		embed = EB()
		embed.set_image(file=file)
		await inter.send(embed=embed)
	

def setup(bot):
	bot.add_cog(Image_(bot))

import os
import json
from pyowo import owo
from PIL import Image
from io import BytesIO
from random import choice
from kaomoji.kaomoji import Kaomoji
kao = Kaomoji()

import disnake
from disnake.ext import commands
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C

class Entertainment(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
		
	@commands.slash_command(
		name='stonks',
		description=f'{E.image_emoji} | stonks')
	async def stonks(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member=None):
		
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
	
	
	@commands.slash_command(
		name='owo',
		description=f'{E.ioio_emoji} | eu vou deixar seu texto fofo')
	async def owo(self, inter: disnake.ApplicationCommandInteraction, *, text: str):
		await inter.response.defer()
		await inter.send(owo(str(text)))
	
	
	@commands.slash_command(
		name='kaomoji',
		description=f'{E.ioio_emoji} | eu gero um belo kaomoji para você.')
	async def kaomoji(self, inter: disnake.ApplicationCommandInteraction, category: str):
		
		await inter.response.defer()
		
		if category == 'indiferença':
			kaomoji = kao.create('indifference')
		elif category == 'felicidade':
			kaomoji = kao.create('joy')
		elif category == 'amoroso':
			kaomoji = kao.create('love')
		elif category == 'tristeza':
			kaomoji = kao.create('sadness')
		
		await inter.send(kaomoji)
	
	
	@kaomoji.autocomplete('category')
	async def categories(self, inter: disnake.ApplicationCommandInteraction, string: str):
		return [
			'indiferença',
			'felicidade',
			'amoroso',
			'tristeza'
			]
	
def setup(bot):
	bot.add_cog(Entertainment(bot))

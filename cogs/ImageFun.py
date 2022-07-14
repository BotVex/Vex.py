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
	
	
	@commands.slash_command(name='img')
	async def image(self, inter: ACI):
		pass
	
	
	@image.sub_command_group()
	async def fun(self, inter: ACI):
		pass
	
	
	@commands.guild_only()
	@fun.sub_command(
		name='stonks',
		description=f'{E.image}Crie um meme do Stonks.',
		options=[
			disnake.Option(
				name='user',
				description='Usuário.',
				type=disnake.OptionType.user,
				required=False)
			]
		)
	@commands.cooldown(1, 10, commands.BucketType.user)	
	async def stonks(
		self, 
		inter: ACI, 
		user: disnake.User=None):
		
		await inter.response.defer()
		
		if user == None:
			user = inter.author
		
		stonks_obj = Image.open("data/images/stonks.jpg").copy()
		
		avatar = user.avatar.with_size(128)
		avatar_obj = Image.open(BytesIO(await avatar.read())).resize((140, 140))
		
		stonks_obj.paste(avatar_obj, (83, 45))
		
		stonks_result = BytesIO()
		
		stonks_obj.save(stonks_result, format='jpg')
		
		file = disnake.File(stonks_result, filename=f'{user.name}_Stonks.jpg')
		
		embed = EB()
		embed.set_image(file=file)
		await inter.send(embed=embed)
	

def setup(bot):
	bot.add_cog(Image_(bot))

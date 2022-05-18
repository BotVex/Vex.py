import os
import json
from random import choice
from PIL import Image
from io import BytesIO

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
		description='')
	async def stonks(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member=None):
		
		await inter.response.defer()
		
		if user == None:
			user = inter.author
		
		stonks_obj = Image.open("data/stonks.jpg")
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
	bot.add_cog(Entertainment(bot))

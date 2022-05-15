import os
from PIL import Image
from io import BytesIO

import disnake
from disnake.ext import commands

from random import randint as rint


class Color(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
	@commands.slash_command(
		name='color',
		description='eu gero uma bela cor para você!')
	async def color(self, ctx: disnake.ApplicationCommandInteraction):
		
		await ctx.response.defer()
		
		RGB = (rint(0, 255), rint(0, 255), rint(0, 255))
		HEX = ''.join(f'{i:02X}' for i in RGB)
		
		embed = disnake.Embed(
			title='informações sobre a cor:',
			description='',
			color=int(HEX, 16))
		embed.add_field('RGB', value=RGB)
		embed.add_field('HEX', value='#'+HEX)
		
		color = Image.new(mode='RGB', size=(100, 100), color=RGB)
		color.save('data/Color.png', format="png")
		
		file = disnake.File('data/Color.png')
		embed.set_image(file=file)
		os.remove('data/Color.png')
		await ctx.edit_original_message(content='', embed=embed)
		
		
def setup(bot):
    bot.add_cog(Color(bot))
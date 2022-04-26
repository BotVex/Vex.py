import os
from PIL import Image

import disnake
from disnake.ext import commands

from random import randint as rint


class Color(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
	@commands.command(
		name='color',
		description='*eu gero uma bela cor para você!*',
		aliases=[
			'cor'
			])
	async def color(self, ctx, *, text=None):
		embed = disnake.Embed(
			title='',
			description='')
		embed.set_author(name='gerando...', icon_url='https://media.discordapp.net/attachments/965785255321681960/967475227149865010/output-onlinegiftools.gif')
		
		msg = await ctx.reply(embed=embed)
		
		RGB = (rint(0, 255), rint(0, 255), rint(0, 255))
		HEX = ''.join(f'{i:02X}' for i in RGB)
		
		embed = disnake.Embed(
			title='informações sobre a cor:',
			description='',
			color=int(HEX, 16))
		embed.add_field('RGB', value=RGB)
		embed.add_field('HEX', value='#'+HEX)
		
		color = Image.new(mode='RGB', size=(100, 100), color=RGB)
		color.save("data/Color.png", format="png")
		
		file = disnake.File('data/Color.png')
		embed.set_image(file=file)
		os.remove('data/Color.png')
		await msg.edit(content='', embed=embed)
		
		
def setup(bot):
    bot.add_cog(Color(bot))
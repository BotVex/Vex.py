import os
import requests

import disnake
from disnake.ext import commands

from config import COWNER


class Print(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
	
	
	@commands.command(
		name='print',
		description='eu tiro uma screenshot de um site inteiro pra você.',
		aliases=[
			'screenshot'
			])
	async def print(self, ctx, url):
		p = requests.get(f'https://api.screenshotmachine.com?key=967555&url={url}&dimension=1024x768').content
		with open('print.png', 'wb') as f:
			f.write(p)
		await ctx.reply(file=disnake.File('print.png'))
		os.remove('print.png')
	
	
def setup(bot):
	bot.add_cog(Print(bot))
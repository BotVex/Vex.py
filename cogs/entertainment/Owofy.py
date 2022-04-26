import os
import json
from pyowo import owo

import disnake
from disnake.ext import commands

from random import choice

from config import prefix


class Owofy(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
	@commands.command(
		name='owo',
		description='*eu vou deixaw seu texto Kawai* :point_right: :point_left:',
		aliases=[
			'uwu'
			])
	async def owo(self, ctx, *, text=None):
		if text == None:
			embed = disnake.Embed(
				title='você precisa informar um texto!',
				description=f'EX: `{prefix}owo texto legal`')
			await ctx.reply(embed=embed)
		else:
			await ctx.reply(owo(str(text)))
		
		
def setup(bot):
    bot.add_cog(Owofy(bot))
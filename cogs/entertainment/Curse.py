import os
import json
from random import choice

import disnake
from disnake.ext import commands

from config import COWNER


class Curse(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		with open('data/curses.json', 'r', encoding='utf8') as curses:
			curses = json.loads(curses.read())
		self.curses = curses
		
		
	@commands.slash_command(
		name='xingar',
		description='te digo um xingamento besta. 😳')
	async def xingar(self, ctx: disnake.ApplicationCommandInteraction):
		await ctx.response.defer()
		embed = disnake.Embed(
			title=f'seu {choice(self.curses)}',
			color=COWNER)
		await ctx.send(embed=embed)
	
	
def setup(bot):
    bot.add_cog(Curse(bot))
import os
import json

import disnake
from disnake.ext import commands

from random import choice



class Kaomojis(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		with open('data/mojis.json', 'r', encoding='utf8') as mojis:
			mojis = json.loads(mojis.read())
		self.mojis = mojis
		
		
	@commands.slash_command(
		name='mojis',
		description='te mostro um belo kaomoji. ｡◕‿‿◕｡')
	async def mojis(self, ctx: disnake.ApplicationCommandInteraction):
		await ctx.response.defer()
		await ctx.send(choice(self.mojis))
	
	
def setup(bot):
    bot.add_cog(Kaomojis(bot))
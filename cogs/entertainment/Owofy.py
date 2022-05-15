import os
from pyowo import owo

import disnake
from disnake.ext import commands


class Owofy(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
	@commands.slash_command(
		name='owo',
		description='eu vou deixaw seu texto Kawai. :point_right: :point_left:')
	async def owo(self, ctx: disnake.ApplicationCommandInteraction, *, text: str):
		await ctx.response.defer()
		await ctx.send(owo(str(text)))
		
		
def setup(bot):
    bot.add_cog(Owofy(bot))
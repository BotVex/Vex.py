import disnake
from disnake.ext import commands

import config
import random


class Ping(commands.Cog):
		def __init__(self, bot):
				self.bot: commands.Bot = bot
	 
		#@commands.cooldown(1, 60, commands.BucketType.user)
		
		@commands.slash_command(
			name='ping',
			description='[🤖] - apenas o meu comando de ping.'
			)
		async def ping(self, inter: disnake.ApplicationCommandInteraction):
			latency_val = int(round(self.bot.latency * 1000))

			if latency_val <= 190:
				latency = latency_val
				latency_color = 0x8DFF9D
			
			elif 191 >= latency_val or latency_val <= 350:
				latency = latency_val
				latency_color=0xFFFC90
			
			elif latency_val >= 351:
				latency = latency_val
				latency_color=0xFF8787
			
			
			embed = disnake.Embed(
				title=f':ping_pong: | {inter.author.name}, eu estou com ***{latency}ms*** de ping!',
				color=latency_color)
			
			await inter.send(embed=embed)


def setup(bot):
		bot.add_cog(Ping(bot))
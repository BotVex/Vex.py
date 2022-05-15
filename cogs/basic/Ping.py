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
			description='apenas o meu comando de ping. 🏓'
			)
		async def ping(self, ctx: disnake.ApplicationCommandInteraction):
			latency_val = int(round(self.bot.latency * 1000))

			if latency_val <= 190:
				latency = f'***{latency_val}ms***'
				latency_color = 0x16ff02
			
			elif 191 >= latency_val or latency_val <= 350:
				latency = f'***{latency_val}ms***'
				latency_color=0xff7100
			
			elif latency_val >= 351:
				latency = f'***{latency_val}ms***'
				latency_color=0xff0000
			
			
			embed = disnake.Embed(
				title=f'{ctx.author.name}, eu estou com {latency} de ping!',
				color=latency_color)
			embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/147/147227.png')
			
			await ctx.send(embed=embed)


def setup(bot):
		bot.add_cog(Ping(bot))
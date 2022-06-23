import os
import sys
import json
import aiohttp
import platform

import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from config import guild_ids

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.dominant_color import dominant_color


def _restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)


class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
	
	
	@commands.slash_command(name='vex')
	async def vex(self):
		pass
	
	
	@vex.sub_command(
		name='info',
		description='exibe minhas informações.')
	async def info(
		self,
		inter: ACI):
			await inter response.defer()
			
			avatar_color = self.bot.user.display_avatar.with_size(16)
			async with aiohttp.ClientSession() as session:
				async with session.get(str(avatar_color)) as resp:
					color = dominant_color(await resp.content.read())
			
			embed = EB(
				title=f'Informações de {self.bot.user.display_name}:',
				color=color)
			embed.add_field(name='Nome:', value=self.bot.user.name, inline=True)
			embed.add_field(name='ID:', value=self.bot.user.id, inline=True)
			embed.add_field(name='Hash:', value=hash(self.bot), inline=True)
			embed.add_field(name='Versão do python:', value=platform.python_version(), inline=False)
			embed.add_field(name='Sistema:', value=platform.system(), inline=False)
			embed.add_field(name='Versão da Disnake:', value=disnake.__version__, inline=False)
			embed.add_field(name='Módulos usados:', value=', '.join(open('requirements.txt', 'r').readlines()), inline=False)
			embed.set_thumbnail(url=self.bot.user.display_avatar)
			
			await inter.send(embed=embed)


def setup(bot):
	bot.add_cog(Bot(bot))
import json
import requests
from utils import dominant_color

import disnake
from disnake.ext import commands

from random import choice


class Anime(commands.Cog):
		def __init__(self, bot):
			self.bot: commands.Bot = bot
			with open('data/animes.json', 'r', encoding='utf8') as animes:
				animes = json.loads(animes.read())
			self.animes = animes
		
		
		@commands.slash_command(
			name='anime',
			description='eu envio uma foto de anime aleatória.')
		async def anime(self, ctx: disnake.ApplicationCommandInteraction):
			
			await ctx.response.defer()
			
			random_anime = choice(self.animes)
			
			get_image = requests.get(random_anime).content
			color = dominant_color(get_image)
			
			embed = disnake.Embed(color=color)
			embed.set_image(
				url=random_anime)
			await ctx.send(embed=embed)


def setup(bot):
		bot.add_cog(Anime(bot))
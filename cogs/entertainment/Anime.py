import json
import requests
from io import BytesIO

import disnake
from disnake.ext import commands

from random import choice


class Anime(commands.Cog):
    def __init__(self, bot):
    	self.bot: commands.Bot = bot
    	with open('data/animes.json', 'r', encoding='utf8') as animes:
    		animes = json.loads(animes.read())
    	self.animes = animes
    
    
    @commands.command(
    	name='anime',
    	description='*envia uma foto de anime aleatória.*',
    	aliases=[
    		'anim',
    		'animes'
    		])
    async def anime(self, ctx):
    	random_anime = choice(self.animes)
    	
    	get_image = requests.get(random_anime).content
    	img = BytesIO(get_image)
    	color_thief = ColorThief(img)
    	dominant_color = color_thief.get_color(quality=1)
    	material = ''.join(f'{i:02X}' for i in dominant_color)
    	
    	embed = disnake.Embed(color=int(material, 16))
    	embed.set_image(
    		url=random_anime)
    	await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Anime(bot))
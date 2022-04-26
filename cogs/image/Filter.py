import os
from PIL import ImageFilter, Image

import disnake
from disnake.ext import commands

from config import prefix, CERROR


class Filter(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
	@commands.command()
	async def blur(self, ctx, *, image=None):
		if image == None:
			embed = disnake.Embed(
				title='você precisa enviar uma imagem junto ao comando!',
				description='', 
				color=CERROR)
			await ctx.reply(embed=embed)
		else:
			#msg = await ctx.reply('gerando...')
			await ctx.reply(image)
			
			
			
		#file = disnake.File('data/QRcode.png')
		#os.remove('data/QRcode.png')
		
		#await msg.edit(content='', embed=embed)
		
		
def setup(bot):
    bot.add_cog(Filter(bot))
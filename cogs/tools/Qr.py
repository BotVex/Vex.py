import os
import qrcode

import disnake
from disnake.ext import commands

from config import prefix, CERROR
from asyncio import sleep


class QR(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
	@commands.slash_command(
		name='qrtxt',
		description=f'eu gero um QRcode através do texto que você me mandar :O')
	async def qrtxt(self, ctx: disnake.ApplicationCommandInteraction, *, text: str):
		await ctx.response.defer()
			
		QR = qrcode.make(str(text))
		QR.save('data/QRcode.png')
		file = disnake.File('data/QRcode.png')
		os.remove('data/QRcode.png')
		
		embed = disnake.Embed(
			description=f'**{str(text)}**',
			color=0xFFFFFF)
		embed.set_image(file=file)
		await ctx.edit_original_message(content='', embed=embed)
		
		
def setup(bot):
    bot.add_cog(QR(bot))
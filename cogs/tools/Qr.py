import os
import qrcode

import disnake
from disnake.ext import commands

from config import prefix, CERROR
from asyncio import sleep


class QR(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
	@commands.command(
		name='qrtxt',
		description=f'*eu gero um QRcode através do texto que você me mandar :O*\n`EX: {prefix}qrtxt melancia gamer`',
		aliases=[
			'qr',
			'qrcode'
			])
	async def qrtxt(self, ctx, *, text=None):
		if text == None:
			embed = disnake.Embed(
				title='você precisa informar um texto!',
				description=f'EX: `{prefix}qrtxt texto legal`', 
				color=CERROR)
			await ctx.reply(embed=embed)
		else:
			embed = disnake.Embed(
				title='',
				description='')
			embed.set_author(name='gerando...', icon_url='https://media.discordapp.net/attachments/965785255321681960/967475227149865010/output-onlinegiftools.gif')
			msg = await ctx.reply(embed=embed)
			QR = qrcode.make(str(text))
			QR.save('data/QRcode.png')
		file = disnake.File('data/QRcode.png')
		os.remove('data/QRcode.png')
		
		embed = disnake.Embed(
			title='',
			description=f'**{str(text)}**',
			color=0xFFFFFF)
		embed.set_image(file=file)
		await sleep(1)
		await msg.edit(content='', embed=embed)
		
		
def setup(bot):
    bot.add_cog(QR(bot))
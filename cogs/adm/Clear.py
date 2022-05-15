import json
from random import choice

import disnake
from disnake.ext import commands


class Clear(commands.Cog):
		def __init__(self, bot):
			self.bot: commands.Bot = bot
		
		
		@commands.slash_command(
			name='clear',
			description='apago uma quantidade específica de mensagens.')
		@commands.has_permissions(manage_messages=True) 
		async def clear(self, inter: disnake.ApplicationCommandInteraction, amount: int):
			await inter.response.defer()
			
			if amount >= 2001:
				embed = disnake.Embed(title='<:svTick_Nao:975225649029578782> | eu posso limpar até 2000 mensagens!')
				await inter.send(embed=embed)
				return
			else:
				try:
					await inter.channel.purge(limit=amount)
					#embed = disnake.Embed(title=f'<:svTick_sim:975225579479646258> | {amount} mensagens apagadas!')
					#await inter.send(embed=embed, ephemeral=True, delete_after=30)
				except:
					pass

def setup(bot):
		bot.add_cog(Clear(bot))
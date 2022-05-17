import os
import sys
import json

import disnake
from disnake.ext import commands
EB = disnake.Embed


from config import CDEFAULT, extensions
import requests 


def _restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	#setavatar
	@commands.slash_command(
		description='owner command', 
		guild_ids=[957509903273046067])
	@commands.is_owner()
	async def setavatar(self, inter: disnake.ApplicationCommandInteraction, avatar: disnake.Attachment):
		await inter.response.defer()
		
		try:
			await self.bot.user.edit(avatar=await avatar.read())
			await inter.send(embed=EB(title='<:svTick_sim:975225579479646258> | avatar alterado!'))
		except:
			await inter.send(embed=EB(title=f'<:svTick_Nao:975225649029578782> | falha ao alterar o avatar'))
	
	
	#restart
	@commands.slash_command(
		description='owner command', 
		guild_ids=[957509903273046067])
	@commands.is_owner()
	async def restart(self, inter: disnake.ApplicationCommandInteraction):
		await inter.response.defer()
		
		await inter.send('<:svTick_sim:975225579479646258>')
		_restart()
	
	
	#load
	@commands.slash_command(
		description='owner command', 
		guild_ids=[957509903273046067])
	@commands.is_owner()
	async def load(self, inter: disnake.ApplicationCommandInteraction, cog: str):
		await inter.response.defer()
		
		self.bot.load_extension(cog)
		
		await inter.send(embed=EB(title=f'<:svTick_sim:975225579479646258> | a cog {cog} foi carregada'))


	@load.autocomplete('cog')
	async def cog_list(self, inter: disnake.ApplicationCommandInteraction, string: str):
		return extensions
	
	
	#unload
	@commands.slash_command(
		description='owner command', 
		guild_ids=[957509903273046067])
	@commands.is_owner()
	async def unload(self, inter: disnake.ApplicationCommandInteraction, cog: str):
		await inter.response.defer()
		
		self.bot.unload_extension(cog)
		
		await inter.send(embed=EB(title=f'<:svTick_sim:975225579479646258> | a cog {cog} foi descarregada'))


	@unload.autocomplete('cog')
	async def cog_list(self, inter: disnake.ApplicationCommandInteraction, string: str):
		return extensions
	
	
	#reload
	@commands.slash_command(
		description='owner command', 
		guild_ids=[957509903273046067])
	@commands.is_owner()
	async def reload(self, inter: disnake.ApplicationCommandInteraction, cog: str):
		await inter.response.defer()
		
		self.bot.unload_extension(cog)
		self.bot.load_extension(cog)
		
		await inter.send(embed=EB(title=f'<:svTick_sim:975225579479646258> | a cog {cog} foi recarregada'))


	@reload.autocomplete('cog')
	async def cog_list(self, inter: disnake.ApplicationCommandInteraction, string: str):
		return extensions
	
	
	
def setup(bot):
    bot.add_cog(Owner(bot))
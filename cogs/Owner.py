import os
import sys
import json

import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from config import extensions
import requests 

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils import dominant_color


def _restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(name='owner')
	async def owner(self, inter: ACI):
		pass
	
	
	@owner.sub_command_group(name='set')
	async def set(self, inter: ACI):
		pass
	
	
	@owner.sub_command_group(name='cog')
	async def cog(self, inter: ACI):
		pass
	
	
	#setavatar
	@set.sub_command(
		name='avatar',
		description='alterar avatar.', 
		guild_ids=[957509903273046067],
		options=[
			disnake.Option(
				name='file',
				description='envie uma mídia.',
				type=disnake.OptionType.attachment,
				required=True
				)
			])
	@commands.is_owner()
	async def avatar(
		self, 
		inter: ACI, 
		file: disnake.Attachment):
		await inter.response.defer()
		
		
		try:
			await self.bot.user.edit(avatar=await file.read())
			await inter.send(embed=EB(title='<:svTick_sim:975225579479646258> | avatar alterado!'))
		except:
			await inter.send(embed=EB(title=f'<:svTick_Nao:975225649029578782> | falha ao alterar o avatar'))
	
	
	
	#restart
	@owner.sub_command(
		description='owner command', 
		guild_ids=[957509903273046067])
	@commands.is_owner()
	async def restart(self, inter: disnake.ApplicationCommandInteraction):
		await inter.response.defer()
		
		await inter.send('<:svTick_sim:975225579479646258>')
		_restart()
	
	
	@owner.sub_command(
		description='owner command', 
		guild_ids=[957509903273046067])
	@commands.is_owner()
	async def push(self, inter: disnake.ApplicationCommandInteraction, commit_text: str='a'):
		await inter.response.defer()
		
		try:
			os.system(f'git add . && git commit -am "{commit_text}" && git push heroku master')
			await inter.send('susseso')
			os.system('^Z')
		except:
			await inter.send('erro')
	
	#load
	@cog.sub_command(
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
	@cog.sub_command(
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
	@cog.sub_command(
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
import os
import sys
import json
from asyncio import sleep

from rich.console import Console
log = Console().log

import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.newassets import Colors as C

from config import GUILD_ID


def _restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.is_owner()
	@commands.slash_command(name='owner', guild_id=GUILD_ID)
	async def owner(self, inter: ACI):
		pass
	
	
	@owner.sub_command_group(name='set', guild_id=GUILD_ID)
	async def set(self, inter: ACI):
		pass
	

	@owner.sub_command_group(name='cog', guild_id=GUILD_ID)
	async def cog(self, inter: ACI):
		pass
	
	
	#restart
	@owner.sub_command(
		name='restart',
		description=f'Reinicia o bot.', 
		guild_id=GUILD_ID)
	async def restart(self, inter: ACI):
		await inter.send('Reiniciando...', ephemeral=True)
		_restart()


	#load
	@cog.sub_command(
		name='load',
		description=f'Carrega uma cog.',
		options=[
			disnake.Option(
				name='cog',
				description='Selecione uma cog.',
				type=disnake.OptionType.string,
				required=True,
				choices=[
					disnake.OptionChoice('Events', 'Events'),
					disnake.OptionChoice('Tools', 'Tools'),
					disnake.OptionChoice('Entertaiment', 'Entertaiment'),
					disnake.OptionChoice('Administration', 'Administration'),
					disnake.OptionChoice('ContextMenus', 'ContextMenus')]
				)
			]
		)
	async def load(self, inter: ACI, cog: str):
		await inter.response.defer()
		
		try:
			self.bot.load_extension(f'cogs.{cog}')
		
			embed = EB(color=C.SUCCESS)
			embed.title = 'Cog carregada!'
			embed.description = f'A cog `{cog}` foi carregada com sucesso!'
			await inter.send(embed=embed, ephemeral=True)
			return
		
		except Exception as e:
			embed = EB(color=C.ERROR)
			embed.title = 'Cog não recarregada!'
			embed.description = f'Não foi possível recarregar a cog `{cog}`!\n\n```py\n{e}```'
			await inter.send(embed=embed, ephemeral=True)
			return
		

	#reload
	@cog.sub_command(
		name='reload',
		description=f'Recarrega uma cog.',
		options=[
			disnake.Option(
				name='cog',
				description='Selecione uma cog.',
				type=disnake.OptionType.string,
				required=True,
				choices=[
					disnake.OptionChoice('Events', 'Events'),
					disnake.OptionChoice('Tools', 'Tools'),
					disnake.OptionChoice('Entertaiment', 'Entertaiment'),
					disnake.OptionChoice('Administration', 'Administration'),
					disnake.OptionChoice('ContextMenus', 'ContextMenus')]
				)
			]
		)
	async def reload(self, inter: ACI, cog: str):
		await inter.response.defer()
		
		try:
			self.bot.unload_extension(f'cogs.{cog}')
			self.bot.load_extension(f'cogs.{cog}')
		
			embed = EB(color=C.SUCCESS)
			embed.title = 'Cog recarregada!'
			embed.description = f'A cog `{cog}` foi recarregada com sucesso!'
			await inter.send(embed=embed, ephemeral=True)
			return
		
		except Exception as e:
			embed = EB(color=C.ERROR)
			embed.title = 'Cog não recarregada!'
			embed.description = f'Não foi possível recarregar a cog `{cog}`!\n\n```py\n{e}```'
			await inter.send(embed=embed, ephemeral=True)
			return
		

def setup(bot):
	bot.add_cog(Owner(bot))



"""	
	#load
	@cog.sub_command(
		description=f'{E.owner}Loads a specific bot cog.', 
		guild_id=guild_id,
		options=[
			disnake.Option(
				name='cog',
				description='Select a cog to load.',
				type=disnake.OptionType.string,
				required=True
				)
			])
	@commands.is_owner()
	async def load(
		self, 
		inter: ACI, 
		cog: str):
		await inter.response.defer()
		
		try:
			self.bot.load_extension(cog)
		
			embed = EB(
				title=f'{E.success}Cog carregada!',
				description=f'A cog `{cog}` foi carregada com sucesso!',
				color=C.success)
		except:
			embed = EB(
				title=f'{E.error}Cog não carregada!',
				description=f'Não foi possível carregar a cog `{cog}`!',
				color=C.error)
		
		await inter.send(embed=embed)


	@load.autocomplete('cog')
	async def cog_list(self, inter: disnake.ApplicationCommandInteraction, string: str):
		
		extensions_list = []
		for extension_file in os.listdir('./cogs'):
			if extension_file.endswith('.py'):
				extensions_list.append(extension_file[:-3])
		
		return extensions_list.sort()
	
	
	#unload
	@cog.sub_command(
		description=f'{E.owner}Unloads a specific bot cog.', 
		guild_id=guild_id,
		options=[
			disnake.Option(
				name='cog',
				description='Select a cog to unload.',
				type=disnake.OptionType.string,
				required=True
				)
			])
	@commands.is_owner()
	async def unload(
		self, 
		inter: ACI, 
		cog: str):
		await inter.response.defer()
		
		try:
			self.bot.unload_extension(cog)
		
			embed = EB(
				title=f'{E.success}Cog descarregada!',
				description=f'A cog `{cog}` foi descarregada com sucesso!',
				color=C.success)
		except:
			embed = EB(
				title=f'{E.error}Cog não descarregada!',
				description=f'Não foi possível descarregar a cog `{cog}`!',
				color=C.error)
		
		await inter.send(embed=embed)
	
	
	@unload.autocomplete('cog')
	async def cog_list(self, inter: disnake.ApplicationCommandInteraction, string: str):
		
		extensions_list = []
		for extension_file in os.listdir('./cogs'):
			if extension_file.endswith('.py'):
				extensions_list.append(extension_file[:-3])
		
		return extensions_list.sort()
"""
	
import os
import sys
import json
import requests 

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


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(name='owner', guild_ids=guild_ids)
	async def owner(self, inter: ACI):
		pass
	
	
	@owner.sub_command_group(name='set', guild_ids=guild_ids)
	async def set(self, inter: ACI):
		pass
	
	
	@owner.sub_command_group(name='cog', guild_ids=guild_ids)
	async def cog(self, inter: ACI):
		pass
	
	
	#setavatar
	@set.sub_command(
		name='avatar', 
		description=f'{E.owner}Changes bot avatar.', 
		guild_ids=guild_ids,
		options=[
			disnake.Option(
				name='file',
				description='Envie uma imagem.',
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
			
			embed = EB(
				title=f'{E.success}Avatar alterado!',
				color=C.success)
			
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error}Falha ao alterar o avatar.',
				description='Verifique se a mídia é uma imagem e de está nas proporções corretas.',
				color=C.error)
			await inter.send(embed=embed)
	
	
	#setstatus
	@set.sub_command(
		name='status', 
		description=f'{E.owner}Changes bot status.', 
		guild_ids=guild_ids,
		options=[
			disnake.Option(
				name='status',
				description='Escreva uma mensagem.',
				type=disnake.OptionType.string,
				required=False
				)
			])
	@commands.is_owner()
	async def status(
		self, 
		inter: ACI, 
		status: str=None):
		await inter.response.defer()
		if status == None:
			status = 'Made by: 🐺'
		try:
			await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.streaming, name=status))
			
			embed = EB(
				title=f'{E.success}Status alterado!',
				color=C.success)
			
			await inter.send(embed=embed)
		except:
			embed = EB(
				title=f'{E.error}Falha ao alterar o Status.',
				description='',
				color=C.error)
			await inter.send(embed=embed)
	
	
	#restart
	@owner.sub_command(
		description=f'{E.owner}Restart the bot', 
		guild_ids=guild_ids)
	@commands.is_owner()
	async def restart(
		self, 
	inter: ACI):
		await inter.response.defer()
		
		await inter.send('restarting...')
		#await msg.delete(delay=2.0)
		_restart()
	
	
	#load
	@cog.sub_command(
		description=f'{E.owner}Loads a specific bot cog.', 
		guild_ids=guild_ids,
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
		guild_ids=guild_ids,
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
	
	
	#reload
	@cog.sub_command(
		description=f'{E.owner}Reloads a specific bot cog.', 
		guild_ids=guild_ids,
		options=[
			disnake.Option(
				name='cog',
				description='Select a cog to reload.',
				type=disnake.OptionType.string,
				required=True
				)
			])
	@commands.is_owner()
	async def reload(
		self, 
		inter: ACI, 
		cog: str):
		await inter.response.defer()
		
		try:
			self.bot.unload_extension(cog)
			self.bot.load_extension(cog)
		
			embed = EB(
				title=f'{E.success}Cog recarregada!',
				description=f'A cog `{cog}` foi recarregada com sucesso!',
				color=C.success)
		except:
			embed = EB(
				title=f'{E.error}Cog não recarregada!',
				description=f'Não foi possível recarregar a cog `{cog}`!',
				color=C.error)
		
		await inter.send(embed=embed)
	
	
	@reload.autocomplete('cog')
	async def cog_list(self, inter: disnake.ApplicationCommandInteraction, string: str):
		
		extensions_list = []
		for extension_file in os.listdir('./cogs'):
			if extension_file.endswith('.py'):
				extensions_list.append(extension_file[:-3])
		
		return extensions_list.sort()
	


def setup(bot):
	bot.add_cog(Owner(bot))
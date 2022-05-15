import os
from datetime import datetime

import disnake
from disnake.ext import commands

from config import *
from utils.paginator import EmbedPaginator

class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
		
	
	@commands.slash_command(
		name='help',
		description='exibe a lista de comandos.')
	async def help(self, ctx: disnake.ApplicationCommandInteraction):
		page1_commands = ['help', 'ping']
		page2_commands = ['color', 'qrtxt']
		page3_commands = ['anime', 'mojis', 'owo', 'rg']
		page4_commands = ['contraste', 'equalizar', 'espelhar', 'flip', 'gray', 'inverter', 'posterizar', 'solarizar', 'nitidez']
		
		#page1
		page1 = disnake.Embed(
			description='meus comandos simples e essenciais!',
			timestamp=datetime.now())
		page1.set_author(
			name = 'Comandos Básicos:',
			icon_url='https://images.emojiterra.com/google/android-11/512px/1f916.png')
		
		for command in page1_commands: 
			page1.add_field(
				f'/{self.bot.get_slash_command(command).name}',
				value=f'{self.bot.get_slash_command(command).description}**\n **', inline=True)
		
		#page2
		page2 = disnake.Embed(
			description='algumas feramentas simples que podem te ajudar!')
		page2.set_author(
			name = 'Ferramentas:',
			icon_url='https://images.emojiterra.com/google/noto-emoji/v2.034/128px/1f6e0.png')
		
		for command in page2_commands: 
			page2.add_field(
				f'/{self.bot.get_slash_command(command).name}',
				value=f'{self.bot.get_slash_command(command).description}**\n **', inline=True)
		
		#page3
		page3 = disnake.Embed(
			description='comandos para você passar o tempo <:cat_foda:945710595414569052>')
		page3.set_author(
			name = 'Entretenimento:',
			icon_url='https://images.emojiterra.com/google/noto-emoji/v2.034/128px/1fa80.png')
		
		for command in page3_commands: 
			page3.add_field(
				f'/{self.bot.get_slash_command(command).name}',
				value=f'{self.bot.get_slash_command(command).description}**\n **', inline=True)
		
		#page4
		"""
		page4 = disnake.Embed(
			description='comandos para você usar com imagens :camera:')
		page4.set_author(
			name = 'Imagems:',
			icon_url='https://images.emojiterra.com/google/noto-emoji/v2.034/128px/1f5bc.png')
		
		for command in page4_commands: 
			page4.add_field(
				f'/{self.bot.get_slash_command(command).name}',
				value=f'{self.bot.get_slash_command(command).description}**\n **', inline=True)
		"""
		embeds_list = [page1, page2, page3] #page4]
		await EmbedPaginator(ctx, embeds=embeds_list, timeout=40).start()

def setup(bot):
	bot.add_cog(Bot(bot))
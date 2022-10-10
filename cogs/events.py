import json
import datetime
from time import time
from random import choice

from rich.console import Console
log = Console().log

import disnake
from disnake.ext import commands, tasks
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.newassets import DefaultColors, GetColor, Icons


class Events(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
		self.bot.start_time = time() 
		
		with open('data/games.json') as games:
			self.game_list = json.loads(games.read())
	
	
	@commands.Cog.listener()
	async def on_connect(self):
		log('connected in Discord')

		#TODO: essa parada ta definndo a cor a cada shard, depois tem que resolver
		bot_avatar = self.bot.user.display_avatar.with_size(16)
		
		self.bot.default_color = await GetColor.general_color_url(bot_avatar)
		log(f'default color is defined to {self.bot.default_color}')


	@commands.Cog.listener()
	async def on_disconnect(self):
		log('disconnected of Discord')


	@commands.Cog.listener()
	async def on_resumed(self):
		log('resumed section')


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == self.bot.user.id or message.author.bot is True:
			return
		else:
			mentions = message.mentions
			if len(mentions) != 0:
				for mentioned in mentions:
					if mentioned.id == self.bot.user.id:
						embed = EB(color=self.bot.default_color)
						embed.title = f':wave: Olá {message.author.name}'
						embed.description = f'Meu nome é **{self.bot.user.name}**!\n\nSou um bot de **entretenimento** ~~e **manipulação de imagem**~~ que está em desenvolvimento.\n\nPara utilizar meus comandos, utilize [comandos de barra ( / )](https://discord.com/blog/welcome-to-the-new-era-of-discord-apps).'
						embed.timestamp = datetime.datetime.now()
						embed.set_footer(text=message.author.display_name, icon_url=message.author.display_avatar)
						
						await message.reply(embed=embed)
						break


	@tasks.loop(minutes=10.0)
	async def status_task(self):
		
		for shard_id in [x for x in self.bot.shards]:
			activity_type = disnake.ActivityType.playing
			activity_name = f'{choice(self.game_list)} [{shard_id+1}]'
		
			await self.bot.change_presence(
				status=disnake.Status.idle,
				activity=disnake.Activity(
					type=activity_type, 
					name=activity_name, 
					shard_id=shard_id
					)
				)
	

	@commands.Cog.listener()
	async def on_ready(self):
		log(f'{self.bot.user} online')
		
		if self.status_task.is_running():
			log('status task was already running')
		else:
			self.status_task.start()
			log('status task started')


def setup(bot):
	bot.add_cog(Events(bot))

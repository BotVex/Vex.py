import json
import datetime
from time import time
from random import choice
from aiohttp import ClientSession

from rich.console import Console
log = Console().log
rprint = Console().print

import disnake
from disnake.ext import commands, tasks
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.newassets import GetColor


class Events(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
		self.bot.start_time = time()


	@tasks.loop(minutes=30.0)
	async def default_color_task(self):
		self.bot.default_color = await GetColor.general_color_url(self.bot.user.display_avatar.with_size(16))
		log(f'[bright_black]default color is defined to {self.bot.default_color}[/]')


	@tasks.loop(minutes=30.0)
	async def get_github_information_task(self):
		async with ClientSession() as session:
			async with session.get('https://api.github.com/repos/BotVex/vex.py') as response_repo:
				response_repo = await response_repo.json()
			
			async with session.get('https://api.github.com/repos/BotVex/vex.py/commits/main') as response_commit:
				response_commit = await response_commit.json()

				self.bot.github = {
					"repo_forks":response_repo["forks_count"],
					"repo_issues":response_repo["open_issues_count"],
					"repo_stars":response_repo["stargazers_count"],
					"repo_name":response_repo["name"],
					"repo_desc":response_repo["description"],
					"repo_url":response_repo["html_url"],
					"repo_topics":response_repo["topics"],
					"repo_last_commit":{
						"message":response_commit["commit"]["message"],
						"url":response_commit["html_url"]
					}
				}

				log(f'[bright_black]information from Github was obtained[/]')


	@commands.Cog.listener()
	async def on_connect(self):
		if self.get_github_information_task.is_running():
			pass
		else:
			self.get_github_information_task.start()
			log('[grey85]trying to get the information from github[/]')

		if self.default_color_task.is_running():
			pass
		else:
			self.default_color_task.start()
			log('[grey85]defalt color task started[/]')
		
		log('[grey85]connected in Discord[/]')


	@commands.Cog.listener()
	async def on_disconnect(self):
		log('[grey85]disconnected of Discord[/]')


	@commands.Cog.listener()
	async def on_resumed(self):
		log('[grey85]resumed section[/]')


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
						embed.description = f'Meu nome é **{self.bot.user.name}**!\n\nSou um bot de **entretenimento** e ~~**manipulação de imagem**~~ que está em desenvolvimento.\n\nPara utilizar meus comandos, utilize [comandos de barra ( / )](https://discord.com/blog/welcome-to-the-new-era-of-discord-apps).'
						embed.set_thumbnail(url=self.bot.user.display_avatar.url)
						embed.timestamp = datetime.datetime.now()
						embed.set_footer(text=message.author.display_name, icon_url=message.author.display_avatar)
						
						try:
							await message.reply(embed=embed)

						except:
							pass

						break


	@tasks.loop(minutes=10.0)
	async def status_task(self):
		with open('data/games.json') as games:
			game_list = json.loads(games.read())
		
		game = choice(game_list)

		for shard_id in [x for x in self.bot.shards]:
			activity_type = disnake.ActivityType.playing
			activity_name = f'{game} [{shard_id+1}]'
		
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
		log('[bright_black]client online[/]')
		rprint(f'[cyan1]{self.bot.user}[/] [bold green]online[/] | [yellow1]{len(self.bot.guilds)} servers[/]')
		
		if self.status_task.is_running():
			log('[bright_black]status task was already running[/]')
		else:
			self.status_task.start()
			log('[grey85]status task started[/]')


def setup(bot):
	bot.add_cog(Events(bot))

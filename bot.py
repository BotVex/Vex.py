import os
from datetime import timedelta
import time

import disnake
from disnake.ext import commands, tasks
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.assets import MediaUrl
import config

from rich.console import Console
CO = Console()

os.system('clear')


bot = commands.AutoShardedInteractionBot(
#bot = commands.InteractionBot(
	#shard_count=2,
	intents							= config.intents,
	help_command				= None,
	sync_commands_debug	= True,
	#sync_permissions		= True,
	case_insensitive		= True,
	owner_ids						= config.owner_ids,
	reload							= True,
	strict_localization = True,
	chunk_guilds_at_startup=False)

#bot.i18n.load("./locale")
#print('locales loaded')

@commands.Cog.listener()
async def on_ready():
	CO.print(f'\n[orange_red1]{bot.user}[/] [green]online[/]')
	status_task.start()
	CO.print('[green]status task started[/]')
	channel = bot.get_channel(987899340293038130)
	await channel.send('online')


@tasks.loop(minutes=1.0)
async def status_task():
	#shard_ids = [for x in bot.shard_count - 1]
	for guild in bot.guilds:
		await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.streaming, name=''))
		
		#f'Shard: {self.bot.get_shard(guild.shard_id).id} | Latency: {int(round(self.bot.get_shard(guild.shard_id).latency, 2)*1000)}ms'), shard_id=guild.shard_id)

c = 0
if __name__ == '__main__':
	CO.print(f'\n[red]COGS TO LOAD:[/]')
	for extension in config.extensions:
		bot.load_extension(extension)
		CO.print(f'  [cyan]{c}[/] [yellow]:[/]  [green]{extension}[/]')
		c += 1

CO.print(f'\n[red]DISNAKE:[/]')

"""
@bot.event
async def on_shard_connect(bot, shard_id):
    print(f"shard {shard_id} connected")

@bot.event
async def on_shard_disconnect(bot, shard_id):
    print(f"shard {shard_id} disconnected")

@bot.event
async def on_shard_resumed(bot, shard_id):
    print(f"shard {shard_id} resumed")

@bot.event
async def on_shard_ready(bot, shard_id):
	print(f"shard {shard_id} ready")
"""

bot.run(config.TOKEN)

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
	shard_count=1,
	intents=config.intents,
	help_command=None,
	sync_commands_debug=True,
	case_insensitive=True,
	owner_ids=config.owner_ids,
	reload=True,
	strict_localization=True,
	chunk_guilds_at_startup=False)

#bot.i18n.load("./locale") #Discord is not supported yet
#print('locales loaded')

@bot.event
async def on_ready():
	CO.print(f'\n[orange_red1]{bot.user}[/] [green]online[/]')
	status_task.start()
	CO.print('[green]status task started[/]')
	#channel = bot.get_channel(987899340293038130)
	#await channel.send('online')



@tasks.loop(minutes=1.0)
async def status_task():
	shard_ids = []
	for guild in bot.guilds:
		shard_ids.append(guild.shard_id)
	shard_ids = sorted(set(shard_ids))
	for shard_id in shard_ids:
		print(f'shard: {shard_id}')
		await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.streaming, name=f'Shard: {bot.get_shard(guild.shard_id).id} | Latency: ~{int(round(bot.get_shard(guild.shard_id).latency, 2)*1000)}ms'), shard_id=shard_id)
		
		

c = 0
if __name__ == '__main__':
	CO.print(f'\n[red]COGS TO LOAD:[/]')
	for extension in config.extensions:
		bot.load_extension(extension)
		CO.print(f'  [cyan]{c}[/] [yellow]:[/]  [green]{extension}[/]')
		c += 1

CO.print(f'\n[red]DISNAKE:[/]')


bot.run("ODI3NjEwMTk3MjQ1MTY1NTc4.GgYMct.7ApKgXz8_cBQQCfVjsCR2gqioPVbejtJ7OY968") #config.TOKEN)

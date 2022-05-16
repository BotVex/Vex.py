import os

import disnake
from disnake.ext import commands, tasks

import config

os.system('clear')

bot = commands.InteractionBot(
  command_prefix       = config.prefix,
  intents              = config.intents,
  help_command         = None,
  sync_commands_debug  = True,
  sync_permissions     = True,
  case_insensitive     = True,
  owner_ids            = config.owner_ids,
  reload               = True)
  #test_guilds=[957509903273046067])



@bot.event
async def on_ready():
	print(f'{bot.user} online')
	status_task.start()
	print('status task started')
	channel = bot.get_channel(967464232021020683)
	await channel.send('online')


@tasks.loop(seconds=7200)
async def status_task():
	try:
		await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.streaming, name=config.get_game()))
		print('changed status task')
	except RuntimeError:
		print('runtime error - retry')
		await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.streaming, name=config.get_game()))
  	
 
 

if __name__ == '__main__':
  for extension in config.extensions:
    bot.load_extension(extension)
    print(f'{extension} loaded')


bot.run(config.TOKEN)
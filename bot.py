import os

import disnake
from disnake.ext import commands, tasks

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.assets import MediaUrl
from config import TOKEN, OWNER_ID, INTENTS, EXTENSIONS


bot = commands.AutoShardedInteractionBot(
	shard_count=1,
	intents=INTENTS,
	help_command=None,
	sync_commands_debug=True,
	case_insensitive=True,
	owner_id=OWNER_ID,
	reload=False,
	strict_localization=True,
	chunk_guilds_at_startup=False)


@bot.event
async def on_ready():
	print(f'\n{bot.user} online')
	try:
		status_task.start()
		print('status task started')
	except Exception as e:
		print(f'status task failed\n{e}')


@tasks.loop(minutes=5.0)
async def status_task():
	humans = []
	for user in bot.users:
		if user.bot:
			pass
		else:
			humans.append(user)
	
	shard_ids = []
	for guild in bot.guilds:
		shard_ids.append(guild.shard_id)
	shard_ids = sorted(set(shard_ids))
	
	for shard_id in shard_ids:
		await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name=f'{len(bot.guilds)} Servers | {len(humans)} Humans', shard_id=shard_id))
	

c = 0
if __name__ == '__main__':
	bot.i18n.load("locale/")
	print('locales loaded')

	print(f'\nCOGS TO LOAD:')
	for extension in EXTENSIONS:
		bot.load_extension(extension)
		print(f'  {c}:  {extension}')
		c += 1

print(f'\nDISNAKE:')

bot.run(TOKEN)

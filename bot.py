from rich.console import Console
log = Console().log

import disnake
from disnake import Intents
from disnake.ext import commands

from config import TOKEN, OWNER_ID, EXTENSIONS


log(f'[bright_black]Disnake version: {disnake.__version__}[/]')

INTENTS = Intents(
	guilds=True,
	members=True,
	bans=True,
	emojis_and_stickers=True,
	integrations=False,
	webhooks=False,
	invites=False,
	voice_states=True,
	presences=False,
	messages=True,
	message_content=False,
	reactions=True,
	typing=True,
	guild_scheduled_events=False
)
#https://docs.disnake.dev/en/stable/api.html?highlight=intents#disnake.Intents

COMMAND_SYNC_FLAGS = commands.CommandSyncFlags(
	allow_command_deletion=True, 
	sync_global_commands=True,
	sync_guild_commands=True,
	sync_commands_debug=True,
	sync_on_cog_actions=True,
)
#https://docs.disnake.dev/en/v2.7.0/ext/commands/api.html#disnake.ext.commands.CommandSyncFlags.allow_command_deletion


bot = commands.AutoShardedInteractionBot(
	shard_count=2,
	intents=INTENTS,
	command_sync_flags=COMMAND_SYNC_FLAGS,
	owner_id=OWNER_ID,
	reload=True,
	strict_localization=True,
	chunk_guilds_at_startup=False)


if __name__ == '__main__':
	bot.i18n.load("locale/")

	#ver se da pra migrar isso pos events
	for extension in EXTENSIONS:
		extension = f'cogs.{extension.lower()}'
		bot.load_extension(extension)
		log(f'[bright_black]EXTENSION: [grey85]{extension}[/] loaded[/]')


bot.run(TOKEN)

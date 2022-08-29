from disnake import Intents 
from disnake.ext import commands

from config import TOKEN, OWNER_ID, EXTENSIONS


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


if __name__ == '__main__':
	bot.i18n.load("locale/")

	for extension in EXTENSIONS:
		bot.load_extension(extension)
		print('extension: ', extension, 'loaded')


bot.run(TOKEN)

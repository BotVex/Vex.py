from disnake import Intents
from disnake.ext import commands

from .logger import log

from .config import OWNER_ID, EXTENSIONS, TOKEN


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
    guild_scheduled_events=False,
)
# https://docs.disnake.dev/en/stable/api.html?highlight=intents#disnake.Intents

COMMAND_SYNC_FLAGS = commands.CommandSyncFlags(
    allow_command_deletion=True,
    sync_global_commands=True,
    sync_guild_commands=True,
    sync_commands_debug=False,
    sync_on_cog_actions=True,
)
# https://docs.disnake.dev/en/v2.7.0/ext/commands/api.html#disnake.ext.commands.CommandSyncFlags.allow_command_deletion


class Bot(commands.AutoShardedInteractionBot):
    def __init__(self):
        super().__init__(
            shard_count=2,
            intents=INTENTS,
            command_sync_flags=COMMAND_SYNC_FLAGS,
            owner_id=OWNER_ID,
            reload=True,
            strict_localization=True,
            chunk_guilds_at_startup=False,
        )

    def setup(self) -> None:
        try:
            log.info("loading locales...")
            self.i18n.load("src/locale/")
            log.info("locales loaded!")
        except Exception as e:
            log.error(f"falied to load locales: \n{e}")

        def load_extensions(extensions: list) -> None:
            for extension in extensions:
                try:
                    self.load_extension(f"src.cogs.{extension}")
                    log.info(f"\tEXTENSION: [slate_blue1]{extension}[/] loaded!")
                except Exception as e:
                    pass
                    log.error(f"[red1]EXTENSION: [b]{extension}[/] falied[/]\n{e}")
            log.info("all extensions loaded!")

        log.info("loading extensions...")
        load_extensions(EXTENSIONS)

    def run(self) -> None:
        log.info("{0:=^40}".format("STARTING"))
        self.setup()
        super().run(TOKEN, reconnect=True)

import json
import datetime
from time import time
from random import choice
from aiohttp import ClientSession

from src.logger import log

import disnake
from disnake.ext import commands, tasks

EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from src.utils import GetColor, ColorConverter


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.bot.start_time = time()

    @tasks.loop(minutes=30.0)
    async def default_color_task(self):
        self.bot.default_color = await GetColor.general_color_url(
            self.bot.user.display_avatar.with_size(16)
        )

        hex_color = ColorConverter.DECIMAL2HEX(self.bot.default_color).replace(
            "0x", "#"
        )

        block = "████"

        log.info(f"default color is defined to [{hex_color}]{hex_color} | {block}")

    @tasks.loop(minutes=30.0)
    async def get_github_information_task(self):
        async with ClientSession() as session:
            async with session.get(
                "https://api.github.com/repos/BotVex/vex.py"
            ) as response_repo:
                response_repo: dict = await response_repo.json()

            async with session.get(
                "https://api.github.com/repos/BotVex/vex.py/commits/main"
            ) as response_commit:
                response_commit: dict = await response_commit.json()

                self.bot.github = {
                    "repo_forks": response_repo.get("forks_count"),
                    "repo_issues": response_repo.get("open_issues_count"),
                    "repo_stars": response_repo.get("stargazers_count"),
                    "repo_name": response_repo.get("name"),
                    "repo_desc": response_repo.get("description"),
                    "repo_url": response_repo.get("html_url"),
                    "repo_topics": response_repo.get("topics"),
                    "repo_last_commit": {
                        "message": response_commit.get("commit", {}).get("message"),
                        "url": response_commit.get("html_url"),
                    },
                }

                log.info(f"information from Github was obtained")

    @commands.Cog.listener()
    async def on_connect(self):
        for shard_id in [x for x in self.bot.shards]:
            activity_type = disnake.ActivityType.playing
            activity_name = f"Restarting... 💤"

            log.info(f"shard {shard_id} was connected in Discord")

            await self.bot.change_presence(
                status=disnake.Status.dnd,
                activity=disnake.Activity(
                    type=activity_type, name=activity_name, shard_id=shard_id
                ),
            )

            log.info(
                f"presence [slate_blue1]{activity_name}[/] defined in shard {shard_id}"
            )

        if self.get_github_information_task.is_running():
            pass
        else:
            log.info("trying to get the information from github")
            try:
                self.get_github_information_task.start()
            except Exception as e:
                log.error(f"failed to get the information from github:\n{e}")

        if self.default_color_task.is_running():
            pass
        else:
            self.default_color_task.start()
            log.info("default color task started")

    @commands.Cog.listener()
    async def on_disconnect(self):
        log.warning("disconnected of Discord")

    @commands.Cog.listener()
    async def on_resumed(self):
        log.info("resumed section")

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author.id == self.bot.user.id or message.author.bot is True:
            return
        else:
            mentions = message.mentions
            if len(mentions) != 0:
                for mentioned in mentions:
                    if mentioned.id == self.bot.user.id and message.reference is None:
                        if message.guild is not None:
                            mentioned_local = (
                                f"{message.guild.name} ({message.guild.id})"
                            )
                        else:
                            mentioned_local = "DM"

                        log.info(
                            f"[deep_pink1]{message.author}[/] ({message.author.id}) mentioned in {mentioned_local}"
                        )

                        embed = EB(color=self.bot.default_color)
                        embed.title = f":wave: Olá {message.author.name}"
                        embed.description = f"""
						Meu nome é **{self.bot.user.name}**!
						
						Sou um bot de **entretenimento** e ~~**manipulação de imagem**~~ que está em desenvolvimento.
						
						Para utilizar meus comandos, utilize [comandos de barra ( / )](https://discord.com/blog/welcome-to-the-new-era-of-discord-apps)."""

                        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
                        embed.timestamp = datetime.datetime.now()
                        embed.set_footer(
                            text=message.author.display_name,
                            icon_url=message.author.display_avatar,
                        )

                        try:
                            await message.reply(embed=embed)

                        except:
                            log.error(
                                f"falied to reply mention of {message.author} ({message.author.id})"
                            )

                        break

    @tasks.loop(minutes=10.0)
    async def status_task(self):
        with open("src/data/games.json") as games:
            game_list = await json.loads(games.read())

        game = choice(game_list)

        for shard_id in [x for x in self.bot.shards]:
            activity_type = disnake.ActivityType.playing
            activity_name = f"{game} [{shard_id+1}]"

            log.info(f"setting presence in shard {shard_id}")

            await self.bot.change_presence(
                status=disnake.Status.idle,
                activity=disnake.Activity(
                    type=activity_type, name=activity_name, shard_id=shard_id
                ),
            )

            log.info(
                f"presence [slate_blue1]{activity_name}[/] defined in shard {shard_id}"
            )

    @commands.Cog.listener()
    async def on_ready(self):
        log.info("client online")
        log.info(
            f"[cyan1]{self.bot.user}[/] [bold green]online[/] - [yellow1]{len(self.bot.guilds)} guilds[/]"
        )

        if self.status_task.is_running():
            pass
        else:
            self.status_task.start()
            log.info("status task started")

    @commands.Cog.listener()
    async def on_slash_command(self, inter: ACI):
        log.info(
            f"[deep_pink1]{inter.author}[/] ({inter.author.id}) executed [dark_orange bold]/{inter.application_command.qualified_name}[/]"
        )


def setup(bot):
    bot.add_cog(Events(bot))

import datetime

import disnake
from disnake import Localized
from disnake.ext import commands

EB = disnake.Embed

from src.utils import GetColor


class CTXCMD(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.user_command(name=Localized("Avatar", key="CTXMENUS_USERCMD_AVATAR_NAME"))
    async def avatar(self, inter: disnake.UserCommandInteraction, user: disnake.User):
        color = await GetColor.general_color_url(user.display_avatar.with_size(16))

        embed = EB(color=color)
        embed.title = f":smirk_cat: Avatar de {user}"
        embed.set_image(url=user.display_avatar.url)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(
            text=inter.author.display_name, icon_url=inter.author.display_avatar
        )

        await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(CTXCMD(bot))

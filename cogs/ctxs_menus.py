import datetime

import disnake
from disnake import Localized
from disnake.ext import commands
EB = disnake.Embed

from utils.newassets import GetColor


class CTXCMD(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot

	@commands.user_command(name=Localized('Avatar', key='CTXMENUS_USERCMD_AVATAR_NAME'))
	async def avatar(self, inter: disnake.UserCommandInteraction, user: disnake.User):
		
		color = await GetColor.general_color_url(user.display_avatar.with_size(16))
		
		embed = EB(color=color)
		embed.title = f'Avatar de {user}'
		embed.set_image(url=user.display_avatar.url)
		embed.timestamp=datetime.datetime.now()
		embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

		await inter.response.send_message(embed=embed, ephemeral=True)


	@commands.has_permissions(manage_messages=True)
	@commands.bot_has_permissions(manage_messages=True)
	@commands.message_command(name=Localized('Remove reactions', key='CTXMENUS_MSGCMD_REMOVEREACTIONS_NAME'))
	async def remove_reactions(self, inter: disnake.MessageCommandInteraction, msg: disnake.Message):
		await msg.clear_reactions()

		await inter.response.send_message('Reações removidas!', ephemeral=True)


def setup(bot):
	bot.add_cog(CTXCMD(bot))
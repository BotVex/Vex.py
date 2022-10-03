import disnake
from disnake import Localized
from disnake.ext import commands
EB = disnake.Embed

from utils.newassets import GetColor


class CTXCMD(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot

	@commands.user_command(name=Localized('Avatar', key='CTXMENUS_USERCMD_AVATAR_NAME'))
	async def avatar(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User):
		
		avatar_color = user.display_avatar.with_size(16)
		color = await GetColor.general_color_url(avatar_color)
		
		embed = EB(color=color)
		embed.title = f'Avatar de {user}'
		embed.set_image(url=user.display_avatar.url)
		await inter.response.send_message(embed=embed, ephemeral=True)


	@commands.message_command(name=Localized('ID', key='CTXMENUS_MSGCMD_ID_NAME'))
	async def _id(self, inter: disnake.ApplicationCommandInteraction, msg: disnake.Message):
		await inter.response.send_message(msg.id, ephemeral=True)


def setup(bot):
	bot.add_cog(CTXCMD(bot))
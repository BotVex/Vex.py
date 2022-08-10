import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.assets import Colors as C


class UserCMD(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 


	@commands.user_command(name="Avatar")
	async def avatar(inter: ACI, user: disnake.User):
		embed = EB(title=f'Avatar de {user}')
		embed.set_image(url=user.display_avatar.url)

		await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
	bot.add_cog(UserCMD(bot))
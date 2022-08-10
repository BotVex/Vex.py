import disnake
from disnake.ext import commands
EB = disnake.Embed
from disnake import ApplicationCommandInteraction


from utils.assets import Emojis as E
from utils.assets import Colors as C


class UserCMD(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 


	@commands.user_command(name='avatar')
	async def avatar(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User):
		embed = disnake.Embed(title=f'avatar de {user}')
		embed.set_image(url=user.display_avatar.url)
		await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
	bot.add_cog(UserCMD(bot))


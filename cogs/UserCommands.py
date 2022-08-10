import disnake
from disnake.ext import commands
EB = disnake.Embed


from utils.assets import Emojis as E
from utils.assets import Colors as C


class UserCMD(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 


	@command.user_command(name="Avatar")
	async def avatar(inter: disnake.ApplicationCommandInteraction, user: disnake.User):
		avatar = user.display_avatar
		avatar_color = avatar.with_size(16)

		async with aiohttp.ClientSession() as session:
				async with session.get(str(avatar_color)) as resp:
					color = dominant_color(await resp.content.read())
			
		embed = EB(color=color)
		embed.set_image(url=avatar)

		await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
	bot.add_cog(UserCMD(bot))


import disnake
from disnake.ext import commands
EB = disnake.Embed


from utils.assets import Emojis as E
from utils.assets import Colors as C


class CTXCMD(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 


	@commands.user_command(name="avatar")
	async def avatar(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User):
		embed = EB(title=f'avatar de {user}')
		embed.set_image(url=user.display_avatar.url)
		await inter.response.send_message(embed=embed, ephemeral=True)


	@commands.message_command(name="ID")
	async def _id(self, inter: disnake.ApplicationCommandInteraction, msg: disnake.Message):
		await inter.response.send_message(msg.id, ephemeral=True)
	

	@commands.user_command(name="Spotify")
	async def spotifysong(self, inter: disnake.CmdInter, user: disnake.Member):
			if not any(isinstance(x, disnake.Spotify) for x in list(user.activities)):
					await inter.send("Este usuário não está ouvindo músicas no Spotify.", ephemeral=True)
					return

			spotify = next((x for x in list(user.activities) if isinstance(x, disnake.Spotify)), None)

			embed = EB(
				title=spotify.title,
				description='` '.join(spotify.artists)+' `',
				color=spotify.color.value
			)
			embed.set_image(url=spotify.album_cover_url)


			class TrackLink(disnake.ui.View):
				def __init__(self):
					super().__init__()
					self.add_item(
						disnake.ui.Button(
							style=disnake.ButtonStyle.link,
							label='Link da música',
							url=spotify.track_url,
							emoji=E.spotify
						)
					)


			await inter.send(embed=embed, view=TrackLink(), ephemeral=True)
	

def setup(bot):
	bot.add_cog(CTXCMD(bot))
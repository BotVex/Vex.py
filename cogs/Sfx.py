import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.buttonLink import ButtonLink


class Sfx(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
	
	
	@commands.slash_command(
		name='sfx',
		description='Reproduz um efeito sonoro em um canal de voz.',
		options=[
					disnake.Option(
						name='sfx',
						description='Escolha um sfx.',
						type=disnake.OptionType.string,
						required=True
						)
		])
	async def sfx(
		self,
		inter: ACI,
		sfx: str):
		await inter.response.defer()
		
		await inter.send(':thumbsup:')
	
	

def setup(bot):
	bot.add_cog(Sfx(bot))

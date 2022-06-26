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
		description='(BETA) Reproduz um efeito sonoro em um canal de voz.',
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
		
		if not inter.author.voice:
			embed = EB(
				title=f'{E.error} Erro!',
				description=f'{inter.author.mention}, Você preciza se conectar em um canal de voz primeiro.',
				color=C.error)
			await inter.send(embed=embed, ephemeral=True)
			return
		
		vc_channel = inter.author.voice.channel
		
		if not inter.guild.voice_client or not inter.guild.voice_client.is_connected():
			await vc_channel.connect(timeout=30.0, reconnect=False)
			await inter.guild.voice_client.play(disnake.PCMAudio(f'data/audio/sfx/{sfx}.opus').read()
	
	
	@sfx.autocomplete('sfx')
	async def categories_(
		self, 
		inter: ACI, 
		string: str):
			return ['cavalo']
	

def setup(bot):
	bot.add_cog(Sfx(bot))

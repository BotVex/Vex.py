import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.assets import MediaUrl

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.Cog.listener()
	async def on_slash_command_error(self, inter: ACI, error: commands.CommandError):

		if isinstance(error, commands.CommandOnCooldown):
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			second = round(error.retry_after)

			if day > 0:
				waiting_time = str(day) + ' dia' if day == 1 else str(day) + ' dias'
			elif hour > 0:
				waiting_time = str(hour) + ' hora' if hour == 1 else str(hour) + ' horas'
			elif minute > 0:
				waiting_time = str(minute) + ' minuto' if minute == 1 else str(minute) + ' minutos'
			else:
				waiting_time = str(second) + ' segundo' if second <= 1 else str(second) + ' segundos'

			embed = disnake.Embed(
					title=f'{E.error}Comando em cooldown!',
					description=f'{inter.author.mention}, este comando está em cooldown, você só poderá executá-lo novamente em `{waiting_time}`.',
					color=C.error)
			embed.set_image(url=MediaUrl.commandoncooldownbanner)
			embed.set_footer(text='Você está executando comandos rapidamente!')
			await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.NotOwner):
				embed = disnake.Embed(
					title=f'{E.error}Não desenvolvedor!',
					description='Apenas pessoas especiais podem utilizar este comando.',
					color=C.error)
				embed.set_image(url=MediaUrl.notownerbanner)
				await inter.send(embed=embed, ephemeral=True)
		

		elif isinstance(error, commands.disnake.HTTPException):
				embed = disnake.Embed(
					title=f'{E.error}Erro!',
					description='Algo **extremamente** errado aconteceu :(',
					color=C.error)
				await inter.send(embed=embed, ephemeral=True)

		
		elif isinstance(error, commands.MissingPermissions):
				embed = EB(
						title=f'{E.error}Sem permissão!',
						description=f'Eu não tenho as permissões nescessárias para executar este comando!\n\n{"Você preciza das seguintes permissões: `" + ", ".join(error.missing_permissions)+"`" if len(error.missing_permissions) != 1 else "Você preciza da seguinte permissão: `" + ", ".join(error.missing_permissions)+"`"}',
						color=C.error)
				embed.set_image(url=MediaUrl.missingpermissionsbanner)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.BotMissingPermissions):
				embed = EB(
					title=f'{E.error}Não autorizado!',
						description=f'Eu não tenho as permissões nescessárias para executar este comando!\n\n{"Eu precizo das seguintes permissões: `" + ", ".join(error.missing_permissions)+"`" if len(error.missing_permissions) != 1 else "Eu precizo da seguinte permissão: `" + ", ".join(error.missing_permissions)+"`"}',
						color=C.error)
				embed.set_image(url=MediaUrl.botmissingpermissionsbanner)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.NoPrivateMessage):
				embed = EB(
					title=f'{E.error}Apenas para servidores!',
						description='Este comando só pode ser utilizado em servidores!', 
						color=C.error) 
				embed.set_image(url=MediaUrl.noprivatemessagebanner)
				await inter.send(embed=embed, ephemeral=True)
		else:
			print(error)
	
	
def setup(bot):
	bot.add_cog(Events(bot))

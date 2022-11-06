from rich.console import Console
log = Console().log

import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.newassets import DefaultColors, Icons


class Errors(commands.Cog):
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
					title='Comando em cooldown!',
					description=f'{inter.author.mention}, este comando está em cooldown, você só poderá executá-lo novamente em `{waiting_time}`.',
					color=DefaultColors.RED)
			embed.set_image(url=Icons.CMD_ON_COOLDOWN)
			embed.set_footer(text='Você está executando comandos rapidamente!')
			await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.NotOwner):
				embed = disnake.Embed(
					title='Não desenvolvedor!',
					description='Apenas pessoas especiais podem utilizar este comando.',
					color=DefaultColors.RED)
				embed.set_image(url=Icons.NOT_OWNER)
				await inter.send(embed=embed, ephemeral=True)

		
		elif isinstance(error, commands.MissingPermissions):
				embed = EB(
						title='Sem permissão!',
						description=f'Eu não tenho as permissões nescessárias para executar este comando!\n\n{"Você preciza das seguintes permissões: `" + ", ".join(error.missing_permissions)+"`" if len(error.missing_permissions) != 1 else "Você preciza da seguinte permissão: `" + ", ".join(error.missing_permissions)+"`"}',
						color=DefaultColors.RED)
				embed.set_image(url=Icons.MISSING_PERMS)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.BotMissingPermissions):
				embed = EB(
					title='Não autorizado!',
						description=f'Eu não tenho as permissões nescessárias para executar este comando!\n\n{"Eu precizo das seguintes permissões: `" + ", ".join(error.missing_permissions)+"`" if len(error.missing_permissions) != 1 else "Eu precizo da seguinte permissão: `" + ", ".join(error.missing_permissions)+"`"}',
						color=DefaultColors.RED)
				embed.set_image(url=Icons.BOT_MISSING_PERMS)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.NoPrivateMessage):
				embed = EB(
					title='Apenas para servidores!',
						description='Este comando só pode ser utilizado em servidores!', 
						color=DefaultColors.RED) 
				embed.set_image(url=Icons.NO_PRIVATE_MSG)
				await inter.send(embed=embed, ephemeral=True)
		else:
			log(error)
	
	
def setup(bot):
	bot.add_cog(Errors(bot))

import disnake
from disnake.ext import commands, tasks
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.assets import MediaUrl

from datetime import timedelta

from rich.console import Console
CO = Console()


class Events(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.Cog.listener()
	async def on_ready(self):
		CO.print(f'\n[orange_red1]{self.bot.user}[/] [green]online[/]')
		status_task.start()
		CO.print('[green]status task started[/]')
		channel = self.bot.get_channel(987899340293038130)
		await channel.send('online')
	
	
	@tasks.loop(minutes=1.0)
	async def status_task(self):
		#shard_ids = [for x in bot.shard_count - 1]
		#print(shard_ids)
		for guild in self.bot.guilds:
			await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.streaming, name=f'Shard: {self.bot.get_shard(guild.shard_id).id} | Latency: {int(round(self.bot.get_shard(guild.shard_id).latency, 2)*1000)}ms'), shard_id=guild.shard_id)
		
	
	@commands.Cog.listener()
	async def on_message(self, msg: disnake.Message):
		if int(msg.channel.id) == 987899340293038130:
			await msg.delete(delay=60.0)

	
	@commands.Cog.listener()
	async def on_slash_command(self, inter: disnake.ApplicationCommandInteraction):
		try:
			CO.print(f"""
	[yellow]COMMAND:[/] [bright_magenta]{inter.data.name}[/]
	[yellow]GUILD:  [/] [bright_magenta]{inter.guild.name}[/] [orange_red1]([/][aquamarine1]{inter.guild.id}[/][orange_red1])[/]
	[yellow]AUTHOR: [/] [bright_magenta]{inter.author}[/] [orange_red1]([/][aquamarine1]{inter.author.id}[/][orange_red1])[/]""")
		except AttributeError:
			CO.print(f"""
	[yellow]COMMAND:[/] [bright_magenta]{inter.data.name}[/]
	[yellow]DM COMMAND[/]
	[yellow]AUTHOR: [/] [bright_magenta]{inter.author}[/] [orange_red1]([/][aquamarine1]{inter.author.id}[/][orange_red1])[/]""")
	
	
	@commands.Cog.listener()
	async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, error: Exception):
		if isinstance(error, commands.CommandOnCooldown):
				embed = disnake.Embed(
					title=f'{E.error}Comando em cooldown!',
					description=f'<@{inter.author.id}>, este comando está em cooldown, você só poderá executá-lo novamente em `{str(timedelta(seconds=error.retry_after)).split(".")[0]}`.',
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
		
		
		elif isinstance(error, commands.errors.MissingPermissions):
				embed = EB(
						title=f'{E.error}Sem permissão!',
						description='Você não tem as permissões nescessárias para executar este comando!\n\nVocê preciza das seguintes permissões: `' + ', '.join(error.missing_permissions)+'`',
						color=C.error)
				embed.set_image(url=MediaUrl.missingpermissionsbanner)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.errors.BotMissingPermissions):
				embed = EB(
					title=f'{E.error}Não autorizado!',
						description='Eu não tenho as permissões nescessárias para executar este comando!\n\nEu precizo das seguintes permissões: `' + ', '.join(error.missing_permissions)+'`',
						color=C.error)
				embed.set_image(url=MediaUrl.botmissingpermissionsbanner)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.errors.NoPrivateMessage):
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






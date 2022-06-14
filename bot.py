import os
from datetime import timedelta

import disnake
from disnake.ext import commands, tasks
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.assets import MediaUrl
import config

from rich.console import Console
C = Console()

os.system('clear')


#bot = commands.AutoShardedInteractionBot(
bot = commands.InteractionBot(
	#shard_count=10,
	intents							= config.intents,
	help_command				= None,
	sync_commands_debug	= True,
	#sync_permissions		= True,
	case_insensitive		= True,
	owner_ids						= config.owner_ids,
	reload							= True,
	strict_localization=True)
	#test_guilds=[957509903273046067])


@bot.event
async def on_ready():
	C.print(f'\n[orange_red1]{bot.user}[/] [green]online[/]')
	#status_task.start()
	C.print('[green]status task started[/]')
	channel = bot.get_channel(967464232021020683)
	await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.streaming, name='Made By: Lobo 🐺'))
	await channel.send('online')

#bot.i18n.load("locale/")
#print('locales loaded')

c = 0
if __name__ == '__main__':
	C.print(f'\n[red]COGS TO LOAD:[/]')
	for extension in config.extensions:
		bot.load_extension(extension)
		C.print(f'  [cyan]{c}[/] [yellow]:[/]  [green]{extension}[/]')
		c += 1

C.print(f'\n[red]DISNAKE:[/]')

@bot.event
async def on_message(msg: disnake.Message):
	if int(msg.channel.id) == 967464232021020683:
		await msg.delete(delay=60.0)


@bot.event
async def on_slash_command(inter: disnake.ApplicationCommandInteraction):
	
	try:
		C.print(f"""
[yellow]COMMAND:[/] [bright_magenta]{inter.data.name}[/]
[yellow]GUILD:  [/] [bright_magenta]{inter.guild.name}[/] [orange_red1]([/][aquamarine1]{inter.guild.id}[/][orange_red1])[/]
[yellow]AUTHOR: [/] [bright_magenta]{inter.author}[/] [orange_red1]([/][aquamarine1]{inter.author.id}[/][orange_red1])[/]""")
	except AttributeError:
		C.print(f"""
[yellow]COMMAND:[/] [bright_magenta]{inter.data.name}[/]
[yellow]DM COMMAND[/]
[yellow]AUTHOR: [/] [bright_magenta]{inter.author}[/] [orange_red1]([/][aquamarine1]{inter.author.id}[/][orange_red1])[/]""")

@bot.event
async def on_slash_command_error(inter: disnake.ApplicationCommandInteraction, error: Exception):
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
		Console.log(error)

bot.run(config.TOKEN)
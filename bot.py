import os
from datetime import timedelta

import disnake
from disnake.ext import commands, tasks
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.assets import MediaUrl
import config


os.system('clear')


bot = commands.InteractionBot(
	intents							= config.intents,
	help_command				= None,
	sync_commands_debug	= True,
	#sync_permissions		= True,
	case_insensitive		= True,
	owner_ids						= config.owner_ids,
	reload							= True)
	#test_guilds=[957509903273046067])



@bot.event
async def on_ready():
	print(f'{bot.user} online')
	status_task.start()
	print('status task started')
	channel = bot.get_channel(967464232021020683)
	await channel.send('online')


@tasks.loop(seconds=15)
async def status_task():
	try:
		await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.streaming, name=f'ping: {int(round(bot.latency * 1000))}ms'))
	except OverflowError:
		pass


if __name__ == '__main__':
	for extension in config.extensions:
		bot.load_extension(extension)
		print(f'{extension} loaded')


@bot.event
async def on_message(
  msg: disnake.Message):
	if int(msg.channel.id) == 967464232021020683:
		await msg.delete(delay=60.0)


@bot.event
async def on_slash_command(inter: disnake.ApplicationCommandInteraction):
	
	try:
		print(f"""\ncommand: {inter.data.name}
guild: {inter.guild.name} ({inter.guild.id})
author: {inter.author} ({inter.author.id})\n""")
	except AttributeError:
		print(f"""\ncommand: {inter.data.name}
DM COMMAND
author: {inter.author} ({inter.author.id})\n""")


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
		print(error)


bot.run(config.TOKEN)
import os
from datetime import timedelta

import disnake
from disnake.ext import commands, tasks
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C

import config


os.system('clear')

bot = commands.InteractionBot(
	intents							= config.intents,
	help_command				= None,
	sync_commands_debug	= True,
	sync_permissions		= True,
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


@tasks.loop(seconds=7200)
async def status_task():
	await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.streaming, name=config.get_game()))
	print('changed status task')


if __name__ == '__main__':
	for extension in config.extensions:
		bot.load_extension(extension)
		print(f'{extension} loaded')


@bot.event
async def on_message(msg: disnake.Message):
	if int(msg.channel.id) == 967464232021020683:
		await msg.delete(delay=120.0)


@bot.event
async def on_slash_command(inter: disnake.ApplicationCommandInteraction):
	
	print(f'Executed {inter.data.name} command in {inter.guild.name} (ID: {inter.guild.id}) by {inter.author} (ID: {inter.author.id})')


@bot.event
async def on_slash_command_error(inter: disnake.ApplicationCommandInteraction, error: Exception):
	
	if isinstance(error, commands.CommandOnCooldown):
			
			embed = disnake.Embed(
				title=f'{E.error} | comando em cooldown!',
				description=f'<@{inter.author.id}>, este comando está em cooldown, você só poderá executá-lo novamente em `{str(timedelta(seconds=error.retry_after)).split(".")[0]}`.',
				color=C.error)
				
			await inter.send(embed=embed, ephemeral=True)
	
	elif isinstance(error, commands.NotOwner):
			
			embed = disnake.Embed(
				title=f'{E.error} | apenas pessoas especiais podem usar este comando.',
				color=C.error)
			
			await inter.send(embed=embed, ephemeral=True)


	elif isinstance(error, commands.errors.MissingPermissions):
		
			embed = EB(
					title='você não tem as permissões nescessárias para executar este comando!',
					description='você preciza das seguintes permissões: `' + ', '.join(error.missing_permissions)+'`',
					color=C.error)
			await inter.send(embed=embed, ephemeral=True)

	elif isinstance(error, commands.errors.BotMissingPermissions):
		
			embed = EB(
					title='eu não tem as permissões nescessárias para executar este comando!',
					description='eu precizo das seguintes permissões: `' + ', '.join(error.missing_permissions),
					color=C.error)+'`'
			await inter.send(embed=embed, ephemeral=True)
	else:
		print(error)


bot.run(config.TOKEN)
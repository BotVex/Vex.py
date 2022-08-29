import json 
from random import choice

import disnake
from disnake.ext import commands, tasks
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.assets import MediaUrl

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
		
		with open('data/games.json') as games:
			self.game_list = json.loads(games.read())


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == self.bot.user.id:
			return
		else:
			mentions = message.mentions
			if len(mentions) != 0:
				for mentioned in mentions:
					if mentioned.id == self.bot.user.id:
						await message.reply(f':wave: | Olá {message.author.mention}, meu nome é **{self.bot.user.name}**, e para utilizar meus comandos, utilize `comandos de barra (/)`.')
						break


	@tasks.loop(minutes=10.0)
	async def status_task(self):
		shard_ids = sorted(set([guild.shard_id for guild in self.bot.guilds]))
		
		for shard_id in shard_ids:
			activity_type = disnake.ActivityType.playing
			activity_name = choice(self.game_list)

			await self.bot.change_presence(
				activity=disnake.Activity(
					type=activity_type, 
					name=activity_name, 
					shard_id=shard_id
					)
				)
	

	@commands.Cog.listener()
	async def on_ready(self):
		print(f'\n{self.bot.user} online')
		try:
			self.status_task.start()
			print('status task started')
		except Exception as e:
			print(f'status task failed\n{e}')


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

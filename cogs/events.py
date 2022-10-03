import json
import datetime
from time import time
from random import choice

from rich.console import Console
log = Console().log

import disnake
from disnake.ext import commands, tasks
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.newassets import DefaultColors, GetColor, Icons


class Events(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
		self.bot.start_time = time() 
		
		with open('data/games.json') as games:
			self.game_list = json.loads(games.read())
	
	
	@commands.Cog.listener()
	async def on_connect(self):
		log('connected in Discord')

		#TODO: essa parada ta definndo a cor a cada shard, depois tem que resolver
		bot_avatar = self.bot.user.display_avatar.with_size(16)
		
		self.bot.default_color = await GetColor.general_color_url(bot_avatar)
		log(f'default color is defined to {self.bot.default_color}')


	@commands.Cog.listener()
	async def on_disconnect(self):
		log('disconnected of Discord')


	@commands.Cog.listener()
	async def on_resumed(self):
		log('resumed section')


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == self.bot.user.id or message.author.bot is True:
			return
		else:
			mentions = message.mentions
			if len(mentions) != 0:
				for mentioned in mentions:
					if mentioned.id == self.bot.user.id:
						embed = EB(color=self.bot.default_color)
						embed.title = f':wave: Olá {message.author.name}'
						embed.description = f'Meu nome é **{self.bot.user.name}**!\n\nSou um bot de **entretenimento** ~~e **manipulação de imagem**~~ que está em desenvolvimento.\n\nPara utilizar meus comandos, utilize [comandos de barra ( / )](https://discord.com/blog/welcome-to-the-new-era-of-discord-apps).'
						embed.timestamp = datetime.datetime.now()
						embed.set_footer(text=message.author.display_name, icon_url=message.author.display_avatar)
						
						await message.reply(embed=embed)
						break


	@tasks.loop(minutes=10.0)
	async def status_task(self):
		
		for shard_id in [x for x in self.bot.shards]:
			activity_type = disnake.ActivityType.playing
			activity_name = f'{choice(self.game_list)} [{shard_id+1}]'
		
			await self.bot.change_presence(
				status=disnake.Status.idle,
				activity=disnake.Activity(
					type=activity_type, 
					name=activity_name, 
					shard_id=shard_id
					)
				)
	

	@commands.Cog.listener()
	async def on_ready(self):
		log(f'{self.bot.user} online')
		
		if self.status_task.is_running():
			log('status task was already running')
		else:
			self.status_task.start()
			log('status task started')


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
					color=DefaultColors.ERROR)
			embed.set_image(url=Icons.CMD_ON_COOLDOWN)
			embed.set_footer(text='Você está executando comandos rapidamente!')
			await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.NotOwner):
				embed = disnake.Embed(
					title='Não desenvolvedor!',
					description='Apenas pessoas especiais podem utilizar este comando.',
					color=DefaultColors.ERROR)
				embed.set_image(url=Icons.NOT_OWNER)
				await inter.send(embed=embed, ephemeral=True)

		
		elif isinstance(error, commands.MissingPermissions):
				embed = EB(
						title='Sem permissão!',
						description=f'Eu não tenho as permissões nescessárias para executar este comando!\n\n{"Você preciza das seguintes permissões: `" + ", ".join(error.missing_permissions)+"`" if len(error.missing_permissions) != 1 else "Você preciza da seguinte permissão: `" + ", ".join(error.missing_permissions)+"`"}',
						color=DefaultColors.ERROR)
				embed.set_image(url=Icons.MISSING_PERMS)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.BotMissingPermissions):
				embed = EB(
					title='Não autorizado!',
						description=f'Eu não tenho as permissões nescessárias para executar este comando!\n\n{"Eu precizo das seguintes permissões: `" + ", ".join(error.missing_permissions)+"`" if len(error.missing_permissions) != 1 else "Eu precizo da seguinte permissão: `" + ", ".join(error.missing_permissions)+"`"}',
						color=DefaultColors.ERROR)
				embed.set_image(url=Icons.BOT_MISSING_PERMS)
				await inter.send(embed=embed, ephemeral=True)
		
		
		elif isinstance(error, commands.NoPrivateMessage):
				embed = EB(
					title='Apenas para servidores!',
						description='Este comando só pode ser utilizado em servidores!', 
						color=DefaultColors.ERROR) 
				embed.set_image(url=Icons.NO_PRIVATE_MSG)
				await inter.send(embed=embed, ephemeral=True)
		else:
			log(error)
	
	
def setup(bot):
	bot.add_cog(Events(bot))

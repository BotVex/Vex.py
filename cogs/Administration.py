from textwrap import shorten as short
import typing

import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.assets import Colors as C


class Administration(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(name='adm')
	async def adm(self, inter: ACI):
		pass
	
	
	#purge
	@commands.has_permissions(manage_messages=True)
	@commands.bot_has_permissions(manage_messages=True)
	@commands.cooldown(1, 7, commands.BucketType.user)
	@commands.guild_only()
	@adm.sub_command(
			name='purge',
			description=f'{E.administration}Deleto a quantidade de mensagens especificadas.',
			options=[
					disnake.Option(
							name='amount',
							description='A quantidade de mensagens que serão apagadas. Deve estar entre 2 e 1000.',
							type=disnake.OptionType.integer,
							required=True,
							min_value=2,
							max_value=1000
					)
			]
	)
	async def purge(self, inter: ACI, amount: int):
		await inter.response.defer()
		
		try:
			count_members = {}
			messages = await inter.channel.history(limit=amount).flatten()
			await inter.channel.purge(limit=amount+1)
			for message in messages[1:]:
				if str(message.author) in count_members:
					count_members[str(message.author)] += 1
				else:
					count_members[str(message.author)] = 1
				new_string = []
				deleted_messages = 0
				for author, message_deleted in list(count_members.items()):
					new_string.append(f'**{author}**: {message_deleted}')
					deleted_messages += message_deleted
				final_string = f'\n'.join(new_string)
			
			embed = EB(
				title=f'{E.success}{deleted_messages} Mensagens apagadas!',
				description=final_string,
				color=C.success)
			
			await inter.channel.send(embed=embed, delete_after=15.0)
		except:
			embed = EB(
				title=f'{E.error}Não foi possivel apagar as mensagens.',
				description=final_string,
				color=C.success)
			
			await inter.channel.send(embed=embed, delete_after=15.0)

	
	#botme
	@commands.has_permissions(administrator=True)
	@commands.bot_has_permissions(manage_webhooks=True, manage_messages=True)
	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.guild_only()
	@adm.sub_command(
			name='botme',
			description=f'{E.administration}Envie uma mensagem como se você fosse um bot.',
			options=[
					disnake.Option(
							name='message',
							description='Sua mensagem.',
							type=disnake.OptionType.string,
							required=True
					),
					disnake.Option(
							name='channel',
							description='O canal onde a mensagem será enviada.',
							type=disnake.OptionType.channel,
							required=False
					)
			]
	)
	async def botme(self, inter: ACI, message: str, channel: disnake.TextChannel=None):
		await inter.response.defer()

		if len(message) > 2000:
			await inter.send('A mensagem é muito grande!')
			return
		
		if channel is None:
			channel = inter.channel
		
		if not isinstance(channel, disnake.TextChannel):
			await inter.send('canal inválido!', ephemeral=True)
			return
		
		channel_webhooks = await channel.webhooks()
		
		for webhook in channel_webhooks:
			if webhook.user == self.bot.user and webhook.name == "Bot Webhook":
				break
		else:
			webhook = await channel.create_webhook(name="Bot Webhook")
		
		await inter.delete_original_message()
		
		await webhook.send(username=inter.author.display_name, content=message, avatar_url=inter.author.display_avatar.url)
	

	#nick
	@commands.has_permissions(manage_nicknames=True)
	@commands.bot_has_permissions(manage_nicknames=True)
	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.guild_only()
	@adm.sub_command(
			name='nick',
			description=f'{E.administration}Altera o nick de um usuário do server.',
			options=[
					disnake.Option(
							name='user',
							description='O usuário que o nick será alterado.',
							type=disnake.OptionType.user,
							required=True
					),
					disnake.Option(
							name='nickname',
							description='O novo nick do usuário. Mantenha vazio para voltar ao nome original.',
							type=disnake.OptionType.string,
							required=False
					)
			]
	)
	async def nick(self, inter: ACI, user: disnake.User, nickname: str = None):

			if len(nickname) > 32:
				await inter.send('O nickname é muito grande! o maximo é de 32 caracteres.')
				return
			
			member = await inter.guild.get_or_fetch_member(user.id)
			try:
					await member.edit(nick=nickname)
					if nickname is None:
						nickname = member.name
					embed = EB(
							title=f'{E.success}nick alterado!',
							description=f'Nick alterado para **`{nickname}`**!',
							color=C.success)
					await inter.send(embed=embed)
			except:
					embed = EB(
							title=f'{E.error}Erro!',
							description=f'Ocorreu um erro ao tentar alterar o nick do usuário. Certifique-se de que meu cargo esteja acima do cargo de {member.mention} e tente novamente.',
							color=C.error)
					await inter.send(embed=embed, ephemeral=True)
	
	
	#kick
	@commands.has_permissions(kick_members=True)
	@commands.bot_has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.guild_only()
	@adm.sub_command(
		name='kick',
		description=f'{E.administration}Quica o usuário do servidor.',
		options=[
				disnake.Option(
						name='user',
						description='O usuário a ser quicado.',
						type=disnake.OptionType.user,
						required=True
				),
				disnake.Option(
						name='reason',
						description='O motivo pelo qual o usuário está sendo quicado.',
						type=disnake.OptionType.string,
						required=False
				),
				disnake.Option(
						name='notify',
						description='Avisar o usuário(caso ele possua a DM aberta).',
						type=disnake.OptionType.boolean,
						required=False
				)
		]
	)
	async def kick(self, inter: ACI, user: disnake.User, reason: str=None, notify: bool=False):
			
			if user.id == inter.author.id:
				await inter.send('Você não pode quicar você mesmo!', ephemeral=True)
				return

			elif user.id == inter.guild.owner_id:
						embed = EB(
							title=f'{E.error}Erro!',
							description='Eu não posso quicar o dono do servidor.',
							color=C.error)
						await inter.send(embed=embed, ephemeral=True)
						return
			
			elif user.guild_permissions.administrator:
						embed = EB(
							title=f'{E.error}Erro!',
							description='Eu não posso quicar administradores.',
							color=C.error)
						await inter.send(embed=embed, ephemeral=True)
						return
			
			else:
					try:
							embed = EB(
								title=f'{E.success} Usuário quicado!',
								description=f'{user.mention} foi quicado por {inter.author.mention}!',
								color=C.success)
							
							if reason is not None:
								if len(reason) > 512:
									reason = short(reason, width=512, placeholder='...')
								
								embed.add_field(
										name='Motivo:',
										value=reason,
										inline=False)
							
							await user.kick(reason=reason)
							await inter.send(embed=embed, ephemeral=True)

							if notify is True:
								try:
									embed = EB(
										title=f'Você foi quicado de {inter.guild.name}!',
										color=C.warning)
									embed.add_field(name='Motivo:', value=reason, inline=False)
									await user.send(embed=embed)
								except disnake.Forbidden:
									pass
					except:
							embed = EB(
									title=f'{E.error}Erro!',
									description=f'Ocorreu um erro ao tentar quicar o usuário. Certifique-se de que meu cargo estejam acima dos cargos de {user.mention} e tente novamente.',
									color=C.error)
							await inter.send(embed=embed, ephemeral=True)
	
	
	#ban
	@commands.has_permissions(ban_members=True)
	@commands.bot_has_permissions(ban_members=True)
	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.guild_only()
	@adm.sub_command(
			name='ban',
			description=f'{E.administration}Bane um usuário do servidor.',
			options=[
					disnake.Option(
							name='user',
							description='Usuário a ser banido.',
							type=disnake.OptionType.user,
							required=True
					),
					disnake.Option(
							name='reason',
							description='Motivo do banimento.',
							type=disnake.OptionType.string,
							required=False
					),
					disnake.Option(
							name='delete_message_days',
							description='O número de dias de mensagens a serem excluídas do usuário No server. O mínimo é 0 e o máximo é 7.',
							type=disnake.OptionType.integer,
							min_value=0,
							max_value=7,
							required=False
					)
			]
	)
	async def ban(self, inter: ACI, user: disnake.User, delete_message_days: int=0, reason: str=None, notify: bool=False): 
			
			if user.id == inter.author.id:
				await inter.send('Você não pode banir você mesmo!', ephemeral=True)
				return

			elif user.id == inter.guild.owner_id:
						embed = EB(
							title=f'{E.error}Erro!',
							description='Eu não posso banir o dono do servidor.',
							color=C.error)
						await inter.send(embed=embed, ephemeral=True)
						return
			
			elif user.guild_permissions.administrator:
						embed = EB(
							title=f'{E.error}Erro!',
							description='Eu não posso bainr administradores.',
							color=C.error)
						await inter.send(embed=embed, ephemeral=True)
						return

			else:
					try:
							embed = EB(
								title=f'{E.success} Usuário banido!',
								description=f'{user.mention} foi banido por {inter.author.mention}!',
								color=C.success)
						
							if reason is not None:
								if len(reason) > 512:
									reason = short(reason, width=512, placeholder='...')
								
								embed.add_field(
										name='Motivo:',
										value=reason,
										inline=False)
							
							await user.ban(reason=reason, delete_message_days=delete_message_days)
							await inter.send(embed=embed, ephemeral=True)

							if notify is True:
								try:
									embed = EB(
										title=f'Você foi banido de {inter.guild.name}!',
										color=C.warning)
									embed.add_field(name='Motivo:', value=reason, inline=False)
									await user.send(embed=embed)
								except disnake.Forbidden:
									pass
					except:
							embed = EB(
									title=f'{E.error}Erro!',
									description=f'Ocorreu um erro ao tentar banir o usuário. Certifique-se de que meu cargo esteja acima do cargo de {user.mention} e tente novamente.',
									color=C.error)
							await inter.send(embed=embed, ephemeral=True)
			
	
	#hackban
	@commands.has_permissions(ban_members=True)
	@commands.bot_has_permissions(ban_members=True)
	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.guild_only()
	@adm.sub_command(
			name='hackban',
			description=f'{E.administration}Bane um usuário sem que ele esteja no servidor através de seu ID.',
			options=[
					disnake.Option(
							name='user_id',
							description='O ID do usuário a ser banido.',
							type=disnake.OptionType.string,
							required=True
					),
					disnake.Option(
							name='reason',
							description='Motivo do banimento.',
							type=disnake.OptionType.string,
							required=False
					)
			]
	)
	async def hackban(self, inter: ACI, user_id: str, reason: str=None): 
			
			try:
					user = await self.bot.get_or_fetch_user(int(user_id))
			except:
					await inter.send('ID de usuário inválido!', ephemeral=True)
					return
			
			try:
					user_banned = await inter.guild.fetch_ban(user)

					embed = EB(
							title=f'{E.error}Erro!',
							description='Usuário já banido.',
							color=C.error)
					#if user_banned.reason not is None:
							#embed.add_field(
								#name='Motivo:',
								#value=user_banned.reason,
								#inline=False)
					
					await inter.send(embed=embed, ephemeral=True)
					return
			except disnake.NotFound:
					pass

			for user_guild in inter.guild.members:
				if user_guild.id == user.id:
					if user.id == inter.guild.owner_id:
						embed = EB(
							title=f'{E.error}Erro!',
							description='Eu não posso banir o dono do servidor.',
							color=C.error)
						await inter.send(embed=embed, ephemeral=True)
						break

					elif user.guild_permissions.administrator:
						embed = EB(
							title=f'{E.error}Erro!',
							description='Eu não posso banir administradores.',
							color=C.error)
						await inter.send(embed=embed, ephemeral=True)
						break
			
			if user.id == inter.author.id:
				await inter.send('Você não pode banir você mesmo!', ephemeral=True)
				return

			try:
					embed = EB(
						title=f'{E.success} Usuário banido!',
						description=f'{user}(*{user.id}*) foi banido por {inter.author.mention}!',
						color=C.success)
				
					if reason is not None:
						if len(reason) > 512:
							reason = short(reason, width=512, placeholder='...')
						
						embed.add_field(
								name='Motivo:',
								value=reason,
								inline=False)
					
					await self.bot.http.ban(str(user.id), inter.guild.id, reason=reason)
					await inter.send(embed=embed, ephemeral=True)

			except:
					embed = EB(
							title=f'{E.error}Erro!',
							description=f'Ocorreu um erro ao tentar banir o usuário {user.name}(*{user.id}*) do servidor.',
							color=C.error)
					await inter.send(embed=embed, ephemeral=True)
			
	
	#unban
	@commands.has_permissions(ban_members=True)
	@commands.bot_has_permissions(ban_members=True)
	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.guild_only()
	@adm.sub_command(
			name='unban',
			description=f'{E.administration}Desbane um usuário através de seu ID.',
			options=[
					disnake.Option(
							name='user_id',
							description='O ID do usuário a ser desbanido.',
							type=disnake.OptionType.string,
							required=True
					),
					disnake.Option(
							name='reason',
							description='Motivo do desbanimento.',
							type=disnake.OptionType.string,
							required=False
					)
			]
	)
	async def unban(self, inter: ACI, user_id: str, reason: str=None): 
			
			try:
					user = await self.bot.get_or_fetch_user(int(user_id))
			except:
					await inter.send('ID de usuário inválido!', ephemeral=True)
					return
			
			if user.id == inter.author.id:
				await inter.send('Você não pode desbanir você mesmo!', ephemeral=True)
				return
			
			for user_guild in inter.guild.members:
				if user_guild.id == user.id:
					if user.id == inter.guild.owner_id:
						embed = EB(
							title=f'{E.error}Erro!',
							description='Eu não posso desbanir o dono do servidor, porque ele não pode ser banido.',
							color=C.error)
						await inter.send(embed=embed, ephemeral=True)
						break

					if user_guild.id == user.id:
						embed = EB(
							title=f'{E.error}Erro!',
							description='Eu não posso desbanir um usuário que já está no servidor.',
							color=C.error)
						await inter.send(embed=embed, ephemeral=True)
						break

			else:
					try:
							embed = EB(
								title=f'{E.success} Usuário desbanido!',
								description=f'{user.name}(*{user.id}*) foi desbanido por {inter.author.mention}!',
								color=C.success)
						
							if reason is not None:
								if len(reason) > 512:
									reason = short(reason, width=512, placeholder='...')
								
								embed.add_field(
										name='Motivo:',
										value=reason,
										inline=False)
							
							await self.bot.http.unban(str(user.id), inter.guild.id, reason=reason)
							await inter.send(embed=embed, ephemeral=True)

					except:
							embed = EB(
									title=f'{E.error}Erro!',
									description=f'Ocorreu um erro ao tentar desbanir o usuário {user.name}(*{user.id}*) do servidor.',
									color=C.error)
							await inter.send(embed=embed, ephemeral=True)
			
	
def setup(bot):
		bot.add_cog(Administration(bot))

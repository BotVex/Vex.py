import datetime

import disnake
from disnake.ext import commands
from disnake import Localized
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.assets import Colors as C


class Administration(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(name=Localized('adm', key='ADM_ADM_NAME'), dm_permission=False)
	async def adm(self, inter: ACI):
		pass
	
	
	#purge
	@commands.has_permissions(manage_messages=True)
	@commands.bot_has_permissions(manage_messages=True)
	@commands.cooldown(2, 10, commands.BucketType.user)
	@adm.sub_command(
			name=Localized('purge', key='ADM_MOD_CMD_PURGE_NAME'),
			description=Localized('Deletes the specified number of messages.', key='ADM_MOD_CMD_PURGE_DESC'),
			options=[
					disnake.Option(
							name='amount',
							description=Localized('The number of messages that will be deleted. It must be between 2 and 1000.', key='ADM_MOD_CMD_PURGE_AMOUNT_DESC'),
							type=disnake.OptionType.integer,
							required=True,
							min_value=2,
							max_value=1000
					)
			]
	)
	async def purge(self, inter: ACI, amount: int):
		await inter.response.defer()
		
		amount += 1

		try:
			count_members = {}
			messages = await inter.channel.history(limit=amount).flatten()
			
			for message in messages[1:]:
				if str(message.author) in count_members:
					count_members[str(message.author)] += 1
				else:
					count_members[str(message.author)] = 1
				new_string = []
				deleted_messages = 0
				for author, message_deleted in list(count_members.items()):
					new_string.append(f'- **`{author}`**: {message_deleted}')
					deleted_messages += message_deleted
			final_string = f'\n'.join(new_string)
			

			embed = EB(color=C.success)
			embed.title = f'{E.success}{deleted_messages} Mensagens apagadas!'
			embed.description = final_string
			embed.timestamp = datetime.datetime.now()
			embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)
			
			await inter.channel.purge(limit=amount)
			await inter.channel.send(embed=embed, delete_after=15.0)
		except:
			embed = EB(color=C.error)
			embed.title=f'{E.error}Não foi possivel apagar as mensagens.'
			embed.timestamp = datetime.datetime.now()
			embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

			await inter.channel.send(embed=embed, delete_after=15.0)

	
	#botme
	@commands.has_permissions(administrator=True)
	@commands.bot_has_permissions(manage_webhooks=True, manage_messages=True)
	@commands.cooldown(1, 15, commands.BucketType.user)
	@adm.sub_command(
			name=Localized('botme', key='ADM_ADM_CMD_BOTME_NAME'),
			description=Localized('Send a message a bot.', key='ADM_ADM_CMD_BOTME_DESC'),
			options=[
					disnake.Option(
							name='message',
							description=Localized('message', key='ADM_ADM_CMD_BOTME_MESSAGE'),
							type=disnake.OptionType.string,
							min_length=1,
							max_length=2000,
							required=True
					),
					disnake.Option(
							name='channel',
							description=Localized('The channel where the message will be sent.', key='ADM_ADM_CMD_BOTME_CHANNEL'),
							type=disnake.OptionType.channel,
							required=False
					)
			]
	)
	async def botme(self, inter: ACI, message: str, channel: disnake.TextChannel=None):
		await inter.response.defer()

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
	@adm.sub_command(
			name=Localized('nick', key='ADM_ADM_CMD_NICK_NAME'),
			description=Localized('Change the nick of a server user.', key='ADM_ADM_CMD_NICK_DESC'),
			options=[
					disnake.Option(
							name='user',
							description=Localized('The user the nick will be changed to.', key='ADM_ADM_CMD_NICK_USER'),
							type=disnake.OptionType.user,
							required=True
					),
					disnake.Option(
							name='nickname',
							description=Localized("The user's new nick. Keep empty to return to the original name.", key='ADM_ADM_CMD_NICK_NICKNAME'),
							type=disnake.OptionType.string,
							min_length=1,
							max_length=32,
							required=False
					)
			]
	)
	async def nick(self, inter: ACI, user: disnake.User, nickname: str = None):
			try:
					await user.edit(nick=nickname)
					if nickname is None:
						nickname = user.name
					
					embed = EB(color=C.success)
					embed.title = f'{E.success}nick alterado!'
					embed.description = f'Nick alterado para **`{nickname}`**!'
					embed.set_thumbnail(url=user.display_avatar)
					embed.timestamp = datetime.datetime.now()
					embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

					await inter.send(embed=embed)
					return

			except AttributeError:
					embed = EB(color=C.error)
					embed.title = 'Erro!'
					embed.description = f'O usuário não está no servidor.'
					embed.timestamp = datetime.datetime.now()
					embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

					await inter.send(embed=embed, ephemeral=True)
					return
			
			except Exception as e:
					embed = EB(color=C.error)
					embed.title = 'Erro!'
					embed.description = f'Ocorreu um erro ao tentar alterar o nick do usuário.\n\n> Certifique-se de que meu cargo esteja acima do cargo de ({user.id});\n\n> Verifique se o usuário está no servidor;\n\n> Certifique-se de que você e eu tenhamos as permissões nescessárias.'
					embed.timestamp = datetime.datetime.now()
					embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

					await inter.send(embed=embed, ephemeral=True)
					print(e)
					return


	#kick
	@commands.has_permissions(kick_members=True)
	@commands.bot_has_permissions(kick_members=True)
	@commands.cooldown(2, 10, commands.BucketType.user)
	@adm.sub_command(
		name=Localized('kick', key='ADM_ADM_CMD_KICK_NAME'),
		description=Localized('Kick the server user.', key='ADM_ADM_CMD_KICK_DESC'),
		options=[
				disnake.Option(
						name='user',
						description=Localized('The user to be kicked out.', key='ADM_ADM_CMD_KICK_USER'),
						type=disnake.OptionType.user,
						required=True
				),
				disnake.Option(
						name='reason',
						description=Localized('The reason the user is being kicked out.', key='ADM_ADM_CMD_KICK_REASON'),
						type=disnake.OptionType.string,
							min_length=3,
							max_length=512,
						required=False
				)
		]
	)
	async def kick(self, inter: ACI, user: disnake.User, reason: str=None):
		try:
			if user.id == inter.author.id:
				await inter.send('Você não pode expulsar você mesmo!', ephemeral=True)
				return

			elif user.id == inter.guild.owner_id:
				await inter.send('Eu não posso expulsar o dono do servidor.', ephemeral=True)
				return
			
			elif user.guild_permissions.administrator:
				await inter.send('Eu não posso expulsar administradores.', ephemeral=True)
				return

			embed = EB(color=C.success)
			embed.title = 'Usuário expulso!'
			embed.description = f'{user}(`{user.id}`) foi expulso por {inter.author.mention}(`{inter.author.id}`)!'
			embed.set_thumbnail(url=user.display_avatar)
			embed.timestamp = datetime.datetime.now()
			embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)
			
			if reason is not None:
				embed.add_field(name='Motivo:', value=reason, inline=False)
			else:
				reason = 'Não informado'
			
			await user.kick(reason=reason)
			await inter.send(embed=embed)
			return

		except AttributeError:
				embed = EB(color=C.error)
				embed.title = 'Erro!'
				embed.description = f'O usuário não está no servidor.'
				embed.timestamp = datetime.datetime.now()
				embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

				await inter.send(embed=embed, ephemeral=True)
				return
		
		except Exception as e:
				embed = EB(color=C.error)
				embed.title = 'Erro!'
				embed.description = f'Ocorreu um erro ao tentar expulsar usuário.\n\n> Certifique-se de que meu cargo esteja acima do cargo de ({user.id});\n\n> Verifique se o usuário está no servidor;\n\n> Certifique-se de que você e eu tenhamos as permissões nescessárias.'
				embed.timestamp = datetime.datetime.now()
				embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

				await inter.send(embed=embed, ephemeral=True)
				return
				print(e)
	
	
	#ban
	@commands.has_permissions(ban_members=True)
	@commands.bot_has_permissions(ban_members=True)
	@commands.cooldown(2, 10, commands.BucketType.user)
	@adm.sub_command(
			name=Localized('ban', key='ADM_ADM_CMD_BAN_NAME'),
			description=Localized('Ban the user from the server.', key='ADM_ADM_CMD_BAN_DESC'),
			options=[
					disnake.Option(
							name='user',
							description=Localized('The user to be Banned.', key='ADM_ADM_CMD_BAN_USER'),
							type=disnake.OptionType.user,
							required=True
					),
					disnake.Option(
							name='reason',
							description=Localized('The reason the user is being banned.', key='ADM_ADM_CMD_BAN_REASON'),
							type=disnake.OptionType.string,
							min_length=3,
							max_length=512,
							required=False
					),
					disnake.Option(
							name='delete_message_days',
							description=Localized('The number of messages to be deleted in days. The minimum is 0 and the maximum is 7.', key='ADM_ADM_CMD_BAN_DELMSGDAYS'),
							type=disnake.OptionType.integer,
							min_value=0,
							max_value=7,
							required=False
					)
			]
	)
	async def ban(self, inter: ACI, user: disnake.User, delete_message_days: int=0, reason: str=None): 
		try:
			if user.id == inter.author.id:
				await inter.send('Você não pode banir você mesmo!', ephemeral=True)
				return

			elif user.id == inter.guild.owner_id:
				await inter.send('Eu não posso banir o dono do servidor.', ephemeral=True)
				return
			
			try:
				if user.guild_permissions.administrator:
					await inter.send('Eu não posso banir administradores.', ephemeral=True)
					return
			except:
				pass

			embed = EB(color=C.success)
			embed.title = 'Usuário banido!'
			embed.description = f'{user}(`{user.id}`) foi banido por {inter.author.mention}(`{inter.author.id}`)!'
			embed.set_thumbnail(url=user.display_avatar)
			embed.timestamp = datetime.datetime.now()
			embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)
			
			try:
				fetch_ban = await inter.guild.fetch_ban(user)

				embed.title = 'Usuário já banido!'
				embed.description = f'{user}(`{user.id}`) já foi banido!'
				embed.add_field(name='Motivo:', value=fetch_ban.reason, inline=False)
				await inter.send(embed=embed)
				return

			except disnake.NotFound:
				if reason is not None:
					embed.add_field(name='Motivo:', value=reason, inline=False)
				else:
					reason = 'Não informado'
				
				await self.bot.http.ban(user_id=str(user.id), guild_id=inter.guild.id, reason=reason, delete_message_days=delete_message_days)
				await inter.send(embed=embed)
				return

		except Exception as e:
				embed = EB(color=C.error)
				embed.title = 'Erro!'
				embed.description = f'Ocorreu um erro ao tentar banir usuário.\n\n> Certifique-se de que meu cargo esteja acima do cargo de ({user.id});\n\n> Verifique se o usuário está no servidor;\n\n> Certifique-se de que você e eu tenhamos as permissões nescessárias.'
				embed.timestamp = datetime.datetime.now()
				embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

				await inter.send(embed=embed, ephemeral=True)
				print(e)
				return

	
	#unban
	@commands.has_permissions(ban_members=True)
	@commands.bot_has_permissions(ban_members=True)
	@commands.cooldown(2, 10, commands.BucketType.user)
	@adm.sub_command(
			name=Localized('unban', key='ADM_ADM_CMD_UNBAN_NAME'),
			description=Localized('Unban a user through his ID.', key='ADM_ADM_CMD_HACKBAN_DESC'),
			options=[
					disnake.Option(
							name='user',
							description=Localized('The ID of the user to be unbanned.', key='ADM_ADM_CMD_UNBAN_USERID'),
							type=disnake.OptionType.user,
							required=True
					)
			]
	)
	async def unban(self, inter: ACI, user: disnake.User):
			for user_guild in inter.guild.members:
				if user_guild.id == user.id:
					await inter.send('Eu não posso desbanir um usuário que já está no servidor.', ephemeral=True)
					break
			
			if user.id == inter.guild.owner_id:
				await inter.send('Eu não posso desbanir o dono do servidor, porque ele não pode ser banido.', ephemeral=True)
				return

			else:
					try:
						embed = EB(color=C.success)
						embed.title = 'Usuário desbanido!'
						embed.description = f'{user}(`{user.id}`) foi desbanido por {inter.author.mention}(`{inter.author.id}`)!'
						embed.set_thumbnail(url=user.display_avatar)
						embed.timestamp = datetime.datetime.now()
						embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

						try:
							fetch_ban = await inter.guild.fetch_ban(user)

							embed.add_field('Motivo do banimento:', fetch_ban.reason)

							await self.bot.http.unban(user_id=str(user.id), guild_id=inter.guild.id)
							await inter.send(embed=embed)
							return

						except disnake.NotFound:
							embed.title = 'Usuário já desbanido!'
							embed.description = f'{user}(`{user.id}`) já foi desbanido!'

							await inter.send(embed=embed)
							return

					except Exception as e:
						embed = EB(color=C.error)
						embed.title = 'Erro!'
						embed.description = f'Ocorreu um erro ao tentar desbanir usuário.\n\nCertifique-se de que você e eu tenhamos as permissões nescessárias.'
						embed.timestamp = datetime.datetime.now()
						embed.set_footer(text=inter.author.display_name, icon_url=inter.author.display_avatar)

						await inter.send(embed=embed, ephemeral=True)
						print(e)
						return
			
	
def setup(bot):
		bot.add_cog(Administration(bot))

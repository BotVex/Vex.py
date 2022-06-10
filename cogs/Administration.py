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
	
	
	#clear
	@commands.guild_only()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(1, 7, commands.BucketType.user)
	@adm.sub_command(
			name='clear',
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
	async def clear(self, inter: disnake.ApplicationCommandInteraction, amount: int):
		await inter.response.defer()
		
		try:
				purged_messages = await inter.channel.purge(limit=amount)
				embed = EB(
					title=f'{E.success}Mensagens apagadas!',
					description=f'**<@{inter.author.id}>** apagou **{len(purged_messages)}** mensagens!',
					color=C.success)
				await inter.channel.send(embed=embed, delete_after=15.0)
		except:
				embed = EB(
					title=f'{E.error}Não foi possivel apagar as mensagens.',
					color=C.error)
				await inter.channel.send(embed=embed, delete_after=15.0, ephemeral=True)
	
	
	#kick
	@commands.guild_only()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.user)
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
				)
		]
	)
	async def kick(
		self, 
		inter: ACI,
		user: disnake.User, 
		reason: str='Motivo não informado.'):

			member = await inter.guild.get_or_fetch_member(user.id)
			if member.guild_permissions.administrator:
					embed = EB(
							title=f'{E.error}Erro!',
							description='Eu não posso quicar administradores.',
							color=C.error)
					await inter.send(embed=embed, ephemeral=True)
			else:
					try:
							await member.kick(reason=reason)
							embed = EB(
									title=f'{E.success} Usuário quicado!',
									description=f'**<@{member.id}>** foi quicado por **<@{inter.id}>**!',
									color=C.success)
							embed.add_field(
									name='Motivo:',
									value=reason)
							await inter.send(embed=embed)
							try:
									await member.send(
											f'Você foi quicado de **{inter.guild.name}** por **{inter.author}**!\n\nMotivo: {reason}')
							except disnake.Forbidden:
									pass
					except:
							embed = EB(
									title=f'{E.error}Erro!',
									description=f'Ocorreu um erro ao tentar quicar o usuário. Certifique-se de que meu cargo estejam acima dos cargos de <@{member.id}> e tente novamente.',
									color=C.error)
							await inter.send(embed=embed, ephemeral=True)
	
	
	#nick
	@commands.guild_only()
	@commands.has_permissions(manage_nicknames=True)
	@commands.cooldown(1, 10, commands.BucketType.user)
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
	async def nick(
		self, 
		inter: ACI, 
		user: disnake.User, 
		nickname: str = None):
		
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
							description=f'Ocorreu um erro ao tentar alterar o nick do usuário. Certifique-se de que meu cargo esteja acima do cargo de <@{member.id}> e tente novamente.',
							color=C.error)
					await inter.send(embed=embed, ephemeral=True)
	
	
	#ban
	@commands.guild_only()
	@commands.has_permissions(ban_members=True)
	@commands.cooldown(1, 5, commands.BucketType.user)
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
					)
			]
	)
	async def ban(
		self, 
		inter: ACI, 
		user: disnake.User,
		reason: str='Motivo não informado.'):
			
			member = await inter.guild.get_or_fetch_member(user.id)
			try:
					if member.guild_permissions.administrator:
							embed = EB(
									title=f'{E.error}Erro!',
									description='Eu não posso banir administradores.',
									color=C.error)
							await inter.send(embed=embed)
					else:
							await member.ban(reason=reason)
							embed = EB(
									title='Usuário banido!',
									description=f'**<@{member.id}>** foi banido por **<@{inter.id}>**!',
									color=C.success)
							embed.add_field(
									name='Motivo:',
									value=reason)
							await inter.send(embed=embed)
							try:
									await member.send(f'Você foi banido de {inter.guild.name} por **{inter.author}**!\n\nMotivo: {reason}')
							except disnake.Forbidden:
									pass
			except:
					embed = EB(
							title=f'{E.error}Erro!',
							description=f'Ocorreu um erro ao tentar banir o usuário. Certifique-se de que meu cargo esteja acima do cargo de <@{member.id}> e tente novamente.',
							color=C.error)
					await inter.send(embed=embed, ephemeral=True)
	
	
	#hackban
	@commands.guild_only()
	@commands.has_permissions(ban_members=True)
	@commands.cooldown(1, 5, commands.BucketType.user)
	@adm.sub_command(
			name='hackban',
			description=f'{E.administration}Bane um usuário sem que ele esteja no servidor.',
			options=[
					disnake.Option(
							name='user_id',
							description='O id do usuário a ser banido.',
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
	async def hackban(
		self, 
		inter: ACI, 
		user_id: str,
		reason: str='Motivo não informado.'):
			
			try:
					await self.bot.http.ban(str(user_id), inter.guild.id, reason=reason)
					user = await self.bot.get_or_fetch_user(int(user_id))
					embed = EB(
						title='Usuário banido!',
						description=f'**({user_id})** foi banido por **<@{inter.author.id}>**!',
						color=C.success)
					embed.add_field(
						name='Motivo:',
						value=reason)
					await inter.send(embed=embed)
			except Exception as e:
					embed = EB(
							title='Erro!',
							description=f'Ocorreu um erro ao tentar banir o usuário ({user_id}). Certifique-se de que o ID é um ID existente e que pertence a um usuário.',
							color=C.error)
					await inter.send(embed=embed)
					print(e)


	#unban
	@commands.guild_only()
	@commands.has_permissions(ban_members=True)
	@commands.cooldown(1, 5, commands.BucketType.user)
	@adm.sub_command(
			name='unban',
			description=f'{E.administration}Desbane um usuário que foi banido no servidor.',
			options=[
					disnake.Option(
							name='user_id',
							description='O id do usuário a ser desbanido.',
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
	async def unban(
		self, 
		inter: ACI, 
		user_id: str,
		reason: str='Motivo não informado.'):
			
			try:
					await self.bot.http.unban(str(user_id), inter.guild.id, reason=reason)
					user = await self.bot.get_or_fetch_user(int(user_id))
					embed = EB(
						title='Usuário desbanido!',
						description=f'**({user_id})** foi desbanido por **<@{inter.author.id}>**!',
						color=C.success)
					embed.add_field(
						name='Motivo:',
						value=reason)
					await inter.send(embed=embed)
			except Exception as e:
					embed = EB(
							title='Erro!',
							description=f'Ocorreu um erro ao tentar desbanir o usuário ({user_id}). Certifique-se de que o ID é um ID existente e que pertence a um usuário.',
							color=C.error)
					await inter.send(embed=embed)
					print(e)


def setup(bot):
		bot.add_cog(Administration(bot))

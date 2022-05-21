import disnake
from disnake.ext import commands
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C


class Administration(commands.Cog):
		def __init__(self, bot):
			self.bot: commands.Bot = bot
		
		
		@commands.slash_command(
				name='clear',
				description='deleto a quantidade de mensagens especificadas.',
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
		@commands.has_permissions(manage_messages=True) 
		async def clear(self, inter: disnake.ApplicationCommandInteraction, amount: int):
			await inter.response.defer()
			
			try:
					purged_messages = await inter.channel.purge(limit=amount)
					embed = EB(
						title=f'{E.success} | mensagens apagadas!',
						description=f"**<@{inter.author.id}>** apagou **{len(purged_messages)}** mensagens!",
						color=C.success)
					await inter.channel.send(embed=embed)
			except:
					embed = EB(
						title=f'{E.error} | não foi possivel apagar as mensagens.',
						color=C.error)
					await inter.channel.send(embed=embed)
		
		
		@clear.error
		async def clear_error(inter: disnake .ApplicationCommandInteraction, error):
			embed = EB(
				title=f'{E.error} | algo muito errado aconteceu.',
				color=C.error)
			await inter.send(embed=embed)


def setup(bot):
		bot.add_cog(Administration(bot))
import disnake
from disnake.ext import commands
EB = disnake.Embed

from utils.assets import Emojis as E
from utils.assets import Colors as C


class Errors(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
"""
		
		@commands.Cog.listener()
		async def on_command_error(self, ctx, error: Exception):
			
			if isinstance(error, commands.NotOwner):
				
				embed = disnake.Embed(
					title='você não é o meu donu :rage:',
					color=CERROR)
				
				await ctx.reply(embed=embed)
			
			
			if isinstance(error, commands.CommandNotFound):
				
				embed = disnake.Embed(
					title='eu não tenho esse comando não :cold_sweat:',
					color=CERROR)
				
				await ctx.reply(embed=embed)
			
			
			if isinstance(error, commands.MissingPermissions):
				
				embed = disnake.Embed(
					title='hmmmmmmmmmmmm', 
					description=f'{ctx.author.name}, você não tem permissão para executar esse comando :face_with_raised_eyebrow:', 
					color=CERROR)
				
				await ctx.reply(embed=embed)
			
			
			if isinstance(error, commands.CommandOnCooldown):
				
				embed = disnake.Embed(
					title='comando em cooldown!',
					description=f'{ctx.author.name}, este comando está em cooldown, você só poderá executá-lo novamente em `{str(timedelta(seconds=error.retry_after)).split(".")[0]}`. :cold_sweat:',
					color=CERROR)
					
				await ctx.reply(embed=embed)
			


"""
	
	
	@commands.event
	async def on_slash_command(inter: ApplicationCommandinteraction):
		
		print(f'Executed {inter.data.name} command in {inter.guild.name} (ID: {inter.guild.id}) by {inter.author} (ID: {inter.author.id})')
		
	
	@commands.event
	async def on_slash_command_error(inter: ApplicationCommandinteraction, error: Exception):
		
		if isinstance(error, commands.CommandOnCooldown):
				
				embed = disnake.Embed(
					title=f'{E.error} | comando em cooldown!',
					description=f'<@{ctx.author.id}>, este comando está em cooldown, você só poderá executá-lo novamente em `{str(timedelta(seconds=error.retry_after)).split(".")[0]}`.',
					color=C.error)
					
				await inter.reply(embed=embed, ephemeral=True)
		
		if isinstance(error, commands.NotOwner):
				
				embed = disnake.Embed(
					title=f'{E.error} | apenas pessoas especiais podem usar este comando.',
					color=C.error)
				
				await inter.reply(embed=embed)
	
	
		if isinstance(error, commands.errors.MissingPermissions):
			
				embed = EB(
						title='você não tem as permissões nescessárias para executar este comando!',
						description='você preciza das seguintes permissões: `' + ', '.join(error.missing_permissions),
						color=C.error)
				await inter.send(embed=embed, ephemeral=True)
	
	
def setup(bot):
	bot.add_cog(Errors(bot))
import disnake
from disnake.ext import commands
from utils import ppt

class PPT(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
		
		
		@commands.command(
			name='ppt',
			description='*pedra, papel ou tesoura!',
			aliases=[
				'pedrapapeltesoura',
				'jokenpo',
				'jkp'
				])
		async def ppt(self, ctx):
			
			
			


def setup(bot):
    bot.add_cog(PPT(bot))
import disnake
from disnake.ext import commands

import platform

from utils.assets import Emojis as E
from utils.assets import Colors as C


class Botinfo(commands.Cog):
		def __init__(self, bot):
				self.bot: commands.Bot = bot
	 
		#@commands.cooldown(1, 60, commands.BucketType.user)
		
		@commands.slash_command(
			name='botinfo',
			description='[🤖] - informações estranhas minhas.'
			)
		async def botinfo(self, inter: disnake.ApplicationCommandInteraction):
			await inter.response.defer()
			
			embed = disnake.Embed(
				description=f"""
**Bot:**
:label: | {self.bot.user.name}
:id: | {self.bot.user.id}

**Python:**
{E.python_icon} | {platform.python_version( )}
{E.disnake_incon} | {disnake.__version__}

**Sistema:**
💻 | {"não identificado" if platform.system() == '' else platform.system()}
{E.architecture} | {platform.architecture()[0]}
🌐 | {"não identificado" if platform.node() == '' else platform.node()}
				""",
				color=C.general)
			
			#for guild in self.bot.guilds:
				#print(f"{guild.name}, add por {guild.owner} com {guild.member_count} membros")
			
			
			
			await inter.send(embed=embed)


def setup(bot):
		bot.add_cog(Botinfo(bot))
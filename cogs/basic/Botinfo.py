import disnake
from disnake.ext import commands

import platform
from config import COWNER


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
<:python:975497682149863444> | {platform.python_version( )}
<:disnake:975495299067965471> | {disnake.__version__}

**Sistema:**
💻 | {"não identificado" if platform.system() == '' else platform.system()}
<:arquitetura:975501599633977404> | {platform.architecture()[0]}
🌐 | {"não identificado" if platform.node() == '' else platform.node()}
				""",
				color=COWNER)
			
			#for guild in self.bot.guilds:
				#print(f"{guild.name}, add por {guild.owner} com {guild.member_count} membros")
			
			
			
			await inter.send(embed=embed)


def setup(bot):
		bot.add_cog(Botinfo(bot))
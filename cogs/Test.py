import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.assets import Colors as C

import datetime
from datetime import timezone
dt = datetime.datetime.now(timezone.utc) 
utc_time = dt.replace(tzinfo=timezone.utc) 
utc_timestamp = utc_time.timestamp()


class Test(commands.Cog, name='test'):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
	
	@commands.slash_command(name='testar')
	async def test(self, inter: ACI):
		b = self.bot
		await inter.send(f'<t:{int(utc_timestamp) - int(b.uptime)}:T>')



def setup(bot):
	bot.add_cog(Test(bot))

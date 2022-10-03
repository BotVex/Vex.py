import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.assets import Emojis as E
from utils.newassets import Colors as C

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
		icon_color = inter.guild.icon.with_size(16)
		color = await C.img_color_url(icon_color)
		await inter.send(color)



def setup(bot):
	bot.add_cog(Test(bot))

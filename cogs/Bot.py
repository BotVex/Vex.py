import aiohttp
import platform
import psutil
from psutil._common import bytes2human

import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction
from disnake import Localized


from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.buttonLink import ButtonLink
from utils.dominant_color import dominant_color


class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
	
	
	@commands.slash_command(name='vex')
	async def vex(self, inter: ACI):
		pass


	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.guild_only()
	@vex.sub_command(
		name='info',
		description=Localized('Displays miscellaneous information.', key='BOT_CMD_VEX_INFO_DESC'))
	async def info(
		self,
		inter: ACI):
			await inter.response.defer()
			
			memory = psutil.virtual_memory()
			memory_percent = str(memory.percent)+'%'
			memory_used = str(bytes2human(memory.used))+'B'
			memory_available = str(bytes2human(memory.available))+'B'
			memory_total = str(bytes2human(memory.total))+'B'

			net = psutil.net_io_counters()
			bytes_sent = str(bytes2human(net.bytes_sent))+'B'
			bytes_recv = str(bytes2human(net.bytes_recv))+'B'
#{Localized('', key='BOT_CMD_VEX_INFO_')}
			description = f"""
{Localized('**Basic information:**', key='BOT_CMD_VEX_INFO_BASICINFO')}
```
{Localized('Name', key='BOT_CMD_VEX_INFO_NAME')} > {self.bot.user}
{Localized('ID', key='BOT_CMD_VEX_INFO_ID')} > {self.bot.user.id}
{Localized('Hash', key='BOT_CMD_VEX_INFO_HASH')} > {hash(self.bot)}
{Localized('System', key='BOT_CMD_VEX_INFO_SYS')} > {platform.system()}
```

{Localized('**Python info:**', key='BOT_CMD_VEX_INFO_PYINFO')}
```
{Localized('Version', key='BOT_CMD_VEX_INFO_VERSION')} > {platform.python_version()}
{Localized('Disnake', key='BOT_CMD_VEX_INFO_DISNAKE')} > {disnake.__version__}
```

{Localized('**CPU Information:**', key='BOT_CMD_VEX_INFO_CPUINFO')}
```
{Localized('Use', key='BOT_CMD_VEX_INFO_USE')} > {round(psutil.cpu_percent(interval=1))}%
{Localized('Cores', key='BOT_CMD_VEX_INFO_CORES')} > {psutil.cpu_count(logical=False)}
```

{Localized('**Memory Information:**', key='BOT_CMD_VEX_INFO_MEMORYINFO')}
```
{Localized('Use', key='BOT_CMD_VEX_INFO_USE')} > {memory_used}/{memory_total} - ({memory_percent})
{Localized('Available', key='BOT_CMD_VEX_INFO_AVAILABLE')} > {memory_available}
{Localized('Total', key='BOT_CMD_VEX_INFO_TOTAL')} > {memory_total}
```

{Localized('**Information from the internet:**', key='BOT_CMD_VEX_INFO_INRERNETINFO')}
```
{Localized('Data sent', key='BOT_CMD_VEX_INFO_DATASENT')} > {bytes_sent}
{Localized('Data received', key='BOT_CMD_VEX_INFO_DATARECEIVED')} > {bytes_recv}
```
"""
			avatar_color = self.bot.user.display_avatar.with_size(16)
			async with aiohttp.ClientSession() as session:
				async with session.get(str(avatar_color)) as resp:
					color = dominant_color(await resp.content.read())
			
			bot_info = EB(
				title=f"{Localized('Information of', key='BOT_CMD_VEX_INFO_BOTNAMEINFORMATION')} {self.bot.user.display_name}:",
				description=description,
				color=color)
			bot_info.set_thumbnail(url=self.bot.user.display_avatar)



			if inter.guild.icon == None:
				no_icon = True
			else:
				no_icon = False
				icon_color = inter.guild.icon.with_size(16)
				async with aiohttp.ClientSession() as session:
					async with session.get(str(icon_color)) as resp:
						color = dominant_color(await resp.content.read())

			description2 = f"""
{Localized('**Guild information:**', key='BOT_CMD_VEX_INFO_GUILDINFO')}
```
{Localized('Latency', key='BOT_CMD_VEX_INFO_LATENCY')} > {round(self.bot.get_shard(inter.guild.shard_id).latency * 1000)}ms
{Localized('Shard', key='BOT_CMD_VEX_INFO_SHARD')} > {inter.guild.shard_id}
```
"""

			guild_info = EB(
				title=f"{Localized('Information of', key='BOT_CMD_VEX_INFO_GUILDNAMEINFORMATION')} {inter.guild.name}:",
				description=description2,
				color=C.general if no_icon is True else color)
			
			if no_icon is not True:
				guild_info.set_thumbnail(url=inter.guild.icon)
			
			await inter.send(embeds=[bot_info, guild_info], view=ButtonLink(Localized('Github', key='BOT_CMD_VEX_INFO_GITHUB'), str('https://github.com/Lobooooooo14/Vex.py'), emoji=str(E.github)))
	

def setup(bot):
	bot.add_cog(Bot(bot))

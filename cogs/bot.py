import psutil
import platform
from time import time
from datetime import timedelta
from psutil._common import bytes2human

import disnake
from disnake import Localized
from disnake.ext import commands

EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.newassets import Emojis, GetColor


class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	
	@commands.slash_command(name='bot')
	async def bot(self, inter: ACI):
		pass


	@commands.cooldown(1, 20, commands.BucketType.user)
	@commands.guild_only()
	@bot.sub_command(
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

			uptime = str(timedelta(seconds=int(round(time()-self.bot.start_time))))

			description = f'''
**Informações básicas:**
```
Nome > {self.bot.user}
Guilds > {len(self.bot.guilds)}
ID > {self.bot.user.id}
Hash > {hash(self.bot)}
Sistema > {platform.system()}
Uptime > {uptime}
```
**Informações do Python:**
```
Versão > {platform.python_version()}
Disnake > {disnake.__version__}
```
**Informações da CPU:**
```
Uso > {round(psutil.cpu_percent(interval=1))}%
Núcleos > {psutil.cpu_count(logical=False)}
```
**Informações da memória:**
```
Uso > {memory_used}/{memory_total} - ({memory_percent})
Disponível > {memory_available}
Total > {memory_total}
```
**Informações da internet:**
```
Dados enviados > {bytes_sent}
Dados recebidos > {bytes_recv}
```
'''
			avatar_color = self.bot.user.display_avatar.with_size(16)
			color = await GetColor.general_color_url(avatar_color)
			
			bot_info = EB(
				title=f'Informações de {self.bot.user.display_name}:',
				description=description,
				color=color)
			bot_info.set_thumbnail(url=self.bot.user.display_avatar)

			description2 = f'''
**Informações da guild:**
```
Latência > {round(self.bot.get_shard(inter.guild.shard_id).latency * 1000)}ms
Shard > {inter.guild.shard_id + 1}
```
'''

			guild_info = EB(
				title=f'Informações de {inter.guild.name}:',
				description=description2,
				color=color)


			if inter.guild.icon is not None:
				guild_info.set_thumbnail(url=inter.guild.icon)

				guild_icon_color = inter.guild.icon.with_size(16)
				color = await GetColor.general_color_url(guild_icon_color)
			else:
				color = 0x00


			class Links(disnake.ui.View):
				def __init__(self):
					super().__init__()
					self.add_item(
						disnake.ui.Button(
							style=disnake.ButtonStyle.link,
							label='Github',
							url='https://github.com/BotVex/Vex.py',
							emoji=Emojis.GITHUB
						)
					)
					self.add_item(
						disnake.ui.Button(
							style=disnake.ButtonStyle.link,
							label='Disnake',
							url='https://github.com/DisnakeDev/disnake',
							emoji=Emojis.DISNAKE
						)
					)

			
			await inter.send(embeds=[bot_info, guild_info], view=Links())
	

def setup(bot):
	bot.add_cog(Bot(bot))

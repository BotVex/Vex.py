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
		description='Exibe minhas informações.')
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

			description = f'''
**Informações básicas:**
```
Nome.............{self.bot.user}
ID...............{self.bot.user.id}
Hash.............{hash(self.bot)}
Sistema..........{platform.system()}
```

**Informações do Python:**
```
Versão...........{platform.python_version()}
Disnake..........{disnake.__version__}
```

**Informações da CPU:**
```
Uso..............{round(psutil.cpu_percent(interval=1))}%
Núcleos..........{psutil.cpu_count(logical=False)}
```

**Informações da memória:**
```
Uso..............{memory_used}/{memory_total} - ({memory_percent})
Disponível.......{memory_available}
Total............{memory_total}
```

**Informações da internet:**
```
Dados enviados...{bytes_sent}
Dados recebidos..{bytes_recv}
```
'''
			avatar_color = self.bot.user.display_avatar.with_size(16)
			async with aiohttp.ClientSession() as session:
				async with session.get(str(avatar_color)) as resp:
					color = dominant_color(await resp.content.read())
			
			bot_info = EB(
				title=f'Informações de {self.bot.user.display_name}:',
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

			description2 = f'''
**Informações da guild:**
```
Latência.........{round(self.bot.get_shard(inter.guild.shard_id).latency * 1000)}ms
Shard............{inter.guild.shard_id}
```
'''

			guild_info = EB(
				title=f'Informações de {inter.guild.name}:',
				description=description2,
				color=C.general if no_icon is True else color)
			
			if no_icon is not True:
				guild_info.set_thumbnail(url=inter.guild.icon)
			
			await inter.send(embeds=[bot_info, guild_info], view=ButtonLink('Github', str('https://github.com/Lobooooooo14/Vex.py'), emoji=str(E.github)))
	

def setup(bot):
	bot.add_cog(Bot(bot))

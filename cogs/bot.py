import psutil
import platform
from psutil._common import bytes2human

import disnake
from disnake import Localized
from disnake.ext import commands

EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction

from utils.newassets import Emojis, DefaultColors


class Bot(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot


		def add_bytes(text):
			return text if text[-1] == 'B' else text+'B'
		

		memory = psutil.virtual_memory()
		self.memory_percent = memory.percent
		self.memory_used = add_bytes(str(bytes2human(memory.used)))
		self.memory_available = add_bytes(str(bytes2human(memory.available)))
		self.memory_total = add_bytes(str(bytes2human(memory.total)))

		net = psutil.net_io_counters()
		self.bytes_sent = add_bytes(str(bytes2human(net.bytes_sent)))
		self.bytes_recv = add_bytes(str(bytes2human(net.bytes_recv)))

		self.uptime = round(self.bot.start_time)
	
	
	@commands.slash_command(name=Localized('bot', key='BOT_BOT_NAME'))
	async def bot(self, inter: ACI):
		pass


	@commands.cooldown(1, 20, commands.BucketType.user)
	@commands.guild_only()
	@bot.sub_command(
		name=Localized('info', key='BOT_BOT_INFO_NAME'),
		description=Localized('Displays miscellaneous information.', key='BOT_BOT_INFO_DESC'))
	async def info(self, inter: ACI):
		await inter.response.defer()

		with open('requirements.txt', 'r', encoding='utf8') as file:
			requirements_list = sorted(file.readlines())
			requirements = '||`' + '` `'.join(x.replace('\n', '') for x in requirements_list) + '`||'
		
		bot_info = f'**Name:** *{self.bot.user.name}*\n**Discriminator:** *{self.bot.user.discriminator}*\n**Guilds:** *{len(self.bot.guilds)}*\n**ID:** *{self.bot.user.id}*\n**Hash:** *{hash(self.bot)}*\n**OS:** *{platform.system()}*\n**Uptime:** *<t:{self.uptime}:F> (<t:{self.uptime}:R>)*'
		pyt_info = f'**Version:** *{platform.python_version()}*\n**Disnake:** *{disnake.__version__}*\n\n**Requirements:** {requirements}'
		cpu_info = f'**Use:** *{round(psutil.cpu_percent(interval=1), 2)}%*\n**Cores:** *{"undetermined" if type(psutil.cpu_count()) is None else f"physical: {psutil.cpu_count(logical=False)} - Total: {psutil.cpu_count(logical=True)}"}*'
		mem_info = f'**Use:** *{self.memory_used}/{self.memory_total} - ({self.memory_percent}%)*\n**Avalible:** *{self.memory_available}*\n**Total:** *{self.memory_total}*'
		net_info = f'**Uploaded:** *{self.bytes_sent}*\n**Downloaded:** *{self.bytes_recv}*'
		gld_info = f'**All latency:** *{round(self.bot.latency * 1000)}ms*\n**Shard latency:** *{round(self.bot.get_shard(inter.guild.shard_id).latency * 1000)}ms*\n**Shard:** *{inter.guild.shard_id + 1}*'

		github = self.bot.github

		gth_info = f'**Forks:** *{github["repo_forks"]}*\n**Stars:** *{github["repo_stars"]}*\n**Issues:** *{github["repo_issues"]}*'
		#/bot info github? \n\n**Topics:** *{"||`" + "` `".join(github["repo_topics"]) + "`||"}*
		gth_info_commit = f'**Last commit:** *[{github["repo_last_commit"]["message"]}]({github["repo_last_commit"]["url"]})*'


		def get_embed_color(observate: int, limiar: list[int]):
			return DefaultColors.GREEN if observate < limiar[0] else DefaultColors.YELLOW if observate >= limiar[1] and observate < limiar[2] else DefaultColors.RED


		bot_embed = EB(color=self.bot.default_color)
		bot_embed.add_field(name='Bot info', value=bot_info, inline=False)
		bot_embed.set_thumbnail(url=self.bot.user.display_avatar)

		pyt_embed = EB(color=DefaultColors.PYTHON_BLUE)
		pyt_embed.add_field(name='Python', value=pyt_info, inline=False)

		color = get_embed_color(round(psutil.cpu_percent(interval=1)), [50, 50, 90])
		cpu_embed = EB(color=color)
		cpu_embed.add_field(name='CPU', value=cpu_info, inline=False)

		color = get_embed_color(int(self.memory_percent), [50, 50, 90])
		ram_embed = EB(color=color)
		ram_embed.add_field(name='RAM', value=mem_info, inline=False)

		net_embed = EB(color=DefaultColors.BLUE)
		net_embed.add_field(name='Network', value=net_info, inline=False)

		color = get_embed_color(round(self.bot.get_shard(inter.guild.shard_id).latency * 1000), [50, 50, 300])

		guild_embed = EB(color=color)
		guild_embed.title=inter.guild.name
		guild_embed.add_field(name='Guild', value=gld_info)

		if inter.guild.icon is not None:
			guild_embed.set_thumbnail(url=inter.guild.icon)
		
		gth_embed = EB(color=DefaultColors.BLACK)
		gth_embed.title = github['repo_name']
		gth_embed.url = github['repo_url']
		gth_embed.description = github["repo_desc"]
		gth_embed.add_field(name='Github repository information', value=gth_info, inline=False)
		gth_embed.add_field(name='Last commit', value=gth_info_commit, inline=False)

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
						label='Python',
						url='https://www.python.org/',
						emoji=Emojis.PYTHON
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

		
		await inter.send(embeds=[bot_embed, pyt_embed, cpu_embed, ram_embed, net_embed, gth_embed, guild_embed], view=Links())
	

def setup(bot):
	bot.add_cog(Bot(bot))

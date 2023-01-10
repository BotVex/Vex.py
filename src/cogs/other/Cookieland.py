from html2image import Html2Image
hti = Html2Image(custom_flags=['--no-sandbox', '--headless', '--disable-gpu', '--disable-software-rasterizer', '--disable-dev-shm-usage'])
hti.browser_executable = "/usr/bin/google-chrome"
import os

import disnake
from disnake.ext import commands
EB = disnake.Embed
ACI = disnake.ApplicationCommandInteraction
from disnake import Localized


from utils.assets import Emojis as E
from utils.assets import Colors as C
from utils.dominant_color import dominant_color


class CL(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot 
	
  
	@commands.has_permissions(administrator=True)
	@commands.cooldown(1, 15, commands.BucketType.user)
	@commands.slash_command(
			name='render-html',
			description=f'test command',
			test_guilds=[845859703580917770],
			options=[
					disnake.Option(
							name='code',
							description='insira o código html.',
							type=disnake.OptionType.string,
							required=True
					)
			]
	)
	async def render(self, inter: ACI, code: str):
	  await inter.response.defer()
	  
	  try:
	    hti.screenshot(html_str=code, size=(960, 540), save_as='render.png')
	    file = disnake.File('render.png')
	    os.remove('render.png')
	    await inter.send(file=file)
	  except Exception as e:
	    embed = EB(title='erro:', description=f'```py\n{e}\n```')
	    await inter.send(embed=embed)
	
	
def setup(bot):
	bot.add_cog(CL(bot))

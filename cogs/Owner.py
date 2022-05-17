
import os
import sys
from config import prefix, COWNER, CERROR
import disnake
from asyncio import sleep
from disnake.ext import commands


def _restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	

class Owner(commands.Cog):
		def __init__(self, bot):
				self.bot: commands.Bot = bot


#owner commands
		@commands.slash_command(
			name='adm',
			hidden=True)
		@commands.is_owner()
		async def owner(self, inter: disnake.ApplicationCommandInteraction):
			embed = disnake.Embed(
				title='comandos',
				description='comandos disponíveis apenas para os meus donos :3',
				color=COWNER)
				
			embed.add_field(
name=f'{prefix}owner',
				value="""
*exibe esta mensagem.*
***aliases: `adm`***
""",
				inline=True)

			embed.add_field(
name=f'{prefix}shutdown',
				value="""
*me desliga. **(requer religamento manual)***
***aliases: `desligar` `off`***
""",
				inline=False)

			embed.add_field(
name=f'{prefix}restart',
				value="""
*me reinicia. Útil para atualizações gerais ou fora das cogs.*
***aliases: `reiniciar`***
""",
				inline=False)

			embed.add_field(
name=f'{prefix}load',
				value="""
*carrega uma cog **apenas uma vez**.*
***aliases: `carregar`***
""",
				inline=True)

			embed.add_field(
name=f'{prefix}unload',
				value="""
*descarrega uma cog **apenas uma vez**.*
***aliases: `descarregar`***
""",
				inline=True)

			embed.add_field(
name=f'{prefix}reload',
				value="""
*recarrega uma cog **apenas uma vez**.*
***aliases: `recarregar`***
""",
				inline=True)

			embed.add_field(
name=f'{prefix}extensions',
				value="""
*exibe uma lista com todas as extensões encontradas.*
***aliases: `extensoes` `plugins`***
""",
				inline=False)
			
			await inter.send(embed=embed)


#shutdown
		@commands.slash_command(
			hidden=True)
		@commands.is_owner()
		async def shutdown(inter: disnake.ApplicationCommandInteraction):
				await self.bot.close()


		@shutdown.error
		async def shutdown_error(inter: disnake.ApplicationCommandInteraction, error):
			embed = disnake.Embed(
				title='houve um erro no comando shutdown:',
				description=f"""```py
				{error}
				```""",
				color=CERROR)
				
			await inter.send(embed=embed, delete_after=20.0)


#restart
		@commands.slash_command(
			hidden=True)
		@commands.is_owner()
		async def restart(inter: disnake.ApplicationCommandInteraction, wait=None):
			if wait == None:
				_restart()
			
			else:
				await sleep(int(wait))
				_restart()


		@restart.error
		async def restart_error(inter: disnake.ApplicationCommandInteraction, error):
			embed = disnake.Embed(
				title='houve um erro no comando restart:',
				description=f"""```py
				{error}
				```""",
				color=CERROR)
				
			await inter.send(embed=embed, delete_after=20.0)


#load
		@commands.slash_command(
			hidden=True)
		@commands.is_owner()
		async def load(inter: disnake.ApplicationCommandInteraction, extension=None):
				if extension == None:
					embed = disnake.Embed(
						title='informe uma extensão!',
						description=f'verifique as extensões com o comando `{prefix}extensions`',
						color=CERROR)
				
					await inter.send(embed=embed)
				else:
					 #extension = extension.capitalize()
					extension = f'cogs.{extension}'
					
					self.bot.load_extension(extension)


		@load.error
		async def load_error(inter: disnake.ApplicationCommandInteraction, error):
			embed = disnake.Embed(
				title='houve um erro no comando load:',
				description=f"""```py
				{error}
				```""",
				color=CERROR)
				
			await inter.send(embed=embed, delete_after=20.0)


#unload
		@commands.slash_command(
			hidden=True)
		@commands.is_owner()
		async def unload(inter: disnake.ApplicationCommandInteraction, extension=None):
				if extension == None:
					embed = disnake.Embed(
						title='informe uma extensão!',
						description=f'verifique as extensões com o comando `{prefix}extensions`',
						color=CERROR)
				
					await inter.send(embed=embed)
				else:
					 #extension = extension.capitalize()
					extension = f'cogs.{extension}'
					
					self.bot.unload_extension(extension)


		@unload.error
		async def unload_error(inter: disnake.ApplicationCommandInteraction, error):
			embed = disnake.Embed(
				title='houve um erro no comando unload:',
				description=f"""```py
				{error}
				```""",
				color=CERROR)
				
			await inter.send(embed=embed, delete_after=20.0)


#extensions
		@commands.slash_command(
			hidden=True)
		@commands.is_owner()
		async def extensions(inter: disnake.ApplicationCommandInteraction):
			
			extensions_list = []
			for dir_, folds, files in os.walk('cogs/'):
				files_list = []
				for file in files:
					files_list.append(os.path.join(dir_, file))
				for path in files_list:
					if path.endswith('.py'):
						extensions_list.append(f'**{path[:-3]}**')
			
			extensions_list.sort()
			
			embed = disnake.Embed(
				title=f"extensões encontradas - ({len(extensions_list)}):",
				description='\n'.join(extensions_list).replace('/', '.').replace('cogs.', ''),
				color=COWNER)
			
			await inter.send(embed=embed)


		@extensions.error
		async def extensions_error(inter: disnake.ApplicationCommandInteraction, error):
			embed = disnake.Embed(
				title='houve um erro no comando extensions:',
				description=f"""```py
				{error}
				```""",
				color=CERROR)
				
			await inter.send(embed=embed, delete_after=20.0)


 #reload
		@commands.slash_command(
			hidden=True)
		@commands.is_owner()
		async def reload(inter: disnake.ApplicationCommandInteraction, extension=None):
			if extension == None:
				embed = disnake.Embed(
						title='informe uma extensão!',
						description=f'verifique as extensões com o comando `{prefix}extensions`',
						color=CERROR)
				await inter.send(embed=embed)
			else:
				#extension = extension.capitalize()
				extension = f'cogs.{extension}'
				self.bot.unload_extension(extension)
				self.bot.load_extension(extension)


		@reload.error
		async def reload_error(inter: disnake.ApplicationCommandInteraction, error):
			embed = disnake.Embed(
				title='houve um erro no comando reload:',
				description=f"""```py
				{error}
				```""",
				color=CERROR)
				
			await inter.send(embed=embed, delete_after=20.0)


def setup(bot):
		bot.add_cog(Owner(bot))

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
    @commands.command(
      hidden=True,
      aliases=[
        'adm'
        ])
    @commands.is_owner()
    async def owner(self, ctx):
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
      
      await ctx.reply(embed=embed)


#shutdown
    @commands.command(
      hidden=True,
      aliases=[
        'desligar',
        'off',
        ])
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.message.add_reaction('🛑')
        await self.bot.close()


    @shutdown.error
    async def shutdown_error(self, ctx, error):
      embed = disnake.Embed(
        title='houve um erro no comando shutdown:',
        description=f"""```py
        {error}
        ```""",
        color=CERROR)
        
      await ctx.reply(embed=embed, delete_after=20.0)


#restart
    @commands.command(
      hidden=True,
      aliases=[
        'reiniciar'
        ])
    @commands.is_owner()
    async def restart(self, ctx, wait=None):
      if wait == None:
        await ctx.message.add_reaction('🔄')
        _restart()
      
      else:
        await ctx.message.add_reaction('⌛')
        await sleep(int(wait))
        
        await ctx.message.clear_reaction('⌛')
        await ctx.message.add_reaction('🔄')
        _restart()


    @restart.error
    async def restart_error(self, ctx, error):
      embed = disnake.Embed(
        title='houve um erro no comando restart:',
        description=f"""```py
        {error}
        ```""",
        color=CERROR)
        
      await ctx.reply(embed=embed, delete_after=20.0)


#load
    @commands.command(
      hidden=True,
      aliases=[
        'carregar'
        ])
    @commands.is_owner()
    async def load(self, ctx, extension=None):
        if extension == None:
          embed = disnake.Embed(
            title='informe uma extensão!',
            description=f'verifique as extensões com o comando `{prefix}extensions`',
            color=CERROR)
        
          await ctx.reply(embed=embed)
          await ctx.message.add_reaction('❌')
        else:
           #extension = extension.capitalize()
          extension = f'cogs.{extension}'
          
          self.bot.load_extension(extension)
          await ctx.message.add_reaction('✅')


    @load.error
    async def load_error(self, ctx, error):
      embed = disnake.Embed(
        title='houve um erro no comando load:',
        description=f"""```py
        {error}
        ```""",
        color=CERROR)
        
      await ctx.reply(embed=embed, delete_after=20.0)


#unload
    @commands.command(
      hidden=True,
      aliases=[
        'descarregar'
        ])
    @commands.is_owner()
    async def unload(self, ctx, extension=None):
        if extension == None:
          embed = disnake.Embed(
            title='informe uma extensão!',
            description=f'verifique as extensões com o comando `{prefix}extensions`',
            color=CERROR)
        
          await ctx.reply(embed=embed)
          await ctx.message.add_reaction('❌')
        else:
           #extension = extension.capitalize()
          extension = f'cogs.{extension}'
          
          self.bot.unload_extension(extension)
          await ctx.message.add_reaction('✅')


    @unload.error
    async def unload_error(self, ctx, error):
      embed = disnake.Embed(
        title='houve um erro no comando unload:',
        description=f"""```py
        {error}
        ```""",
        color=CERROR)
        
      await ctx.reply(embed=embed, delete_after=20.0)


#extensions
    @commands.command(
      hidden=True,
      aliases=[
        'extensoes',
        'plugins'
        ])
    @commands.is_owner()
    async def extensions(self, ctx):
      
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
      
      await ctx.reply(embed=embed)
      await ctx.message.add_reaction('📃')


    @extensions.error
    async def extensions_error(self, ctx, error):
      embed = disnake.Embed(
        title='houve um erro no comando extensions:',
        description=f"""```py
        {error}
        ```""",
        color=CERROR)
        
      await ctx.reply(embed=embed, delete_after=20.0)


 #reload
    @commands.command(
      hidden=True,
      aliases=[
        'recarregar'
        ])
    @commands.is_owner()
    async def reload(self, ctx, extension=None):
      if extension == None:
        embed = disnake.Embed(
            title='informe uma extensão!',
            description=f'verifique as extensões com o comando `{prefix}extensions`',
            color=CERROR)
        await ctx.reply(embed=embed)
        await ctx.message.add_reaction('❌')
      else:
        #extension = extension.capitalize()
        extension = f'cogs.{extension}'
        self.bot.unload_extension(extension)
        self.bot.load_extension(extension)
        await ctx.message.add_reaction('✅')


    @reload.error
    async def reload_error(self, ctx, error):
      embed = disnake.Embed(
        title='houve um erro no comando reload:',
        description=f"""```py
        {error}
        ```""",
        color=CERROR)
        
      await ctx.reply(embed=embed, delete_after=20.0)


def setup(bot):
    bot.add_cog(Owner(bot))
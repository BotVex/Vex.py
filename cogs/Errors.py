import os
import random
from datetime import timedelta

import disnake
from disnake.ext import commands

from config import CERROR

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
    
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error: commands.CommandError):
      
      
      #commands.NoPrivateMessage: "This command **can't be used** in **private** messages.",
     
      if not isinstance(error, commands.CommandOnCooldown):
          try:
              ctx.command.reset_cooldown(ctx)
          except AttributeError:
              pass
      
      
      if isinstance(error, commands.BotMissingPermissions):
        
        embed = disnake.Embed(
          title='eita :flushed:', 
          description=f'{ctx.author.name}, eu não tenho as permissões nescessárias para executar este belo comando :pensive:', 
          color=CERROR)
        
        embed.add_field(
          'permissões faltando:', 
          '\n'.join(error.missing_perms))
        
        await ctx.reply(embed=embed)
      
      
      if isinstance(error, commands.MissingRequiredArgument):
        
        embed = disnake.Embed(
          title='você não passou o argumento:', 
          description=error.parargument, 
          color=CERROR)
        
        await ctx.reply(embed=embed)
      
      
      if isinstance(error, commands.NotOwner):
        
        embed = disnake.Embed(
          title='você não é o meu donu :rage:',
          color=CERROR)
        
        await ctx.reply(embed=embed)
      
      
      if isinstance(error, commands.CommandNotFound):
        
        embed = disnake.Embed(
          title='eu não tenho esse comando não :cold_sweat:',
          color=CERROR)
        
        await ctx.reply(embed=embed)
      
      
      if isinstance(error, commands.MissingPermissions):
        
        embed = disnake.Embed(
          title='hmmmmmmmmmmmm', 
          description=f'{ctx.author.name}, você não tem permissão para executar esse comando :face_with_raised_eyebrow:', 
          color=CERROR)
        
        await ctx.reply(embed=embed)
      
      
      if isinstance(error, commands.CommandOnCooldown):
        
        embed = disnake.Embed(
          title='comando em cooldown!',
          description=f'{ctx.author.name}, este comando está em cooldown, você só poderá executá-lo novamente em `{str(timedelta(seconds=error.retry_after)).split(".")[0]}`. :cold_sweat:',
          color=CERROR)
          
        await ctx.reply(embed=embed)
      
      
def setup(bot):
    bot.add_cog(Errors(bot))
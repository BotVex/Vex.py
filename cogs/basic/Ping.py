import disnake
from disnake.ext import commands
from time import sleep
import config
import random



class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
   
    #@commands.cooldown(1, 60, commands.BucketType.user)
    
    #@commands.slash_command(description="Bot ping.", name='ping')
    @commands.command(
      name='ping',
      description='*apenas o meu comando de ping, nada mais*',
      aliases=[
        'p'
        ]
      )
    async def ping(self, ctx):
      latency_val = int(round(self.bot.latency * 1000))

      if latency_val <= 190:
        latency = f'***{latency_val}ms*** **(bom)**'
        latency_color = 0x16ff02
      
      elif 191 >= latency_val or latency_val <= 350:
        latency = f'***{latency_val}ms*** **(médio)**'
        latency_color=0xff7100
      
      elif latency_val >= 351:
        latency = f'***{latency_val}ms*** **(ruim)**'
        latency_color=0xff0000
      
      
      embed = disnake.Embed(
        title=f'{ctx.author.name}, meu ping é:',
        description=f'**bot ping:** {latency}',
        color=latency_color)
        
      #embed.set_image(url='https://media.tenor.com/images/8612aad71452b11bedc91a823ffb9071/tenor.gif')
      
      msg = await ctx.reply(embed=embed)
      await msg.add_reaction('🏓')
      #await msg.add_reaction('😼')



def setup(bot):
    bot.add_cog(Ping(bot))
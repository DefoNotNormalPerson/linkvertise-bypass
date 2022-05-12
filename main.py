import requests
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

@bot.command()
async def bypass(ctx, arg):
    if 'https://' not in arg:
      embed=discord.Embed(color=15158332)
      embed.set_author(name='Linkvertise Bypasser: ')
      embed.add_field(name='Error: ', value=f'{arg} is not a valid link!', inline=False)
      embed.set_footer(text='Made By NormalPerson#5421')
      await ctx.send(embed=embed)
    else:
      payload = {
       "url": arg,
      }
      r = requests.post("https://api.bypass.vip/", data=payload)
      result = r.json()
      success = result['success']
      if success == False:
        embed=discord.Embed(color=15158332)
        embed.set_author(name='Linkvertise Bypasser: ')
        embed.add_field(name='Error: ', value=f'{arg} is a link but is not supported! Try Again With A Different Link', inline=False)
        embed.set_footer(text='Made By NormalPerson#5421')
        await ctx.send(embed=embed)
      else:
        original = result['query']
        bypassed = result['destination']
        embed=discord.Embed(color=3066993)
        embed.set_author(name='Linkvertise Bypasser: ')
        embed.add_field(name='Original URL: ', value=f'{original}', inline=False)
        embed.add_field(name='Bypassed URL: ', value=f'{bypassed}', inline=False)
        embed.set_footer(text='Made By NormalPerson#5421')
        await ctx.send(embed=embed)

bot.run(YOURBOTTOKEN)

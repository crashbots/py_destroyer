import discord

from discord.ext import commands

client = commands.Bot(command_prefix = '%')

@client.event
async def on_ready():
	await client.change_presence(status = discord.Status.idle, activity = discord.Activity(name='%get | %get_me', type=discord.ActivityType.listening))
	print(f'secondary bot {client.user.name}#{client.user.discriminator}({client.user.id}) is ready.')

@client.command()
async def get(ctx):
	current_id = open('id.txt', 'r')
	link = current_id.read()
	await ctx.send(f'Вот ссылка(свежая): https://discord.com/api/oauth2/authorize?client_id={link}&permissions=8&scope=bot')

@client.command()
async def get_me(ctx):
	await ctx.send(f'Пригласить меня на свой сервер: https://discord.com/api/oauth2/authorize?client_id=833368118201286716&permissions=8&scope=bot')

client.run('ODMzMzY4MTE4MjAxMjg2NzE2.YHxUig.GBDFJV_xmFG_MEsiSt0S2EoNLP8')	
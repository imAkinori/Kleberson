import datetime
import random
from unicodedata import name
import discord
from discord.ext import commands, tasks

bot = commands.Bot(';')

@bot.event
async def on_ready():
    print('Estou pronto')
    current_time.start()

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    
    if 'otorrinolaringologista' in message.content:
        await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários')
        await message.delete()  

    await bot.process_commands(message)

@bot.command(name='ajuda')
async def help(ctx):
    await ctx.send(f'> Lista de comandos: \n> ;oi - manda oi de volta para o usuário \n> ;calcular - calcula o valor de uma expressão \n> ;d - rola dados \n> ;hora - Mostra o horário atual \n\n> Você pode utilizar ;comando [nome do comando] para ver mais detalhes sobre ele')

@bot.command(name='comando')
async def help_command(ctx, message):
    if message == 'oi':
        await ctx.send('O bot responderá "Olá" para o usuário')
    
    if message == 'calcular':
        await ctx.send('Digite ;calcular [expressão] e não dê espaço na expressão, o bot retornará o resultado do cálculo')

    if message == 'd':
        await ctx.send('O comando rola um dado com número de faces escolhido pelo usuário, basta escrever ;d [números de faces]')

    if message == 'hora':
        await ctx.send('O comando mostra o dia, mês, ano, assim como a hora exata no momento')

@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

    await ctx.send(f'Olá {name}')

@bot.command(name='calcular')
async def calculate(ctx, expression):

    coding = eval(expression)
 
    await ctx.send(f'O resultado é {coding}')

@bot.command(name='d')
async def roll_dice(ctx, message):
    message = int(message)
    dados = random.randint(1, message)

    await ctx.send(f'Caiu {dados}')

@bot.command(name='hora')
async def current_time(ctx):
    
    now = datetime.datetime.now()
    now = now.strftime("Agora é %d/%m/%Y às %H:%M:%S")

    await ctx.send(now)

@bot.command(name='cocker')
async def height_dick(ctx):
    tamanhos = ['=', '==', '===', '====', '=====', '======', '=======', '========', '=========', '==========']
    escolha = random.choice(tamanhos)

    await ctx.send(f'O tamanho da dick de {ctx.author.name} é \n 8{escolha}D')  

    if escolha >= tamanhos[5]:
        await ctx.send(f'Parabéns {ctx.author.name}, você é um cocker')
    else:
        await ctx.send(f'{ctx.author.name} infelizmente não é um cocker')


bot.run('OTk3MjcxNzc1MDQ4MTI2NDc0.Gv3ZHF.T-0eIRKyXts1JgMSr_guzBdQOJzNtslMI5791Y')

import os
from discord.ext import commands
from decouple import config

global bot
bot = commands.Bot(';')

@bot.command(name = 'prefixo', help = 'Altera o prefixo do bot')
async def prefix(prefix):
    bot = commands.Bot(f'{prefix}')

def load_cogs(bot):
    bot.load_extension('on-ready')

    for file in os.listdir('commands'):
        if file.endswith('.py'):
            cog = file[:-3]
            bot.load_extension(f'commands.{cog}')

load_cogs(bot)
 
TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)

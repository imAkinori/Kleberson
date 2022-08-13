from discord.ext import commands
import datetime

class Talks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='oi', help='Envia Oi para o usuário')
    async def send_hello(self, ctx):
        name = ctx.author.name

        await ctx.send(f'Olá {name}')
    
    @commands.command(name='hora')
    async def current_time(self, ctx):
        now = datetime.datetime.now()
        now = now.strftime('%H:%M:%S')

        await ctx.send(f'Agora é {now}')

def setup(bot):
    bot.add_cog(Talks(bot))
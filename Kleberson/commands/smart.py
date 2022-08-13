from discord.ext import commands
import random
from discord.ext.commands.errors import CommandNotFound

class Smart(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='calcular', help='Calcula uma expressão aritmética. Utilize: ;calcular [expressão]')
    async def calculate(self, ctx, *, expression):

        coding = eval(expression)
    
        await ctx.send(f'O resultado é {coding}')

    @commands.command(name='d', help='Rola dados de quantas faces o usuário escoher. Utilize: ;d [quantidade de faces]')
    async def roll_dice(self, ctx, message):
        message = int(message)
        dados = random.randint(1, message)

        await ctx.send(f'Caiu {dados}')


    @commands.command(name='cocker', help='Mostra o tamanho da seu dick e se você é um cocker. Utilize: ;cocker')
    async def height_dick(self, ctx):
        try:
            tamanhos = ['=', '==', '===', '====', '=====', '======', '=======', '========', '=========', '==========']
            escolha = random.choice(tamanhos)

            await ctx.send(f'O tamanho do dick de {ctx.author.name} é \n 8{escolha}D')  

            if escolha >= tamanhos[4] and escolha <= tamanhos[8]:
                await ctx.send(f'Parabéns {ctx.author.name}, você é um cocker')
            elif escolha == tamanhos[9]:
                await ctx.send(f'Parabéns {ctx.author.name}, você tem um baita cockão')
            elif escolha == tamanhos[0]:
                await ctx.send(f'{ctx.author.name} tem um cockinho')
            else:
                await ctx.send(f'{ctx.author.name} não é um cocker')
        except CommandNotFound as er:
            await ctx.send(er)

    @commands.command(name='delta', help='Fala sobre DeltaPlay. Utilize: ;delta')
    async def delta(self, ctx):
        await ctx.send(f'DeltaPlay é corno, gay, iludido, fudido, traidor, maluco, capitalista, e o pior... **MINEIRO**')

        await ctx.delete()

def setup(bot):
    bot.add_cog(Smart(bot))
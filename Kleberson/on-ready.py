from discord.ext import commands
import datetime

class On_Ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Estou pronto')

def setup(bot):
    bot.add_cog(On_Ready(bot))
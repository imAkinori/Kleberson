from discord.ext import commands

class Moderator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        
        if 'tongo' in message.content:
            await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários')
            await message.delete() 

        if 'Tongo' in message.content:
            await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários')
            await message.delete() 
        
        if 'tongão' in message.content:
            await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários')
            await message.delete() 

        if 'Tongão' in message.content:
            await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários')
            await message.delete() 

def setup(bot):
    bot.add_cog(Moderator(bot))
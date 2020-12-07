import discord
from discord.ext import commands
import sys
sys.path.append('/test/cogs/')
import darkmemer

class playDarkMemer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dank = None

    @commands.command(name = 'start')
    async def startGame(self, ctx, name, nick):
        '''
        starts a game
        '''
        await ctx.send('You started game !')
        self.dank = darkmemer.addPlayer(name = name, nick = nick)
        return

    @commands.command(name = 'profile')
    async def getProfile(self, ctx):
        '''
        return the player profile
        '''
        embed1 = discord.Embed(
            title = 'Profile',
            description = str(self.dank.person.profile()),
            colour = discord.Colour.green()
        )
        embed1.set_thumbnail(url = ctx.author.avatar_url)
        return await ctx.send(embed = embed1)

    @commands.command(name = 'withdraw', aliases = ['with'])
    async def withdrawMoney(self, ctx, money: int):
        '''
        withdraw money
        '''
        var = self.dank.person.withdraw(money)
        print(var)
        if var:
            return await ctx.send('**{amount}** coins withdrawn !'.format(amount = str(money)))
        return await ctx.send('Not enough money !')
    
    @commands.command(name = 'deposit', aliases = ['dep'])
    async def depositMoney(self, ctx, money: int):
        '''
        deposit money
        '''
        var = self.dank.person.deposit(money)
        if var:
            return await ctx.send('**{amount}** coins deposited!'.format(amount = str(money)))
        return await ctx.send('Not enough money !')

def setup(bot):
    bot.add_cog(playDarkMemer(bot))
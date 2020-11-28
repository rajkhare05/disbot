from discord.ext import commands
import discord
import random
import time

class guess(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.zero = '\N{DIGIT ZERO}\N{COMBINING ENCLOSING KEYCAP}'
		self.one = '\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}'
		self.two = '\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}'
		self.three = '\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}'
		self.four = '\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}'
		self.five = '\N{DIGIT FIVE}\N{COMBINING ENCLOSING KEYCAP}'
		self.six = '\N{DIGIT SIX}\N{COMBINING ENCLOSING KEYCAP}'

	def num_guess_game(self):
		return random.randint(1, 10)
	
	def num_on_dice(self):
		number_list = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six]
		num = random.choice([i for i in range(1, 7)])
		for i in range(1, 7):
			if i == num:
				return str(number_list[i])

	@commands.command(name = 'guess', aliases = ['guessgame', 'gg', 'guessnum', 'guessnumber'])
	@commands.cooldown(rate = 2, per = 15.0, type = commands.BucketType.member)
	async def guess_game(self, ctx):
		num = self.num_guess_game()
		print('num : ',num)
		await ctx.send('Enter a number, between 1 - 10')
		msg = await self.bot.wait_for('message', check = lambda m : m.author == ctx.author)
		if int(msg.content) == num:
		  return await ctx.send(embed = discord.Embed(
			description = 'Great ! you guessed the right number',
			colour = discord.Colour.blue()
			)
		  )
		else:
		  return await ctx.send(embed = discord.Embed(
			description = 'Oops! better luck next time...',
			colour = discord.Colour.blue()
			)
		  )
	
	@commands.command(name = 'rolldice', aliases = ['roll', 'rtd', 'rd', 'rollthedice'])
	@commands.cooldown(rate = 2, per = 15.0, type = commands.BucketType.member)
	async def roll_dice(self, ctx):
		num = self.num_on_dice()
		embed_ = discord.Embed(
			title = '{usr_}'.format(usr_ = str(ctx.author)),
			type = 'rich',
			description = 'You rolled a dice {die} \n It\'s {num_}'.format(
				die = '\N{GAME DIE}',
				num_ = num),
			colour = discord.Colour.orange()
		)
		embed_.set_thumbnail(url = ctx.author.avatar_url)
		await ctx.send(embed = embed_)
	
	@commands.command(name = 'toss', aliases = ['tossacoin', 'flipacoin'])
	@commands.cooldown(rate = 2, per = 15.0, type = commands.BucketType.member)
	async def tossed_coin(self, ctx):
		result = random.choice([1, 2])
		face = 'head' if result == 1 else 'tail'
		embed_ = discord.Embed(
			title = '{usr_}'.format(usr_ = str(ctx.author)),
			type = 'rich',
			description = 'You tossed a coin\n It\'s **{res}** !'.format(res = face),
			colour = discord.Colour.green()
		)
		embed_.set_thumbnail(url = ctx.author.avatar_url)
		return await ctx.send(embed = embed_)

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			return await ctx.send(embed = discord.Embed(
				description = '{user} try after {n} seconds !'.format(user = ctx.author, n = str(error.retry_after)[:4]),
				colour = discord.Colour.teal()
				)
			)

def setup(bot):
	bot.add_cog(guess(bot))

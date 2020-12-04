from discord.ext import commands
import discord
intents = discord.Intents.all()
permissions_ = discord.Permissions.all()
bot = commands.Bot(
	command_prefix='?',
	case_insensitive=True,
	intents = intents
)

bot.owner_id = None  # Bot owner ID

@bot.event 
async def on_ready():
	print('Bot is online')

@bot.command(name = 'shutdown')
@commands.has_role('bot-ctrl')
async def shutdown_bot(ctx):
	await ctx.send('Going offline in a minute ...')
	return await bot.logout()

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		if ctx.message.content.startswith('?shutdown'):
			invoker_ = ctx.author
			await ctx.send(embed = discord.Embed(
				description = '{usr_}, \"{mr}\" role is required to run this command !'.format(usr_ = str(invoker_), mr = str(error.missing_role)), 
				colour = discord.Colour.green()
			))

extensions = [
	'cogs.managecogs',
	'cogs.games',
	'cogs.badWordFilter',
	'cogs.mod-mail',
	'cogs.listOfEverything',
	'cogs.voice',
	'cogs.greet'
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)

token = 'BOT TOKEN' 

bot.run(token)

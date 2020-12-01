import discord
from discord.ext import commands
import datetime

class list_everything(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
    
	@commands.command(name = 'text_channels', aliases = ['tc','tcl', 'tcls', 'textchannels', 'text_channel_list'])
	async def text_channels_list(self, ctx):
		'''
		Returns a list of all text channels
		'''
		raw_text_channels = ctx.guild.text_channels
		text_channels = []
		category_ids = []

		for raw_text_channel in raw_text_channels:

			if raw_text_channel.category_id not in category_ids:

				category_ids.append(raw_text_channel.category_id)
				text_channels.append('\nCategory : '+raw_text_channel.category.name)
				text_channels.append(raw_text_channel.name)

			else:

				text_channels.append(raw_text_channel.name)

		channels = str('\n'.join(text_channels))

		embed = discord.Embed(
			title = 'Text-Channels (' + str(len(raw_text_channels)) + ')',
			description = channels,
			colour = discord.Colour.orange()
		)

		return await ctx.send(embed = embed)

	@commands.command(name = 'voice_channels', aliases = ['vc', 'vcl', 'vcls', 'voicechannels', 'voice_channel_list'])
	async def voice_channels_list(self, ctx):
		'''
		Returns a list of all voice channels
		'''
		raw_voice_channels = ctx.guild.voice_channels
		voice_channels = []
		category_ids = []

		for raw_voice_channel in raw_voice_channels:

			if raw_voice_channel.category_id not in category_ids:

				category_ids.append(raw_voice_channel.category_id)
				voice_channels.append('\nCategory : '+raw_voice_channel.category.name)
				voice_channels.append(raw_voice_channel.name)

			else:

				voice_channels.append(raw_voice_channel.name)

		channels = str('\n'.join(voice_channels))

		embed = discord.Embed(
			title = 'Voice-Channels (' + str(len(raw_voice_channels)) + ')',
			description = channels,
			colour = discord.Colour.dark_orange()
		)

		return await ctx.send(embed = embed)
	
	@commands.command(name = 'memberlist', aliases = ['mls', 'memberls'])
	async def memberlist(self, ctx):
		'''
		Returns a list of members
		'''
		raw_member_list = ctx.guild.members
		members = []
		for member in raw_member_list:
			if not member.bot:
				members.append(str(member.name) + '#' + str(member.discriminator))
				
		embed = discord.Embed(
			title = 'List Of Members',
			description = str('\n'.join(members)),
			timestamp = datetime.datetime.today(),
			colour = discord.Colour.teal()
		)
		return await ctx.send(embed = embed)

	@commands.command(name = 'botlist', aliases = ['bls', 'botls'])
	async def botlist(self, ctx):
		'''
		Returns a list of bots
		'''
		raw_bot_list = ctx.guild.members
		bots = []
		for bot_ in raw_bot_list:
			if bot_.bot:
				bots.append(str(bot_.name) + '#' + str(bot_.discriminator))
				
		embed = discord.Embed(
			title = 'List Of Bots',
			description = str('\n'.join(bots)),
			timestamp = datetime.datetime.today(),
			colour = discord.Colour.gold()
		)
		return await ctx.send(embed = embed)


def setup(bot):
	bot.add_cog(list_everything(bot))

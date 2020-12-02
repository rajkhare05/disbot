import discord
from discord.ext import commands

class voiceCmd(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name = 'join', aliases = ['summon'])
	async def _join(self, ctx, channel: discord.VoiceChannel = None):
		'''
		Bot joins a voice channel
		'''
		destination = channel if channel else ctx.author.voice.channel
		if ctx.voice_client:
			await ctx.guild.voice_client.move_to(destination)
			await ctx.send(f"Succesfully joined the voice channel: {destination.name}.")
			return
		await destination.connect(reconnect = True)
		await ctx.send(f"Succesfully joined the voice channel: {destination.name}.")

	@commands.command(name = 'leave', aliases = ['out'])
	async def _leave(self, ctx):
		'''
		Bot leaves a voice channel
		'''
		voice_client = ctx.guild.voice_client
		if voice_client:
			await voice_client.disconnect(force = True)
			await ctx.send("Bot left the voice channel")
		else:
			print("Bot was not in channel")
		return
	
def setup(bot):
	bot.add_cog(voiceCmd(bot))

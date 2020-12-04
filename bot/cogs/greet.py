import discord
from discord.ext import commands
from datetime import datetime
import re
import pytz

class greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
    
	def c_time(self):
		time_ = str(datetime.now(pytz.timezone('Asia/Kolkata')))
		pattern = r"\d\d:\d\d:\d\d"
		return ''.join(re.findall(pattern, time_))
    
	@commands.Cog.listener()
	async def on_message(self, message):
		match = re.findall('^hi+.*', str(message.content.lower()))
		if message.author.id == self.bot.user.id:
			return
		if message.content.lower() in match:
			time_ = int(str(self.c_time())[:2])
			if time_ < 12:
				await message.channel.send('Hi, Good Morning ! <@{id}> '.format(id = message.author.id))
			elif time_ > 11 and time_ < 18:
				await message.channel.send('Hi, Good Afternoon ! <@{id}>'.format(id = message.author.id))
			elif time_ > 17:
				await message.channel.send('Hi, Good Evening ! <@{id}>'.format(id = message.author.id))

		if message.content.lower() == 'bye':
			await message.channel.send('Bye, see you ! <@{id}> :-)'.format(id = message.author.id))

def setup(bot):
	bot.add_cog(greetings(bot))

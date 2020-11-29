import discord
from discord.ext import commands
import re
import asyncio

class remove_bad_word(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	def hasBadWords(self, sentence):
		result = False
		f_words = r'(\w|\s)*(\W|_)*(f+(\W|_)*(c|u|\*)+(\W|_)*(u|c|\*)+(\W|_)*k+(\W|_)*(3|e)*(\W|_)*(r|d)*(\W|_)*(\$|&|s)*(\w|\s)*)'
		s_words = r'(\w|\s)*(\W|_)*((\$|&|s)+(\W|_)*(#|h|\*)+(\W|_)*(i|\*)+(\W|_)*t+(\W|_)*y*(\W|_)*(\$|&|s)*(\W|_)*(\w|\s)*)'
		c_words = r'(\w|\s)*(\W|_)*(c+(\W|_)*(0|o|\*)+(\W|_)*(c|\*)+(\W|_)*k+(\W|_)*y*(\W|_)*(\$|&|s)*(\W|_)*(\w|\s)*)'
		p_words = r'(\w|\s)*(\W|_)*(p+(\W|_)*(u|\*)+(\W|_)*(\$|&|s|\*)+(\W|_)*(\$|&|s|\*)+(\W|_)*(i*e*(s|\$|&)*)?(\W|_)*y*(\W|_)*(\w|\s)*)'
		d_words = r'(\w|\s)*(\W|_)*(d+(\W|_)*(i|\*)+(\W|_)*(c|\*)+(\W|_)*k+(\W|_)*y*(\W|_)*(i*(3|e)*)?(\W|_)*(\$|&|s)*(\W|_)*t*(\W|_)*(\w|\s)*)'
		a_words = r'(\w|\s)*(\W|_)*((@|a)+(\W|_)*(\$|&|s|\*)+(\W|_)*(\$|&|s|\*)+(\W|_)*(#|h|\*)+(\W|_)*(0|o|\*)+(\W|_)*(1|l|\*)+(\W|_)*(3|e)*(\W|_)*(\$|&|s)*(\W|_)*(\w|\s)*)'
		b_words = r'(\w|\s)*(\W|_)*(b+(\W|_)*(u|\*)+(\W|_)*(t|\*)+(\W|_)*(t|\*)+(\W|_)*(\$|&|s)*(\W|_)*(\w|\s)*)'
		t_words = r'(\w|\s)*(\W|_)*(t+(\W|_)*(i|\*)+(\W|_)*(t|\*)+(\W|_)*(i*(3|e)*)?(\W|_)*(\$|&|s)*(\W|_)*(\w|\s)*)'
		pn_words = r'(\w|\s)*(\W|_)*(p+(\W|_)*(0|o|\*)+(\W|_)*(r|\*)+(\W|_)*n+(\W|_)*(\w|\s)*)'
		sl_words = r'(\w|\s)*(\W|_)*((\$|&|s)+(\W|_)*(1|l|\*)+(\W|_)*(u|\*)+(\W|_)*t+(\W|_)*(\$|&|s)*(\W|_)*y*(\W|_)*(\w|\s)*)'
		bb_words = r'(\w|\s)*(\W|_)*(b+(\W|_)*(0|o|\*)+(\W|_)*(0|o|\*)+(\W|_)*(b|\*)+(\W|_)*(i*e*)?(\W|_)*(s|\$|&)*(\W|_)*(\w|\s)*)'
		bh_words = r'(\w|\s)*(\W|_)*(b+(\W|_)*(u|\*)+(\W|_)*(t|\*)+(\W|_)*(t|\*)+(\W|_)*(#|h|\*)+(\W|_)*(0|o|\*)+(\W|_)*(1|l|\*)+(\W|_)*(e|3)+(\W|_)*(\$|&|s)*(\W|_)*(\w|\s)*)'
		cm_words = r'(\w|\s)*(\W|_)*(c+(\W|_)*(u|\*)+(\W|_)*m+(\W|_)*(e*d*i*n*g*(\$|&|s)*)?(\W|_)*(\w|\s)*)'
		as_words = r'(\w|\s)*(\W|_)*((@|a)+(\W|_)*(\$|s|&|\*)+(\W|_)*(\$|s|&|\*)+(\W|_)*(\w|\s)*)'
		an_words = r'(\w|\s)*(\W|_)*((@|a)+(\W|_)*(n|\*)+(\W|_)*(@|a|\*)+(\W|_)*l+(\W|_)*(\w|\s)*)'
		bt_words = r'(\w|\s)*(\W|_)*(b+(\W|_)*(i|\*)+(\W|_)*(t|\*)+(\W|_)*(c|\*)+(\W|_)*(h|#)+(\W|_)*(\w|\s)*)'
		words = [f_words, s_words, c_words, p_words,
				d_words, a_words, b_words, t_words,
				pn_words, sl_words, bb_words, bh_words,
				cm_words, as_words, an_words]
		for word in words:
			find_ = list(re.findall(word, sentence))
			match_ = re.match(word, sentence)
			if find_ != [] and (match_ or find_[0][2] != ''):
				result = True
				break
		return result

	@commands.Cog.listener()
	async def on_message(self, message : discord.Message):
		if message.author.id == self.bot.user.id:
			return
		anyBadWord = self.hasBadWords(message.content.lower())
		if anyBadWord:
			await message.delete(delay = 0)
			member_ = message.guild.get_member(message.author.id)
			await message.channel.set_permissions(member_, read_messages = True, send_messages = False)
			await member_.create_dm()
			await member_.send('Watch your words {user_}, you can't message for 20 seconds !'.format(user_ = member_.mention))
			await asyncio.sleep(20)
			await message.channel.set_permissions(member_, overwrite = None)

def setup(bot):
	bot.add_cog(remove_bad_word(bot))

from discord.ext import commands
import discord

class dm_channel_(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name = 'modmail')
	@commands.has_role('MOD')
	async def mod_mail(self, ctx, member_ : str = None, *,dm : str = None):
		'''
		Sends a modmail
		'''
		if str(ctx.channel.name) == 'mod-mail':
			member_id = int(member_.strip('<@!>'))
			member_ = ctx.guild.get_member(member_id)
			if dm is None:
				dm = 'msg'
			await member_.create_dm()
			await member_.send(content = dm)
			reply = discord.Embed(
				description = '{m_u}, mod-mail sent !'.format(m_u = str(ctx.author)),
				colour = discord.Colour.teal()
			)
			return await ctx.send(embed = reply)
		await ctx.message.delete(delay = 4.0)
		msg = await ctx.send(embed = discord.Embed(
			description = '{usr_}, send in mod-mail channel !'.format(usr_ = str(ctx.author)),
			colour = discord.Colour.teal()
			)
		)
		return await msg.delete(delay = 5.0)

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		invoker_ = ctx.author
		if ctx.message.content.startswith('?modmail'):
			if isinstance(error, commands.MissingRole):
				return await ctx.send(embed = discord.Embed(
					description = '{usr}, you are not a \"{role_}\"'.format(usr = str(invoker_),
					role_ = error.missing_role),
					colour = discord.Colour.green()
				))

def setup(bot):
	bot.add_cog(dm_channel_(bot))

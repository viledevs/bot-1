import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix='$')
TOKEN = 'ODc4NDU3NzI5NDc0MjQwNTMy.YSBdgw.NSAZbBplNBzQHu87-u_SNPz4mao'


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    await bot.change_presence(activity=discord.Game('Viledevs.com'))


@bot.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send('Testing 1 2 3!')


@bot.event
async def on_member_join(member):
    await bot.get_channel(878685364208955452).send(f"{member.name} welcome to viledevs.")


@bot.command(name='server')
async def fetchServerInfo(context):
    guild = context.guild

    await context.send(f'Server Name: {guild.name}')
    await context.send(f'Server Size: {len(guild.members)}')
    await context.send(f'Server Name: {guild.owner.display_name}')


bot.run(TOKEN)


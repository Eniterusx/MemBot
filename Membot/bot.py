# pylint: disable=line-too-long,import-error,undefined-variable,consider-using-f-string,bare-except

"""
Main bot configuration module.
"""

import atexit

from discord.ext import commands, tasks

from Membot.env_live import ADMIN_LIST, CHANNEL_ID, REPORT_CHANNEL, BOT_TOKEN
from bot_on_message_commands import *

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


def run():
    bot.run(BOT_TOKEN)


@tasks.loop(minutes=10)
async def delete_under_performing_pictures():
    """
    Delete picture records, that have less than -5 total score from votes every 10 minutes.
    """
    print("Deleting bad pictures!")
    with ManageDatabase() as manage_database:
        manage_database.delete_under_performing_picture()
    print("Deleted bad pictures!")


def shutdown():
    """
    Execute when we close bot program.
    """


@bot.command(name='ban', pass_context=True)
async def ban(ctx, report_id, how_long_ban_in_days, reason_of_ban):
    """
    Bot !ban command.
    """
    try:
        if int(report_id) or int(how_long_ban_in_days) or str(reason_of_ban):
            await ctx.send("Command Error {}".format(ctx.message.author.mention))
        else:
            await ctx.send("Sending ban request!")
            if ctx.message.author.id in ADMIN_LIST:
                ban_user(report_id, how_long_ban_in_days, reason_of_ban)
                await ctx.send("User has been banned!")
            else:
                msg = "{}, you cannot use this command, because you do not have administrator permissions!".format(
                    ctx.message.author.mention)
                await ctx.send(msg)
        return
    except:
        await ctx.send("{}, Please use the command in the correct format".format(ctx.message.author.mention))
        return


@ban.error
async def new_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("{}, Please use the command in the correct format".format(ctx.message.author.mention))


@bot.command(name='unban', pass_context=True)
async def unban(ctx, report_id: int):
    """
    Bot !unban command.
    """
    if ctx.message.author.id in ADMIN_LIST:
        await ctx.send("Sending unban request!")
        unban_user(report_id)
        await ctx.send("User unbanned!")
    else:
        await ctx.send("{}, you cannot use this command, because you do not have administrator permissions!"
            .format(ctx.message.author.mention))
    return


@unban.error
async def unban_error(ctx, error):
    """
    Bot reaction upon not administrator !unban command usage.
    """
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("{}, Please use the command in the correct format".format(ctx.message.author.mention))


@bot.command(name='see', pass_context=True)
async def see(ctx, picture_id: int):
    await ctx.send("Sending see request!")
    record: list[tuple[Any, ...]] = get_image(picture_id)
    if record is not None:
        await ctx.send(record[0][4])
        await ctx.send("Request sent!")
    else:
        await ctx.send("Your picture was not found {}!".format(ctx.message.author.mention))


@bot.event
async def on_ready():
    """
    Po uruchomieniu polacz sie z baza danych, wyslij wiadomosc na kanale testowym
    """
    atexit.register(shutdown)
    channel = bot.get_channel(CHANNEL_ID)
    delete_under_performing_pictures.start()
    # channel = discord.utils.get(bot.get_all_channels(), name='channel_name')
    await channel.send("Meow!")


@bot.event
async def on_message(message):
    """
    Command handling:
        -   zamiast bot.command stosujemy bot.event i nazwe funkcji on_message wtedy bedzie nasluchiwal wszystkich
            wiadomosci na wszystkich kanalach i jezeli ktorakolwiek zaczyna sie tak jak zdefiniowano ponizej, to
            zacznie przetwarzac informacje
    """
    if message.content.startswith('!meme') or message.content == '!m':
        await fetch_meme(message, False)
    elif message.content.startswith('!waitroom') or message.content == '!w':
        await fetch_meme(message, True)
    elif message.content.startswith('!upload'):
        user = message.author
        with ManageDatabase() as manage_database:
            if not manage_database.is_user_banned(user.id):
                await upload_meme(message)
            else:
                await message.channel.send(
                    "{} You are banned from using !upload command!".format(message.author.mention))
    elif message.content.startswith('!help'):
        await send_help_message(message)
    elif message.content.startswith('!report'):
        await report_picture(message, bot)
    elif message.content.startswith('!see'):
        await see_meme(message)
    else:
        await bot.process_commands(message)


def extract_embed_message(embed):
    if embed.type == "rich":
        return embed.description
    return None


@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '👍' and user != bot.user and reaction.message.author == bot.user and reaction.message.embeds:
        await add_vote(reaction.message, user, True)
    if reaction.emoji == '👎' and user != bot.user and reaction.message.author == bot.user and reaction.message.embeds:
        await add_vote(reaction.message, user, False)

# pylint: disable=line-too-long,import-error,undefined-variable,consider-using-f-string,bare-except

"""
Configuration to bot responses on commands (on_message).
"""
from typing import Any, Optional

import discord

from DatabasePackage.src.manage_module.manage_database import ManageDatabase, PICTURE_SUCCESS
from DatabasePackage.src.verification_module.data_verification import Verification

from imgur import imgur_upload

from Membot.env_live import REPORT_CHANNEL


def create_embed(record):
    file_type = record[0][4][-3:]
    url = record[0][4]
    url = url.replace('com', 'com.', 1)
    current_score = record[0][9]
    if current_score < -4:
        color = discord.Colour.dark_red()
    elif current_score < -2:
        color = discord.Colour.red()
    elif current_score > 3:
        color = discord.Colour.green()
    elif current_score > 6:
        color = discord.Colour.dark_green()
    else:
        color = discord.Colour.orange()
    embed = discord.Embed(
        title=record[0][2],
        url=url,
        description=f'Score: {current_score}',
        color=color
    )


    embed.set_image(url=url)
    embed.set_footer(text=f'Picture ID: {record[0][0]}',
                     icon_url="https://static.wikia.nocookie.net/memes/images/9/9a/Troll-face.jpg/revision/latest"
                              "/scale-to-width-down/250?cb=20150924183516&path-prefix=pl")
    if file_type == "mp4":
        embed.description += "\nBecause of discord limitations, mp4 files are only available as a link"
    return embed


def extract_embed_message(embed):
    if embed.type == "rich":
        return embed.description
    return None


async def send_help_message(message):
    embed = discord.Embed(
        title="Help",
        description='!help - triggers this message\n'
                    '!upload - usage !upload *title* - uploads a meme with your title\n'
                    '!meme or !m - sends a highest quality meme\n'
                    f'!waitingroom or !w - sends a low quality meme (score <{PICTURE_SUCCESS})\n'
                    '!see or !s - usage !see *picture id* - sends the meme with the desired id\n'
                    '!report - usage !report *picture id* *message* - reports the message\n'
                    '!ban - usage !ban *report id* *amount of days* *report message* - admin only, '
                    'bans user from posting memes\n'
                    '!unban - usage !unban *discord id* - admin only, unbans user',
        color=discord.Colour.magenta()
    )
    await message.channel.send(embed=embed)


async def upload_meme(message):
    if message.attachments:

        # Download attachment
        attachment = message.attachments[0]

        # Sprawdz, czy użytkownik dołączył nazwę mema
        file_name = message.content.split(" ", 1)
        if len(file_name) > 1:
            file_name = file_name[1]
        else:
            file_name = ""

        list_of_test: list[tuple[str, Any], ...] = [
            ('file_name', file_name),
            ('file_type', attachment.filename.split(".")[-1]),
            ('file_size', attachment),
            ('image_category', 'Empty')
        ]

        verification_object = Verification()
        errors = verification_object.verify_data(list_of_test)

        # Sprawdzenie czy są błędy jak errors sa pustą listo to nie było błędów
        if errors is not None:
            # Dict, który zawiera jakie informacje mamy przekazać użytkonikowi z zewnątrz :D
            # key, to jaki test nie wypalił
            # d[key], to jaką informację przekazać użytkownikowi :D

            dict_of_responses: dict[str, str] = {
                "file_name_must_contain_specific_characters": "Encoding of a file name is not correct.\n"
                                                              "It can only consist of: a-z, A-Z, 0-9, _, "
                                                              "(space)",
                "file_name_must_be_specific_length": "File name not correct! It Can be only between 2 and 70 characters"
                                                     " long",
                "_verify_file_size_too_big": "The size of a provided file is too big! Maximum available size "
                                             "is 25MiB.",
                "file_type_must_be_in_allowed_types": "File type not supported!",
                "image_category_must_contain_specific_characters": "Incorrect meme category\n"
                                                                   "It can only consist of: a-z, "
                                                                   "A-Z, 0-9, _, (space)"
            }
            for err in errors:
                await message.channel.send(dict_of_responses.get(err[0]))
        else:
            # Spróbuj wysłać plik na platformę imgur
            await message.channel.send(f'Sending meme: {file_name}!')
            response = await imgur_upload(attachment.url)
            if response:
                try:
                    with ManageDatabase() as manage_database:
                        manage_database.add_picture(message.author, message.author.id, file_name,
                                                    str(response.get('type')), str(response.get('link')),
                                                    str(response.get('id')), str(response.get('deletehash')))
                        await message.channel.send('The file has been sent successfully!')
                except:
                    await message.channel.send('Error has occurred :( Please try again!')
            else:
                await message.channe.send('Sending error occurred!')
    else:
        await message.channel.send("You did not attach a file to the message!")


async def fetch_meme(message, if_waiting: bool):
    try:
        if if_waiting:
            with ManageDatabase() as manage_database:
                record = manage_database.random_picture_wait_room()
        else:
            with ManageDatabase() as manage_database:
                record = manage_database.random_picture()
        embed = create_embed(record)

        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    except:
        await message.channel.send('Error has occurred :( Please try again!')


async def add_vote(message, user, vote):
    embed_message = message.embeds[0]
    pic_id = embed_message.footer.text.split(" ")[-1]
    channel = message.channel

    with ManageDatabase() as manage_database:
        if vote:
            manage_database.add_vote(user.id, user, pic_id, 1)
            await channel.send(f'Liked the meme, {user}')
        else:
            manage_database.add_vote(user.id, user, pic_id, -1)
            await channel.send(f'Disliked the meme, {user}')


async def report_picture(message, bot):
    channel = message.channel
    user = message.author
    split = message.content.split(" ", 2)
    try:
        split[2]
    except:
        await channel.send("Command error!")
        return
    pic_id = split[1]
    report_reason = split[2]
    try:
        if int(pic_id) <= 0:
            await channel.send("Id error!")
            return
    except:
        await channel.send("Id error!")
        return
    if not len(report_reason) > 0:
        await channel.send("Report reason must not be blank!")
        return

    with ManageDatabase() as manage_database:
        check = manage_database.add_report(user.id, user, pic_id, report_reason)
    if check == -1:
        await channel.send("Picture doesn't exist!")
        return
    if not check:
        await channel.send("Report sent!")
        channel = bot.get_channel(REPORT_CHANNEL)
        with ManageDatabase() as manage_database:
            record = manage_database.find_picture(('picture_id', pic_id))
            report = manage_database.find_report(("picture_id_&_discord_id", pic_id, user.id))
            record = manage_database.find_user(('user_id', record[0][1]))
        response = f'Received new report of id: {report[0][0]}\n' \
                   f'Picture reported: {pic_id}\n' \
                   f'Picture was added by user of id: {record[0][0]}\n' \
                   f'Here are his discord details: {record[0][1]}, {record[0][2]}\n' \
                   f'This report was made by user that has discord details such as: {user.id}, {user}\n' \
                   f'Report reason: {report_reason}'
        await channel.send(response)
    else:
        await channel.send("You have already reported this image!")
        return


async def see_meme(message):
    try:
        pic_id = int(message.content.split(" ", 1)[1])
        with ManageDatabase() as manage_database:
            record = manage_database.find_picture(('picture_id', pic_id))
        if not record:
            await message.channel.send('{} Meme not found'.format(message.author.mention))
            return
        embed = create_embed(record)

        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        return
    except:
        await message.channel.send('{} Command error!'.format(message.author.mention))
        return


def ban_user(report_id: int, how_long_ban_in_days: int, reason_of_ban: str):
    with ManageDatabase() as manage_database:
        manage_database.ban(report_id, how_long_ban_in_days, reason_of_ban)


def unban_user(report_id: int):
    with ManageDatabase() as manage_database:
        manage_database.unban(report_id)


def get_image(picture_id: int) -> Optional[list[tuple[Any, ...]]]:
    with ManageDatabase() as manage_database:
        return manage_database.find_picture(("picture_id", picture_id))




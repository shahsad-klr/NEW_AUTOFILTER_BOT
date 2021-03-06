#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG 

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@DB_ROBOTS"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("ð¤­ Sorry BRO, You are B A N N E D ð¤£ð¤£ð¤£")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>ð ðð¼ð¶ð» ð¢ðð¿ ð ð®ð¶ð» ð°ðµð®ð»ð»ð²ð¹ ð\n\n TO ACSEES TO GET DESIRED MOVIES FILES U SHOULD JOIN OUR CHANNEL,AFTER U AGAIN SEND /start COMMAND . THAT'S ALL \n\ð¡ï¸âï¸ THANK YOU ð»â¤ï¸</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" ð°JOIN OUR CHANNELð° ", url=f"https://t.me/DB_ROBOTS")]
              ])
            )
            return
        except Exception:
            await update.reply_text("SRY DIDN'T JOINED OUR @DB_ROBOTS CHANNEL THAT'S Y THIS IS HAPPENING")
            return
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = "<b>ââ¢â¢â¿ UMR GROUP â¿â¢â¢â\n\nâ ðÊá´É´É´á´Ê :https://t.me/UNI_MOVIES_BOX\n\nâ GÊá´á´á´ : https://t.me/UM_REQUESTS</b>",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('â­ï¸ ððð¼ðð â­ï¸', url='https://t.me/share/url?url=https://t.me/UM_REQUESTS')
                ],
                [
                    InlineKeyboardButton('ððððð ð¬', url='https://t.me/UM_REQUESTS'),
                    InlineKeyboardButton('â¼ï¸ ð¾ðð¼ðððð', url='https://t.me/UNI_MOVIES_BOX')
                ]
            ]
        )
    )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('â­ï¸ ððð¼ðð â­ï¸', url='https://t.me/share/url?url=https://t.me/DB_ROBOTS')
                ],
                [
                    InlineKeyboardButton('ððððð ð¬', url='https://t.me/UM_REQUESTS'),
                    InlineKeyboardButton('â¼ï¸ ð¾ðð¼ðððð', url='https://t.me/UNI_MOVIES_BOX')
                ]
            ]
        )
    )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'â ï¸ ðð¢ðð¡ ð¢ð¨ð¥ ðð¥ð¢ð¨ð£ â ï¸', url="https://t.me/DB_ROBOTS"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('ð¡ï¸ ð¶ðð¾ðð¿', url='https://t.me/UM_REQUESTS'),
        InlineKeyboardButton('ð¼ ð¾ððð¼ððð', url ='https://t.me/DEEKS_04_8')
        ],[
        InlineKeyboardButton('âï¸ ðððð ððð ð¾ðð¼ðððð âï¸', url ='https://t.me/db_robots')
        ],[
        InlineKeyboardButton('ð¤  ðððð', callback_data="help"),
        InlineKeyboardButton('ð ð¾ðððð', callback_data="close")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/3edda07f6b4ba518ac137.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.mention),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('ðð¤ð¢ð ð', callback_data='start'),
        InlineKeyboardButton('ð¼ðð¤ðªð© ð¿', callback_data='about')
    ],[
        InlineKeyboardButton('ð¾ð¡ð¤ð¨ð ð', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/3edda07f6b4ba518ac137.jpg",
        caption=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('ðð¤ð¢ð ð', callback_data='start'),
        InlineKeyboardButton('ð¾ð¡ð¤ð¨ð ð', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import TelegramBot
from bot.config import Telegram
from bot.static import *

@TelegramBot.on_message(
    filters.command('start')
    & (
        filters.private |
        filters.group
    )
)
async def start_command(_, msg: Message):
    return await msg.reply(
        text=WelcomeText % {'first_name': msg.from_user.first_name if msg.from_user else 'Anonymous'},
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆', url=f'https://telegram.me/{Telegram.BOT_USERNAME}?startgroup=botstart')
                ],
                [
                    InlineKeyboardButton(text='• ᴜᴩᴅᴀᴛᴇꜱ •', url='https://t.me/hd_movies488'),
                    InlineKeyboardButton(text='• ꜱᴜᴩᴩᴏʀᴛ •', url='https://t.me/+SDBvltduRtkyMGM1')
                ],
                [
                    InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆', url=f'https://telegram.me/{Telegram.BOT_USERNAME}?startchannel=botstart')
                ]
            ]
        )
    )

@TelegramBot.on_message(
    filters.command('help')
    & (
        filters.private |
        filters.group
    )
)
async def send_emojis(_, msg: Message):
    return await msg.reply(
        text=Help,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='👨‍💻 ᴏᴡɴᴇʀ', url='https://telegram.me/randeep_singh48'),
                    InlineKeyboardButton(text='💥 ʀᴇᴘᴏ', url='https://telegram.me/randeep_singh48')
                ]
            ]
        )
    )

from pyrogram.types import InlineKeyboardButton

import config
from ThavaXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝖠𝖣𝖣 𝖬𝖤 𝖣𝖠𝖱𝖫𝖨𝖭𝖦 😍",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="𝖧𝖤𝖫𝖯", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="𝖦𝖱𝖮𝖴𝖯", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝖢𝖧𝖠𝖭𝖭𝖤𝖫", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="𝖣𝖠𝖱𝖫𝖨𝖭𝖦 ᥫ᭡", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝖬𝖠𝖨𝖭𝖳𝖠𝖨𝖭𝖤𝖣 𝖡𝖸", url=f"https://t.me/Idhayann"),
        ],
        [
            InlineKeyboardButton(
                text="𝖠𝖫𝖳𝖤𝖱 𝖤𝖦𝖮 😍",
                url=f"https://t.me/ShinobuMusicBot",
            )
        ],
    ]
    return buttons

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
                text="ᴊᴜsᴛ ᴛᴏᴜᴄʜ ᴛᴏ ᴀᴅᴅ ᴍᴇ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="ᴅᴀʀʟɪɴɢ ᥫ᭡", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ", url=f"https://t.me/Ak1082"),
        ],
    ]
    return buttons

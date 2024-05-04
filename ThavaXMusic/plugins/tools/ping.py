from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from ThavaXMusic import app
from ThavaXMusic.core.call import THAVA
from ThavaXMusic.utils import bot_sys_stats
from ThavaXMusic.utils.decorators.language import language
from ThavaXMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL, SUPPORT_CHAT


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo="https://telegra.ph/file/e500a4952873f1476196e.jpg",
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await THAVA.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping, SUPPORT_CHAT),
        reply_markup=supp_markup(_),
    )

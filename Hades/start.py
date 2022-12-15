TEXT = """Hey {}! I'm AFK Bot of Spoiled Community. 

Try: replying afk to some media or stickers or gifs to make it more reasonable !

We host our bots on vps, zero down time !
"""

from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
#from .Database.users import add_user
from .helpers import get_readable_time
from . import startTime
import time
from .Database.cm import check_cc

LINK = "https://telegra.ph/file/0a95deafeb88af0c05596.jpg"

async def start(_, m):
    y = await check_cc(m.chat.id)
    x = True if y else False
    if x:
        try:
            await m.delete()
        except:
            pass
    l = await _.get_me()
    un = l.username
    name = m.from_user.first_name
    up = get_readable_time(int(time.time() - startTime))
    markup = IKM(
             [
             [
             IKB("➕ Add me to your group ➕", url=f"t.me/{un}?startgroup=True")
             ]
             ]
             )
    await m.reply_photo(LINK, caption=(TEXT.format(name) + f"\nUptime : {up}"),  reply_markup=markup)
    #await add_user(m.from_user.id)

import asyncio 

from .Database.chats import get_chats
from pyrogram.errors import FloodWait
from Hades.Database.cm import check_cc

async def broadcast(_, message):
    y = await check_cc(message.chat.id)
    x = True if y else False
    if x:
        try:
            await message.delete()
        except:
            pass
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    pinned = 0
    chats = await get_chats()
    for i in chats:
        try:
            if message.reply_to_message:
                ok = await _.forward_messages(i, y, x)
                sent += 1
                try:
                    await _.pin_chat_message(i, ok.id)
                    pinned += 1
                except:
                    continue 
            else:
                ok = await _.send_message(i, query)
                sent += 1
                try:
                    await _.pin_chat_message(i, ok.id)
                    pinned += 1
                except:
                    continue
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await message.reply_text(
            f"**Broadcasted Message In {sent} Chats and pinned in {str(pinned)} Chats**"
        )
    except:
        pass

async def info(_, m):
    if len(m.command) == 2:
        lel = int(m.text.split(None, 1)[1])
        if str(lel)[0] == "-":
            id = lel
        else:
            omfoo = "-" + str(lel)
            id = int(omfoo)

    getter = await _.get_chat(id)
    try:
        username = getter.username
    except:
        username = "None"
    try:
        link = getter.invite_link
    except:
        link = "None"
    await m.reply(f"Group name :- {getter.title}\n\nInvite link :- {link}\n\nUsername :- @{username}")

async def schats(_, m):
    chats = await get_chats()
    msg = ""
    NOTED = []
    for i in chats:
        if i in NOTED:
            continue
        NOTED.append(i)
        i = str(i)
        msg += f"\n<code>{i}</code>"
    await m.reply(f"**Served chats** :-\n{msg}\n\n**Count** :- {len(NOTED)}")

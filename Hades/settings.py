from pyrogram import Client, filters
from Hades.Database.cm import toggle_cc, check_cc
from pyrogram.types import CallbackQuery as CBQ, InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

id = None


IMG = "https://telegra.ph/file/a19360563978fe7980c8f.jpg"

async def settings(_, m):
    global id
    if str(m.chat.id)[0] != "-":
        return
    id = m.from_user.id
    y = await check_cc(m.chat.id)
    x = True if y else False
    if x:
        try:
            await m.delete()
        except:
            pass
    mk = [
        [
        IKB("Commands Clean", callback_data="cc_answer"),
        IKB("{}".format("Enabled ✅" if x else "Disabled ❌"), callback_data="cc_toggle")
        ],
        [
        IKB("Close 🔙", callback_data="close")
        ]
    ]
    await m.reply_photo(IMG, caption=f"⚙️ AFK Bot settings\n\n🏘️ Group :- {m.chat.title}\n\n🆔 Group id :- <code>{m.chat.id}</code>\n\nChoose from below options !", reply_markup=IKM(mk))
    
async def cc_ans(_, q):
    await q.answer("What's this ?\n\nIf this mode is enabled, Command messages will be deleted automatically.\n\nFor this, bot must be admin with delete messages right !", show_alert=True)
    
async def cc_tog(_, q):
    z = await _.get_chat_member(q.message.chat.id, q.from_user.id)
    if not z.status.name in ["OWNER", "ADMINISTRATOR"]:
        return await q.answer("Only admins can make changes !", show_alert=True)
    await toggle_cc(q.message.chat.id)
    y = await check_cc(q.message.chat.id)
    x = True if y else False
    mk = [
        [
        IKB("COMMANDS CLEAN", callback_data="cc_answer"),
        IKB("{}".format("Enabled ✅" if x else "Disabled ❌"), callback_data="cc_toggle")
        ],
        [
        IKB("Close 🔙", callback_data="close")
        ]
    ]
    try:
        await q.answer()
        await q.edit_message_reply_markup(reply_markup=IKM(mk))
    except Exception as e:
        await q.message.reply(e)

async def close(_, q):
    global id
    await q.answer()
    if q.from_user.id != id:
        return
    await q.message.delete()

from config import API, TOKENS, DEV
from pyrogram import Client as Hades, idle
from pyrogram.filters import command as hade_cmd, new_chat_members, user
from Hades.afk import afk
from Hades.watcher import afk_reply_watcher, afk_watcher, welcome
from Hades.broadcast import broadcast
from Hades.start import *
import time

st = None

def get_uptime(sec):
    seconds = int(sec)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return [hours, minutes, seconds]

print("modules imported !")

hades = Hades(":Hades:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN)

print("\nClient verified !")

@hades.on_message(hade_cmd(["afk"]) | hade_cmd("brb", ""))
async def afk_plug(_, m):
    await afk(_, m)

print("\nMain module loaded !")

@hades.on_message(group=1)
async def watcher1(_, m):
    await afk_watcher(_, m)

print("\nWatcher 1 loaded !")

@hades.on_message(group=2)
async def watcher2(_, m):
    await afk_reply_watcher(_, m)

print("\nWatcher 2 loaded !")

@hades.on_message(new_chat_members, group=3)
async def welcome_plug(_, m):
    await welcome(_, m)

print("\nWatcher 3 loaded !")

@hades.on_message(hade_cmd("broadcast") & user(DEV.SUDO_USERS))
async def broadcast_plug(_, m):
    await broadcast(_, m)

print("\nBroadcaster loaded !")

TEXT = """Hey {}! I'm AFK Bot of Spoiled Community. 

Try: replying afk to some media or stickers or gifs to make it more reasonable !

"""

@hades.on_message(hade_cmd("start"))
async def start(_, m):
    end = time.time()
    tot = end-st
    upt = get_uptime(tot)
    Uptime = f"{upt[0]}h:{upt[1]}m:{upt[2]}s"
    l = await _.get_me()
    un = l.username
    name = m.from_user.first_name
    markup = IKM(
             [
             [
             IKB("➕ Add me to your group ➕", url=f"t.me/{un}?startgroup=True")
             ]
             ]
             )
    TEXT = TEXT + f"\n\nUptime : {Uptime}"
    await m.reply_photo(LINK, caption=TEXT.format(name), reply_markup=markup)

def Asynchorous(x):
    global st
    x.start()
    st = time.time()
    y = x.get_me()
    z = y.username
    t = f"\n@{z} Started Successfully !"
    print(t)
    idle()

try:
    Asynchorous(hades)
except:
    pass


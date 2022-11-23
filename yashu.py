from config import API, TOKENS, DEV
from pyrogram import Client as Hades, idle
from pyrogram.filters import command as hade_cmd, new_chat_members, user
from Hades.afk import afk
from Hades.watcher import afk_reply_watcher, afk_watcher, welcome
from Hades.broadcast import broadcast
from Hades.start import start

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

@hades.on_message(hade_cmd("start"))
async def start_plug(_, m):
    await start(_, m)

def Asynchorous(x):
    x.start()
    y = x.get_me()
    z = y.username
    t = f"\n@{z} Started Successfully !"
    print(t)
    idle()

try:
    Asynchorous(hades)
except:
    pass


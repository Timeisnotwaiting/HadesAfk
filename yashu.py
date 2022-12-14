from config import API, TOKENS, DEV
from pyrogram import Client as Hades, idle
from pyrogram.filters import command as hade_cmd, new_chat_members, user, regex
from Hades.afk import afk
from Hades.watcher import afk_reply_watcher, afk_watcher, welcome
from Hades.broadcast import broadcast, info, schats
from Hades.start import start
from Hades.sysinfo import sysinfo
from Hades.settings import *

print("modules imported !")

hades = Hades(":Hades:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN)

print("\nClient verified !")

@hades.on_message(hade_cmd(["afk", "fuck"]) | hade_cmd("brb", ""))
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

@hades.on_message(hade_cmd("info") & user(DEV.SUDO_USERS))
async def info_plug(_, m):
    await info(_, m)

@hades.on_message(hade_cmd("schats") & user(DEV.SUDO_USERS))
async def schats_plug(_, m):
    await schats(_, m)

print("\nBroadcaster loaded !")

@hades.on_message(hade_cmd("sysinfo"))
async def sysinfoplug(_, m):
    await sysinfo(_, m)

@hades.on_message(hade_cmd("settings"))
async def settings_plug(_, m):
    await settings(_, m)

@hades.on_callback_query(regex("cc_answer"))
async def cc1(_, q):
    await cc_ans(_, q)

@hades.on_callback_query(regex("cc_toggle"))
async def cc2(_, q):
    await cc_tog(_, q)

@hades.on_callback_query(regex("close"))
async def cc3(_, q):
    await close(_, q)

print("\nSettings loaded !")

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


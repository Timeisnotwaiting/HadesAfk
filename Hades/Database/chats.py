from . import db

chatsdb = db.chats

async def add_chat(chat_id: int):
    x = await chatsdb.find_one({"chat_id": chat_id})
    if not x:
        return await chatsdb.insert_one({"chat_id": chat_id})
    return

async def get_chats():
    x = chatsdb.find({"chat_id": {"$lt": 0}})
    if not x:
        return []
    CHATS = []
    for y in await x.to_list(length=1000000000):
        CHATS.append(int(y["chat_id"]))
    return CHATS

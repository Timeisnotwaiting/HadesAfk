from . import db

cc = db.cc

async def toggle_cc(chat_id: int):
    is_on = await cc.find_one({"chat_id": chat_id})
    if is_on:
        await cc.delete_one({"chat_id": chat_id})
    else:
        await cc.insert_one({"chat_id": chat_id})

async def check_cc(chat_id: int):
    is_on = await cc.find_one({"chat_id": chat_id})
    if is_on:
        return True
    else:
        return False

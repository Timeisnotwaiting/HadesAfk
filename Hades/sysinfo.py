import psutil as p

async def sysinfo(_, m):
    CPU = p.cpu_percent(1)
    TOTAL_RAM = (p.virtual_memory().total / 10000000000)
    RAM_USEDP = p.virtual_memory().percent
    RAM_USED = str((RAM_USEDP * TOTAL_RAM) / 100)[0:4]
    TOTAL_RAM = str(p.virtual_memory().total / 10000000000)[0:4]
    DISK_USAGE = str(p.disk_usage("/").percent)
    IMG = "https://te.legra.ph/file/70ef0b7a6c8fece1a13c0.jpg"

    txt = "\n"
    txt += f"• **SYS NAME : Alpha's VPS**"
    txt += "\n\n"
    txt += f"• **OS : Linux's Ubuntu**"
    txt += "\n\n"
    txt += f"**• CPU : {CPU}%**"
    txt += "\n\n"
    txt += f"**• DISK : {DISK_USAGE}%**"
    txt += "\n\n"
    txt += f"**• MEMORY USAGE : {RAM_USED}GB ({RAM_USEDP}%)**"
    txt += "\n\n"
    txt += f"**• MEMORY TOTAL (RAM) : {TOTAL_RAM}GB**"
    await m.reply_photo(IMG, caption=txt)

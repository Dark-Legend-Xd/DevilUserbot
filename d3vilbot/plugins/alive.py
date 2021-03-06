from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

d3vil_pic = Config.ALIVE_PIC or "https://te.legra.ph/file/3d3e0c14a462ac23f8477.jpg"
pm_caption = "  __**π₯π₯βΡΞ½ΞΉβΠ²ΟΡ ΞΉΡ Ξ±βΞΉΞ½Ρπ₯π₯**__\n\n"

pm_caption += f"**ββββββββββββββββββββ**\n\n"
pm_caption += (
    f"                 βΌπ ππ¦π§ππ₯β\n  **γ {d3vil_mention} γ**\n\n"
)
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += f"β β’β³β  `ΡΡβΡΡΠ½ΟΠΈ:` `{tel_ver}` \n"
pm_caption += f"β β’β³β  `Ξ½ΡΡΡΞΉΟΠΈ:` `{d3vil_ver}`\n"
pm_caption += f"β β’β³β  `ΡΟβΟ:` `{is_sudo}`\n"
pm_caption += f"β β’β³β  `Β’Π½Ξ±ΠΈΠΈΡβ:` [πΉπππ](https://t.me/Devil_Us3rBot)\n"
pm_caption += f"β β’β³β  `ΡΟΟΟΟΡΡ:` [βΡΞ½ΞΉβΠ²ΟΡ Β’Π½Ξ±Ρ](https://t.me/DevilB0T_CHAT)\n"
pm_caption += f"β β’β³β  `Β’ΡΡΞ±ΡΟΡ:` [Β’ΡΡΞ±ΡΟΡ](https://t.me/mr_developer_xd)\n"
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += " [β‘REPOβ‘](https://github.com/Dark-Legend-Xd/DevilBot) πΉ [πLicenseπ](https://github.com/Dark-Legend-Xd/DevilBot/blob/main/LICENSE)"


#-------------------------------------------------------------------------------

@bot.on(d3vil_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(d3vil):
    if d3vil.fwd_from:
        return
    await d3vil.get_chat()
    await d3vil.delete()
    await bot.send_file(d3vil.chat_id, d3vil_pic, caption=pm_caption)
    await d3vil.delete()

msg = f"""
**β‘ βΡΞ½ΞΉβΠ²ΟΡ ΞΉΡ ΟΠΈβΞΉΠΈΡ β‘**
{Config.ALIVE_MSG}
**π π±ππ ππππππ π**
**βΌπ ππ¦π§ππ₯β   :**  **γ{d3vil_mention}γ**
**ββββββββββββββββββββ**
**β β³β  ΡΡβΡΡΠ½ΟΠΈ :**  `{tel_ver}`
**β β³β  βΡΞ½ΞΉβΠ²ΟΡ  :**  **{d3vil_ver}**
**β β³β  ΟΟΡΞΉΠΌΡ   :**  `{uptime}`
**β β³β  Ξ±Π²ΟΡΡ    :**  **{abuse_m}**
**β β³β  ΡΟβΟ      :**  **{is_sudo}**
**ββββββββββββββββββββ
"""
botname = Config.BOT_USERNAME

@bot.on(d3vil_cmd(pattern="d3vil$"))
@bot.on(sudo_cmd(pattern="d3vil$", allow_sudo=True))
async def d3vil_a(event):
    try:
        d3vil = await bot.inline_query(botname, "alive")
        await d3vil[0].click(event.chat_id)
        if event.sender_id == d3krish:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "d3vil", None, "Shows Inline Alive Menu with more details."
).add()

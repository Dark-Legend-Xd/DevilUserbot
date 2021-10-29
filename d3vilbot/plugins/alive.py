from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

d3vil_pic = Config.ALIVE_PIC or "https://telegra.ph/file/e74b430f6153a998cec81.jpg"
pm_caption = "  __**🔥🔥∂єνιℓвσт ιѕ αℓινє🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 ↼𝗠𝗔𝗦𝗧𝗘𝗥⇀\n  **『 {d3vil_mention} 』**\n\n"
)
pm_caption += f"╔══════════════════╗\n"
pm_caption += f"╠•➳➠ `тєℓєтнσи:` `{tel_ver}` \n"
pm_caption += f"╠•➳➠ `νєяѕισи:` `{d3vil_ver}`\n"
pm_caption += f"╠•➳➠ `ѕυ∂σ:` `{is_sudo}`\n"
pm_caption += f"╠•➳➠ `¢нαииєℓ:` [𝙹𝗈𝗂𝗇](https://t.me/Devil_Us3rB0t)\n"
pm_caption += f"╠•➳➠ `ѕυρρσят:` [∂єνιℓвσт ¢нαт](https://t.me/devilBot_chat)\n"
pm_caption += f"╠•➳➠ `¢яєαтσя:` [𝙳3𝚅𝙸𝙻𝙶𝚄𝙻𝚂𝙷𝙰𝙽](https://t.me/pro_error_xd)\n"
pm_caption += f"╚══════════════════╝\n"
pm_caption += " [⚡REPO⚡](https://github.com/Dark-Legend-Xd/DevilBot) 🔹 [📜License📜](https://github.com/Dark-Legend-Xd/DevilBot/blob/main/LICENSE)"


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
**⚡ ∂єνιℓвσт ιѕ σиℓιиє ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**↼𝗠𝗔𝗦𝗧𝗘𝗥⇀   :**  **『{d3vil_mention}』**
**╔══════════════════╗**
**╠➳➠ тєℓєтнσи :**  `{tel_ver}`
**╠➳➠ ∂єνιℓвσт  :**  **{d3vil_ver}**
**╠➳➠ υρтιмє   :**  `{uptime}`
**╠➳➠ αвυѕє    :**  **{abuse_m}**
**╠➳➠ ѕυ∂σ      :**  **{is_sudo}**
**╚══════════════════╝
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

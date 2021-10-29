from telethon import events
from . import *
#from d3vilbot import YOUR_NAME
from d3vilbot import bot

D3VIL_USER = bot.me.first_name
d3krish = bot.uid
d3vil_mention = f"[{D3VIL_USER}](tg://user?id={d3krish})"

d3vil_pic = Config.ALIVE_PIC or "https://telegra.ph/file/2bf0c83da574c94f5af8c.jpg"
pm_caption = "  __**🔥🔥∂єνιℓвσт ιѕ αℓινє🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 ↼𝗠𝗔𝗦𝗧𝗘𝗥⇀\n  **『 {d3vil_mention} 』**\n\n"
)
pm_caption += f"╔══════════════════╗\n"
pm_caption += f"╠•➳➠ `тєℓєтнσи:` `1.23.0` \n"
pm_caption += f"╠•➳➠ `νєяѕισи:` `2.0.5`\n"
pm_caption += f"╠•➳➠ `¢нαииєℓ:` [𝙹𝗈𝗂𝗇](https://t.me/Devil_Us3rB0t)\n"
pm_caption += f"╠•➳➠ `ѕυρρσят:` [∂єνιℓвσт ¢нαт](https://t.me/devilBot_chat)\n"
pm_caption += f"╠•➳➠ `¢яєαтσя:` [¢яєαтσя](https://t.me/pro_error_xd)\n"
pm_caption += f"╚══════════════════╝\n"
pm_caption += " [⚡REPO⚡](https://github.com/Dark-Legend-Xd/DevilBot) 🔹 [📜License📜](https://github.com/Dark-Legend-Xd/DevilBot/blob/main/LICENSE)"

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, d3vil_pic, caption=pm_caption)

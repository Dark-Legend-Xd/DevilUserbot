from telethon import events
from . import *
#from d3vilbot import YOUR_NAME
from d3vilbot import bot

D3VIL_USER = bot.me.first_name
d3krish = bot.uid
d3vil_mention = f"[{D3VIL_USER}](tg://user?id={d3krish})"

d3vil_pic = Config.ALIVE_PIC or "https://telegra.ph/file/2bf0c83da574c94f5af8c.jpg"
pm_caption = "  __**π₯π₯βΡΞ½ΞΉβΠ²ΟΡ ΞΉΡ Ξ±βΞΉΞ½Ρπ₯π₯**__\n\n"

pm_caption += f"**ββββββββββββββββββββ**\n\n"
pm_caption += (
    f"                 βΌπ ππ¦π§ππ₯β\n  **γ {d3vil_mention} γ**\n\n"
)
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += f"β β’β³β  `ΡΡβΡΡΠ½ΟΠΈ:` `1.23.0` \n"
pm_caption += f"β β’β³β  `Ξ½ΡΡΡΞΉΟΠΈ:` `2.0.5`\n"
pm_caption += f"β β’β³β  `Β’Π½Ξ±ΠΈΠΈΡβ:` [πΉπππ](https://t.me/Devil_Us3rB0t)\n"
pm_caption += f"β β’β³β  `ΡΟΟΟΟΡΡ:` [βΡΞ½ΞΉβΠ²ΟΡ Β’Π½Ξ±Ρ](https://t.me/devilBot_chat)\n"
pm_caption += f"β β’β³β  `Β’ΡΡΞ±ΡΟΡ:` [Β’ΡΡΞ±ΡΟΡ](https://t.me/pro_error_xd)\n"
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += " [β‘REPOβ‘](https://github.com/Dark-Legend-Xd/DevilBot) πΉ [πLicenseπ](https://github.com/Dark-Legend-Xd/DevilBot/blob/main/LICENSE)"

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, d3vil_pic, caption=pm_caption)

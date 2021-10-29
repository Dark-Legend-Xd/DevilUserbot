import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from d3vilbot import LOGS, bot, tbot
from d3vilbot.config import Config
from d3vilbot.utils import load_module, start_assistant
from d3vilbot.version import __d3vil__ as d3vilver
hl = Config.HANDLER
D3VIL_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/e74b430f6153a998cec81.jpg"

LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    

# let's get the bot ready
async def d3vil_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"D3VILBOT_SESSION - {str(e)}")
        sys.exit()


# Userbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("༆𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝚄𝚂𝙴𝚁𝙱𝙾𝚃༆")
            bot.loop.run_until_complete(d3vil_bot(Config.BOT_USERNAME))
            LOGS.info("✵𝙳E𝚅𝙸𝙻𝙱𝙾𝚃 𝚂𝚃𝙰𝚁𝚃𝚄𝙿 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳✵")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "d3vilbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

assistant = os.environ.get("ASSISTANT", None)
async def assistants():
    if assistant == "ON":
        path = "d3vilbot/assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_assistant(shortname.replace(".py", ""))


bot.loop.run_until_complete(assistants())

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/TEAM-D3VIL/D3VILADDONS"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "d3vilbot/plugins/*.py"
#     files = glob.glob(path)
#      for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))

# let the party begin...
LOGS.info("➪𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝙱𝙾𝚃 𝙼𝙾𝙳𝙴")
tbot.start()
LOGS.info("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
LOGS.info(
    "𝖧𝖾𝖺𝖽 𝗍𝗈 @DevilBot_Chat 𝖿𝗈𝗋 𝖴𝗉𝖺𝖽𝗍𝖾 𝖭𝖾𝗐. 𝖠𝗅𝗌𝗈 𝗃𝗈𝗂𝗇 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 to 𝗀𝖾𝗍 𝗎𝗉𝖽𝖺𝗍𝖾 𝗋𝖾𝗀𝖺𝗋𝖽𝗂𝗇𝗀 𝗍𝗈 𝖣e𝗏𝗂𝗅𝖡𝗈𝗍."
)
LOGS.info("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

# that's life... Devil Boy is Op
async def d3vil_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                D3VIL_PIC,
                caption=f"ℓєgєи∂αяу αf ∂єνιℓвσт\n\n**𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ➪ {d3vilver}**\n\n𝐓𝐲𝐩𝐞 `{hl}ping` or `{hl}alive` 𝐭𝐨 𝐜𝐡𝐞𝐜𝐤! \n\nJoin [∂єνιℓвσт](t.me/Devil_Us3rb0t) for Updates & [∂єνιℓвσт ¢нαт](t.me/DevilBot_chat) fσяє αиу qυєяу яєgαя∂ιиg ∂єνιℓвσт",
            )
    except Exception as e:
        LOGS.info(str(e))


    try:
        await bot(JoinChannelRequest("@Devil_Us3rb0t"))
    except BaseException:
        pass


bot.loop.create_task(d3vil_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()



from hellbot import *
from hellbot.config import Config
from hellbot.helpers import *
from hellbot.utils import *


HELL_USER = Config.YOUR_NAME or "Hêll"
ForGo10God = bot.uid
hell_mention = f"[{HELL_USER}](tg://user?id={ForGo10God})"
hell_logo = "./hellbot/resources/hellbot_logo.jpg"


sudos = Config.SUDO_USERS

if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

chnl_link = "https://t.me/the_hellbot"
hell_channel = f"[†hê Hêllẞø†]({chnl_link})"

# will add more soon

# hellbot

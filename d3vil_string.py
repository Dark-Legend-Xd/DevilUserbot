import os
os.system("pip install telethon")
import telethon
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


okvai = input("Enter yes/y to continue & Enter no/n to stop: ")
if okvai == "y" or "yes":

    print("Please go to my.telegram.org and get your API Id and API Hash to proceed.")
    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")

    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        print(client.session.save())
        client.send_message("me", client.session.save())
        client.send_message("me", "Above is your #DEVILBOT_SESSION \nPaste this string in Heroku Var.\n\n[тєαм ∂єνιℓ](t.me/dev1l_userbot)")

else:
    print("Your Devil string session genreted successfully. Join for query dev1l_userbot)

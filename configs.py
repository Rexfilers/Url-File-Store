# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "11792434"))
  API_HASH = os.environ.get("API_HASH", "01e88901122505e544f89ac04540063e")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6502053475:AAFUb8EgJwzdhVZBhg7eSbQ3YfD36v9BqWU")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mvpsfilebot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001749570382"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "api.shareus.io")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1642086010"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://yeleci3611:1234@cluster0.vltv8hr.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001916608066")
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [@Rambo](https://t.me/Rexisop99)
 
 I am Super noob Please Support My Hard Work.

"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent FileStore Bot.

Join: @Movies_Provide"""

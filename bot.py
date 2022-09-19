# copyright @heartlog
import os
from configs import Config
from pyrogram import Client, filters, errors

plugins = dict(root="plugins")

app = Client(
    "my_bot",
    api_id=Config.API_ID, api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=plugins
)

app.run()

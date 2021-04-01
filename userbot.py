# import logging
from pyrogram import Client, idle

app = Client("tgvc")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> VC CHODNA STARTED')
idle()
app.stop()
print('\n>>> VC CHODNA STOPPED')

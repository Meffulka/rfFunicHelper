from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

load_dotenv()

api_id =  int(os.getenv('api_id'))
api_hash = os.getenv('api_hash')
nickname = os.getenv('nickname')
client = TelegramClient(nickname, api_id, api_hash)
chat_id = int(os.getenv('chat_id'))

@client.on(events.NewMessage(chats=('https://t.me/rf_telegram_bot')))
async def normal_handler(event):
#    print(event.message)
    # pprint.pprint(event.message.to_dict())
    msgDict = event.message.to_dict()
    if not event.out:
        if 'Ты направляешься в следующую пещеру🐾, прибудешь через 0 мин. 30 сек.' in msgDict['message']:
            await client.send_message(chat_id, message='шагнул')
        elif 'Ты прибыл в пещеру' in msgDict['message']:
            await client.forward_messages(chat_id, event.message)

client.start()
client.run_until_disconnected()
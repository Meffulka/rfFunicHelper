from telethon import TelegramClient, events
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

logger.info("Bot started")

load_dotenv()

logger.info(".env loaded")

api_id =  int(os.getenv('api_id'))
api_hash = os.getenv('api_hash')
nickname = os.getenv('nickname')
client = TelegramClient(nickname, api_id, api_hash)
chat_id = int(os.getenv('chat_id'))

@client.on(events.NewMessage(chats=(577009581)))
async def normal_handler(event):
#    print(event.message)
    # pprint.pprint(event.message.to_dict())
    msgDict = event.message.to_dict()
    if not event.out:
        if 'Ты направляешься в следующую пещеру🐾, прибудешь через 0 мин. 30 сек.' in msgDict['message']:
            await client.send_message(chat_id, message='шагнул')
            logger.info("step to new cave")
        elif 'Ты прибыл в пещеру' in msgDict['message']:
            await client.forward_messages(chat_id, event.message)
            logger.info("Arrive to new cave")

client.start()
client.run_until_disconnected()
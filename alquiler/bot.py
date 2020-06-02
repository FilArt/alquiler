import telegram

from alquiler.local_settings import USER_ID, TOKEN


def send_message(text: str):
    user_id = USER_ID
    token = TOKEN
    bot = telegram.Bot(token)
    bot.send_message(user_id, text)

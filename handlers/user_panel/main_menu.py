from aiogram.types import Message
from utils import load_texts
from keyboards import ReplyKeyboard


async def main_menu(message: Message):
    texts = await load_texts()

    text = None
    if message.text == texts['password_wifi_btn']:
        text = texts['password_wifi']
    elif message.text == texts['support_btn']:
        text = texts['support']
    elif message.text == texts['how_open_close_door_btn']:
        text = texts['how_open_close_door']
    elif message.text == texts['instruction_btn']:
        text = texts['instruction']

    return message.answer(text=text, reply_markup=await ReplyKeyboard.back_to_menu())

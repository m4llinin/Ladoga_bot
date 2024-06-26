from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils import load_texts
from keyboards import ReplyKeyboard
from states.states import Back


async def price_list_menu(message: Message):
    texts = await load_texts()
    return message.answer(text=texts['price_list'], reply_markup=await ReplyKeyboard.price_list())


async def price_list(message: Message, state: FSMContext):
    texts = await load_texts()
    await state.set_state(Back.price_list)

    text = None
    if message.text == texts['living_btn']:
        text = texts['living']
    elif message.text == texts['activities_btn']:
        text = texts['activities']
    elif message.text == texts['additional_services_btn']:
        text = texts['additional_services']
    elif message.text == texts['extend_living_btn']:
        text = texts['extend_living']

    return message.answer(text=text, reply_markup=await ReplyKeyboard.back())

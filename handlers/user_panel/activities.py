from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils import load_texts
from keyboards import ReplyKeyboard
from states.states import Back


async def activities_menu(message: Message):
    texts = await load_texts()
    return message.answer(text=texts['actions'], reply_markup=await ReplyKeyboard.activities())


async def activities(message: Message, state: FSMContext):
    texts = await load_texts()
    await state.set_state(Back.activities)

    text = None
    if message.text == texts['sup_boards_btn']:
        text = texts['sup_boards']
    elif message.text == texts['quadro_btn']:
        text = texts['quadro']
    elif message.text == texts['boat_btn']:
        text = texts['boat']
    elif message.text == texts['sauna_btn']:
        text = texts['sauna']
    elif message.text == texts['fish_stick_btn']:
        text = texts['fish_stick']
    elif message.text == texts['bycycle_btn']:
        text = texts['bycycle']

    return message.answer(text=text, reply_markup=await ReplyKeyboard.back())

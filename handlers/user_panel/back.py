from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from utils import load_texts
from keyboards import ReplyKeyboard
from states.states import Back


async def back(message: Message, state: FSMContext):
    texts = await load_texts()
    states = await state.get_state()
    await state.set_state(None)

    if states == Back.activities:
        return await message.answer(text=texts['actions'], reply_markup=await ReplyKeyboard.activities())
    elif states == Back.price_list:
        return await message.answer(text=texts['price_list'], reply_markup=await ReplyKeyboard.price_list())

from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import Message
from utils import load_texts
from keyboards import ReplyKeyboard


async def start(message: Message, state: FSMContext):
    texts = await load_texts()
    await state.clear()
    return await message.answer(text=texts['start_message'], reply_markup=await ReplyKeyboard.start_kb())


async def back_to_menu(message: Message, state: FSMContext):
    texts = await load_texts()
    await state.set_state(None)
    return await message.answer(text=texts['back_to_menu'], reply_markup=await ReplyKeyboard.start_kb())


async def bad_command(message: Message, state: FSMContext):
    texts = await load_texts()
    await state.set_state(None)
    return await message.answer(text=texts['bad_command'], reply_markup=ReplyKeyboardRemove())

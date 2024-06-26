from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from utils import load_texts, write_texts
from keyboards import InlineKeyboard

from states.states import Text


async def edit_text(callback: CallbackQuery, state: FSMContext):
    texts = await load_texts()
    await state.set_state(None)
    await callback.message.delete()
    return await callback.message.answer(text=texts['edit_text'], reply_markup=await InlineKeyboard.choose_class())


async def choose_subclass(callback: CallbackQuery):
    if callback.data == "actions":
        return await callback.message.edit_reply_markup(reply_markup=await InlineKeyboard.activities())
    return await callback.message.edit_reply_markup(reply_markup=await InlineKeyboard.price_list())


async def wait_text(callback: CallbackQuery, state: FSMContext):
    texts = await load_texts()

    if callback.data != "wait_text":
        await state.update_data(key=callback.data)

    await state.set_state(Text.text)
    await callback.message.delete()
    return await callback.message.answer(text=texts['wait_text'], reply_markup=await InlineKeyboard.back("edit_text"))


async def get_text(message: Message, state: FSMContext):
    texts = await load_texts()
    data = await state.get_data()
    key = data.get('key')

    await write_texts(key, message.html_text)
    await state.clear()
    return await message.answer(text=texts['get_text'].format(text=message.html_text),
                                reply_markup=await InlineKeyboard.back("admin"))

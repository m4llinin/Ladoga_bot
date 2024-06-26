from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards import InlineKeyboard
from utils import load_texts


async def admin(message: Message, state: FSMContext):
    texts = await load_texts()
    await state.set_state(None)
    return await message.answer(text=texts['admin'], reply_markup=await InlineKeyboard.admin_kb())


async def admin_clb(callback: CallbackQuery):
    texts = await load_texts()
    await callback.message.delete()
    return await callback.message.answer(text=texts['admin'], reply_markup=await InlineKeyboard.admin_kb())

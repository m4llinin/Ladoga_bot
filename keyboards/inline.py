import asyncio

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils import load_texts


class InlineKeyboard:
    texts: dict = asyncio.run(load_texts())

    @classmethod
    async def admin_kb(cls):
        kb = [
            [InlineKeyboardButton(text=cls.texts['edit_text_btn'], callback_data='edit_text')]
        ]
        return InlineKeyboardMarkup(inline_keyboard=kb)

    @classmethod
    async def choose_class(cls):
        kb = [
            [InlineKeyboardButton(text=cls.texts['password_wifi_btn'], callback_data='password_wifi')],
            [InlineKeyboardButton(text=cls.texts['actions_btn'], callback_data='actions')],
            [InlineKeyboardButton(text=cls.texts['support_btn'], callback_data='support')],
            [InlineKeyboardButton(text=cls.texts['price_list_btn'], callback_data='price_list')],
            [InlineKeyboardButton(text=cls.texts['how_open_close_door_btn'], callback_data='how_open_close_door')],
            [InlineKeyboardButton(text=cls.texts['instruction_btn'], callback_data='instruction')],
            [InlineKeyboardButton(text=cls.texts['back'], callback_data='admin')]
        ]
        return InlineKeyboardMarkup(inline_keyboard=kb)

    @classmethod
    async def back(cls, data: str):
        kb = [
            [InlineKeyboardButton(text=cls.texts['back'], callback_data=data)]
        ]
        return InlineKeyboardMarkup(inline_keyboard=kb)

    @classmethod
    async def activities(cls):
        kb = [
            [InlineKeyboardButton(text=cls.texts['sup_boards_btn'], callback_data='sup_boards')],
            [InlineKeyboardButton(text=cls.texts['quadro_btn'], callback_data='quadro'),
             InlineKeyboardButton(text=cls.texts['boat_btn'], callback_data='boat')],
            [InlineKeyboardButton(text=cls.texts['sauna_btn'], callback_data='sauna'),
             InlineKeyboardButton(text=cls.texts['fish_stick_btn'], callback_data='fish_stick')],
            [InlineKeyboardButton(text=cls.texts['bycycle_btn'], callback_data='bycycle'), ],
            [InlineKeyboardButton(text=cls.texts['back'], callback_data='edit_text')],
        ]
        return InlineKeyboardMarkup(inline_keyboard=kb)

    @classmethod
    async def price_list(cls):
        kb = [
            [InlineKeyboardButton(text=cls.texts['living_btn'], callback_data='living'),
             InlineKeyboardButton(text=cls.texts['activities_btn'], callback_data='activities')],
            [InlineKeyboardButton(text=cls.texts['additional_services_btn'], callback_data='additional_services'), ],
            [InlineKeyboardButton(text=cls.texts['extend_living_btn'], callback_data='extend_living'), ],
            [InlineKeyboardButton(text=cls.texts['back_to_menu_btn'], callback_data='edit_text')],
        ]
        return InlineKeyboardMarkup(inline_keyboard=kb)

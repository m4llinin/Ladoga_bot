import asyncio

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils import load_texts


class ReplyKeyboard:
    texts: dict = asyncio.run(load_texts())

    @classmethod
    async def start_kb(cls):
        kb = [
            [KeyboardButton(text=cls.texts['password_wifi_btn'])],
            [KeyboardButton(text=cls.texts['actions_btn'])],
            [KeyboardButton(text=cls.texts['support_btn'])],
            [KeyboardButton(text=cls.texts['price_list_btn'])],
            [KeyboardButton(text=cls.texts['how_open_close_door_btn'])],
            [KeyboardButton(text=cls.texts['instruction_btn'])]
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)

    @classmethod
    async def back_to_menu(cls):
        kb = [
            [KeyboardButton(text=cls.texts['back_to_menu_btn'])],
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)

    @classmethod
    async def back(cls):
        kb = [
            [KeyboardButton(text=cls.texts['back'])],
            [KeyboardButton(text=cls.texts['back_to_menu_btn'])]
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)

    @classmethod
    async def activities(cls):
        kb = [
            [KeyboardButton(text=cls.texts['sup_boards_btn'])],
            [KeyboardButton(text=cls.texts['quadro_btn']),
             KeyboardButton(text=cls.texts['boat_btn'])],
            [KeyboardButton(text=cls.texts['sauna_btn']),
             KeyboardButton(text=cls.texts['fish_stick_btn'])],
            [KeyboardButton(text=cls.texts['bycycle_btn'])],
            [KeyboardButton(text=cls.texts['back_to_menu_btn'])]
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)

    @classmethod
    async def price_list(cls):
        kb = [
            [KeyboardButton(text=cls.texts['living_btn']),
             KeyboardButton(text=cls.texts['activities_btn'])],
            [KeyboardButton(text=cls.texts['additional_services_btn'])],
            [KeyboardButton(text=cls.texts['extend_living_btn'])],
            [KeyboardButton(text=cls.texts['back_to_menu_btn'])]
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)

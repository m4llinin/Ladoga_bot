__all__ = ['register_users_handlers']

import asyncio

from aiogram import F, Router
from aiogram.filters import CommandStart

from utils import load_texts

from .start import start, back_to_menu, bad_command
from .main_menu import main_menu
from .activities import activities_menu, activities
from .price_list import price_list_menu, price_list
from .back import back

texts: dict = asyncio.run(load_texts())


def register_users_handlers(router: Router):
    router.message.register(start, CommandStart())
    router.message.register(back_to_menu, lambda x: x.text == texts['back_to_menu_btn'] or x.text.lower() == "меню")
    router.message.register(main_menu, lambda x: x.text in [texts['password_wifi_btn'], texts['support_btn'],
                                                            texts['how_open_close_door_btn'], texts['instruction_btn']])
    router.message.register(activities_menu, F.text == texts['actions_btn'])
    router.message.register(activities,
                            lambda x: x.text in [texts['sup_boards_btn'], texts['boat_btn'], texts['quadro_btn'],
                                                 texts['sauna_btn'], texts['fish_stick_btn'], texts['bycycle_btn']])
    router.message.register(price_list_menu, F.text == texts['price_list_btn'])
    router.message.register(price_list,
                            lambda x: x.text in [texts['living_btn'], texts['activities_btn'],
                                                 texts['additional_services_btn'], texts['extend_living_btn']])
    router.message.register(back, F.text == texts['back'])

    router.message.register(bad_command)
